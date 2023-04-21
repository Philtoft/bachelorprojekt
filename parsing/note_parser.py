from bs4 import BeautifulSoup as bs
import pathlib

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
        pass

    def _parse_note() -> str:
        pass

    def _html_to_plaintext(self, html_notes: str):
        """Converts a """

    def _remove_html_table_tags(self, html_note: str):
        """Removes all html table tags from the note."""
        soup = bs(html_note, "html.parser")
        self._remove_html_tags('table', soup)
        return str(soup)

    def _remove_html_tags(self, tag: str, soup: bs):
        """Removes all instances of the specified html `tag` from the html `soup`."""
        for tag in soup.find_all(tag):
            tag.decompose()

    def _get_note_format(self) -> str:
        """Returns the format of the given `NoteParser.note`."""
        suffix = pathlib.Path(f"{_NOTE_DIR}/{self.note}").suffix

        if suffix in _NOTE_FORMATS:
            return suffix

        raise FileNotFoundError(f"'{suffix}' is not a supported note format.")
