import re
from bs4 import BeautifulSoup as bs
import pathlib
from markdown import markdown
from exceptions.exceptions import NoSupportedFileTypeFoundError 
from parsing.markdown_preprocessor import RemoveInlineCode

_NOTE_FORMATS = [".md", ".html"]


class NoteParser:
    """"
    This class is used to parse a note
    Steps:
    - Get note
    - Remove specific html tags:
        - table
    - Clean note from html tags
    - Add colon or dot 
    """

    def __call__(self, file_path) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            file = file.read()
        note_type = self._get_note_format(file_path)

        return self._parse_note(file, note_type)
    
    def _get_note_format(self, file_path: str) -> str:
        """Returns the format of the given `NoteParser.note`."""
        suffix = pathlib.Path(file_path).suffix

        if suffix in _NOTE_FORMATS:
            return suffix

        raise NoSupportedFileTypeFoundError(suffix)

    def _parse_note(self, file: str, format: str) -> str:
        if (".md" == format):
            note = self._markdown_to_html(file)
        
        return self._html_to_plaintext(note, format)

    def _markdown_to_html(self, markdown_notes: str) -> str:
        """Converts a markdown string to HTML."""

        # Markdown cleanup 
        # Case "**" -> ""
        markdown_notes = markdown_notes.replace("**", "")

        # Case "```\w*```" -> "" remove everything between ``` and ```
        markdown_notes = re.sub(r"```.*?```", "", markdown_notes, flags=re.DOTALL)

        result = markdown(markdown_notes, extensions=['markdown.extensions.tables', 'pymdownx.superfences', RemoveInlineCode()])

        return result

    def _html_to_plaintext(self, html_notes: str, format: str):
        """Converts a """

        soup = bs(html_notes, "html.parser")
        soup = soup.prettify()
        soup = bs(soup, "html.parser")

        # Remove everything besides the body
        if format == ".html":
            for tag in soup.find_all(text=True):
                if tag.string and tag.string != '\n':
                    # Remove newline characters from the tag contents
                    tag.string.replace_with(tag.string.replace('\n', ''))
        
         # Clean up h-tags
        for h_tag in soup.find_all(["h1", "h2", "h3"]):
            h_tag.string = self._add_colon_if_last_char_not_dot_or_colon(h_tag.text)

        for tag in soup.find_all():
            tag.string = self.add_dot_if_last_char_not_dot(tag.text.strip())
                
        tags_to_remove = ["table", "code"]
        soup = self._remove_html_tags(soup=soup, tags=tags_to_remove)

        result = soup.get_text(separator=" ")
        result = result.replace("\n", ". ")
        result = result.replace("\t", " ")

        result = self.final_cleanup(result)

        return result

    def _remove_html_tags(self, soup: bs, tags: list[str]) -> bs:
        """Removes all instances of the specified html `tag` from the html `soup`."""
        if len(tags) == 0:
            return soup
        
        for tag in tags:
            for html_tag in soup(tag):
                html_tag.decompose()

        return soup
    
    def _check_if_text_needs_refactoring(self, text: str):
        text = text.strip()
        if len(text) > 0 and text[-1] != "." and text[-1] != ":" and text[-1] != "?":
            return True
        return False
    
    def _add_colon_if_last_char_not_dot_or_colon(self, text: str):
        if self._check_if_text_needs_refactoring(text):
            text = "" + text.replace("\n", "") + ": "
        return "" + text + " "

    def add_dot_if_last_char_not_dot(self, text: str):
        if self._check_if_text_needs_refactoring(text):
            text = "" + text + "."
        return "" + text + ""
    
    # Cleanup from different cases in notes
    def final_cleanup(self, notes: str):
        patterns = [
            (r"…", ""),                         # Case "…" -> ""
            (r"\-{3,}", ""),                    # Case "---" -> ""
            (r"\*{2,}", ""),                    # Case "**" -> ""
            (r"\|\.\s{0,}\|", ". "),            # Case "|. |" -> ". "
            (r"\|", ""),                        # Case "|" -> ""
            (r"\s\.\s", ". "),                  # Case " . " -> ". "
            (r"\.{2,}", ". "),                  # Case ".." -> ". " or "..." -> ". "
            (r":\s{0,}\.", ": "),               # Case ":." -> ": " or ": ." -> ": " or ":  ." -> ": "
            (r"\?\s{0,}\.", ": "),              # Case "?." -> "? " or "?. " -> "? "
            (r"\!\s{0,}\.", ": "),              # Case "!." -> "! " or "! ." -> "! "
            (r"\.{2,}", ". "),                  # Case ".." -> ". " or "..." -> ". "
            (r"\s\s+", " "),                    # Case "  " -> " "
            (r"\s\.\s", ". "),                  # Case " . " -> ". "
            (r"\.{2,}", ". "),                  # Case ".." -> ". " or "..." -> ". "
            (r"\s\s+", " "),                    # Case "  " -> " "
            (r":\.", ":"),                      # Case ":." -> ":"
        ]

        # Case " ." -> ""
        patterns.append((r"\s\.", ""))

        # Remove spaces before kolon -> " :" -> ":"
        patterns.append((r"\s:", ":"))

        # Remove dots after kolon -> ":." -> ":"
        patterns.append((r":\.", ":"))

        # Apply regex patterns
        for pattern, replacement in patterns:
            notes = re.sub(pattern, replacement, notes)

        return notes
