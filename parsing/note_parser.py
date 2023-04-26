import argparse
import html
import re
import sys
from bs4 import BeautifulSoup as bs
import pathlib
from markdown import markdown

_NOTE_FORMATS = [".md", ".html"]
_NOTE_DIR = "parsing/notes"


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

    def __init__(self, student: str, notetype: str):
        """Initializes a new `NoteParser` instance for the specified `note`."""
        self.student = student
        self.notetype = notetype
        self.path_and_file = f"{_NOTE_DIR}/{self.student}/{self.student}"
        self.path_to_dir = f"{_NOTE_DIR}/{self.student}"

    def __call__(self):
        plaintext = self._parse_note()
        return plaintext

    def _parse_note(self) -> str:
        note_format = self._get_note_format()

        with open(f"{self.path_and_file}{self.notetype}", 'r', encoding='utf-8') as file:
            self.note = file.read()

        if (".md" == self.notetype):
            self.note = self._markdown_to_html(self.note)
        
        return self._html_to_plaintext(self.note)
    
    def output_plaintext_notes(self, notes: str):
        with open(f"{_NOTE_DIR}/{self.student}/{self.student}.txt", 'w', encoding='utf-8') as file:
            file.write(notes)

        return notes

    def _get_note_format(self) -> str:
        """Returns the format of the given `NoteParser.note`."""
        suffix = pathlib.Path(f"{_NOTE_DIR}/{self.student}/{self.student}").suffix

        if suffix in _NOTE_FORMATS:
            return suffix

    def _markdown_to_html(self, markdown_notes: str) -> str:
        """Converts a markdown string to HTML."""

        # Markdown cleanup 
        # Case "**" -> ""
        markdown_notes = markdown_notes.replace("**", "")

        result = markdown(markdown_notes, extensions=['markdown.extensions.tables'])

        return result

    def _html_to_plaintext(self, html_notes: str):
        """Converts a """

        soup = bs(html_notes, "html.parser")

        soup = soup.prettify()

        with open(f"{self.path_and_file}-pretty.html", 'w', encoding='utf-8') as file:
            file.write(soup)

        soup = bs(soup, "html.parser")

        # Remove everything besides the body
        soup = soup.body    

        # Iterate over all tags in the soup
        for tag in soup.find_all(text=True):
            if tag.string and tag.string != '\n':
                # Remove newline characters from the tag contents
                tag.string.replace_with(tag.string.replace('\n', ''))
        
         # Clean up h-tags
        for h_tag in soup.find_all(["h1", "h2", "h3"]):
            h_tag.string = self._add_colon_if_last_char_not_dot_or_colon(h_tag.text)

        for tag in soup.find_all():
            tag.string = self.add_dot_if_last_char_not_dot(tag.text.strip())
                
        tags_to_remove = ["table", "title"]
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
            print(tag)
            for html_tag in soup(tag):
                print(f"{tag}: {html_tag}")
                html_tag.decompose()

        return soup

        raise FileNotFoundError(f"'{suffix}' is not a supported note format.")
    
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

def main(args: argparse.Namespace, no_arguments: bool):
    """Main function for the `note_parser` module."""
    if no_arguments:
        print("No arguments provided.")
        parser.print_help()
    else:
        note_parser = NoteParser(args.student, args.filetype)
        plaintext = note_parser()
        res = note_parser.output_plaintext_notes(plaintext)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a note.")
    parser.add_argument("-s", "--student", type=str, metavar="text", help="The student notes to parse.")
    parser.add_argument("-t", "--filetype", type=str, metavar="text", help="Filetype of the note.")

    main(parser.parse_args(), not (len(sys.argv) > 1))