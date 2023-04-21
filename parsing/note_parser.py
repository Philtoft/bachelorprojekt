import html
import re
from bs4 import BeautifulSoup as bs
import pathlib

import markdown

_NOTE_FORMATS = [".md", ".html"]
_NOTE_DIR = "data/notes"


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

    def __init__(self, note: str):
        """Initializes a new `NoteParser` instance for the specified `note`."""
        self.note = note

    def __call__(self):
        plaintext = self._parse_note()
        return plaintext

    def _parse_note(self) -> str:
        note_format = self._get_note_format()

        with open(f"{_NOTE_DIR}/{self.note}", 'r', encoding='utf-8') as file:
            note = file.read()
        
        if (note_format == '.md'):
            note = self._markdown_to_html(note)
        
        return self._html_to_plaintext(note)

    def _markdown_to_html(self, markdown_notes: str) -> str:
        """Converts a markdown string to HTML."""

        escaped_markdown = html.escape(markdown_notes)

        return markdown(escaped_markdown)

    def _html_to_plaintext(self, html_notes: str):
        """Converts a """

        soup = bs(html_notes, "html.parser")

         # Clean up h-tags
        for h_tag in soup.find_all(["h1", "h2", "h3"]):
            h_tag.string = self._add_colon_if_last_char_not_dot_or_colon(h_tag.text)

        tags_to_remove = ["table", "title"]
        self._remove_html_tags(html_notes, tags_to_remove)

        result = soup.get_text(separator=" ")
        result = result.replace("\n", " ")
        result = result.replace("\t", " ")
        result = re.sub("\s\s+", " ", result)
        return result


    def _remove_html_tags(self, html_note: str, *tags: str) -> bs:
        """Removes all instances of the specified html `tag` from the html `soup`."""
        soup = bs(html_note, "html.parser")
        
        if len(tags) == 0:
            return soup
        
        for tag in tags:
            for html_tag in soup.find_all(tag):
                html_tag.decompose()

        return soup

    def _get_note_format(self) -> str:
        """Returns the format of the given `NoteParser.note`."""
        suffix = pathlib.Path(f"{_NOTE_DIR}/{self.note}").suffix

        if suffix in _NOTE_FORMATS:
            return suffix

        raise FileNotFoundError(f"'{suffix}' is not a supported note format.")
    
    def _check_if_text_needs_refactoring(self, text: str):
        if len(text) > 0 and text[-1] != "." and text[-1] != ":" and text[-1] != "?":
            return True
        return False
    
    def _add_colon_if_last_char_not_dot_or_colon(self, text: str):
        if self._check_if_text_needs_refactoring(text):
            text = "" + text + ":"
        return "" + text + " "

    def add_dot_if_last_char_not_dot(self, text: str):
        if self._check_if_text_needs_refactoring(text):
            text = "" + text + "."
        return "" + text + ""