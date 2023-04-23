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

        with open(f"{self.path_and_file}.md", 'r', encoding='utf-8') as file:
            self.note = file.read()
        
        if (".md" == self.notetype):
            self.note = self._markdown_to_html(self.note)
        
        return self._html_to_plaintext(self.note)
    
    def output_plaintext_notes(self, notes: str):
        with open(f"{_NOTE_DIR}/{self.student}/{self.student}.txt", 'w', encoding='utf-8') as file:
            file.write(notes)

    def _get_note_format(self) -> str:
        """Returns the format of the given `NoteParser.note`."""
        suffix = pathlib.Path(f"{_NOTE_DIR}/{self.student}/{self.student}").suffix

        if suffix in _NOTE_FORMATS:
            return suffix

    def _markdown_to_html(self, markdown_notes: str) -> str:
        """Converts a markdown string to HTML."""

        # markdown_notes = self._remove_markdown_tables(markdown_notes)
        pattern = r"(\|.*\|\n)((\|:?-+:?\|)+\n)((\|.*\|[\n])+)"
        removed_markdown_tables = re.sub(pattern, '', markdown_notes, 0, re.MULTILINE)

        with open(f"{_NOTE_DIR}/{self.student}/{self.student}-table-removed.txt", "w", encoding='utf-8') as file:
            file.write(removed_markdown_tables)

        escaped_markdown = html.escape(removed_markdown_tables)


        result = markdown(escaped_markdown)

        with open(f"{_NOTE_DIR}/{self.student}/{self.student}-generated.html", "w", encoding='utf-8') as file:
            file.write(result)

        return result
    
    def _remove_markdown_tables(self, markdown_text:str) -> str:
        # Define a regular expression pattern to match markdown tables
        pattern = r"(\|.*\|\n)((\|:?-+:?\|)+\n)((\|.*\|[\n])+)"
        
        # Remove the markdown tables using re.sub()
        cleaned_text = re.sub(pattern, '', markdown_text)
        
        return cleaned_text

    def _html_to_plaintext(self, html_notes: str):
        """Converts a """

        soup = bs(html_notes, "html.parser")

         # Clean up h-tags
        for h_tag in soup.find_all(["h1", "h2", "h3"]):
            h_tag.string = self._add_colon_if_last_char_not_dot_or_colon(h_tag.text)


        for tag in soup.find_all():
            tag.string = self.add_dot_if_last_char_not_dot(tag.text.strip())

        tags_to_remove = ["table", "title"]
        self._remove_html_tags(soup=soup, tags=tags_to_remove)

        result = soup.get_text(separator=" ")
        result = result.replace("\n", " ")
        result = result.replace("\t", " ")
        result = re.sub("\s\s+", " ", result)

        with open(f"{self.path_and_file}-cleaned.txt", "w") as file:
            file.write(result)

        return result

    def _remove_html_tags(self, soup: bs, tags: list[str]) -> bs:
        """Removes all instances of the specified html `tag` from the html `soup`."""
        if len(tags) == 0:
            return soup
        
        for tag in tags:
            print(f"Tag: {tag}")
            for html_tag in soup.find_all(tag):
                html_tag.decompose()

        return soup

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
    
def main(args: argparse.Namespace, no_arguments: bool):
    """Main function for the `note_parser` module."""
    if no_arguments:
        print("No arguments provided.")
        parser.print_help()
    else:
        note_parser = NoteParser(args.student, args.filetype)
        plaintext = note_parser()
        note_parser.output_plaintext_notes(plaintext)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a note.")
    parser.add_argument("-s", "--student", type=str, metavar="text", help="The student notes to parse.")
    parser.add_argument("-t", "--filetype", type=str, metavar="text", help="Filetype of the note.")

    main(parser.parse_args(), not (len(sys.argv) > 1))