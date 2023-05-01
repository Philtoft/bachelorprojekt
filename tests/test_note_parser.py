import unittest
from parsing.note_parser import NoteParser as np
from bs4 import BeautifulSoup as bs


class TestNoteHTMLParser(unittest.TestCase):

    def setUp(self) -> None:
        with open("./tests/notes/test_case.html", "r") as f:
            self.notes = f.read()
            self.note_parser = np()
            self.maxDiff = 10000
            self.soup = bs(self.notes, "html.parser")

        with open("./tests/notes/test_case.md", "r") as file:
            self.md_note = file.read()


    def test_remove_html_tags_given_table_and_code_tags_removes_all_table_and_code_tags(self):
        actual = str(self.note_parser._remove_html_tags(self.soup, ["table", "code"]))
        self.assertNotIn("<table>", actual)
        self.assertNotIn("</table>", actual)
        self.assertNotIn("<code>", actual)
        self.assertNotIn("</code>", actual)


    def test_remove_html_tags_given_code_tag_removes_all_code_tags(self):
        actual = str(self.note_parser._remove_html_tags(self.soup, ["code"]))
        self.assertNotIn("<code>", actual)
        self.assertNotIn("</code>", actual)


    def test_remove_html_tags_given_no_tags_removes_nothing(self):
        actual = str(self.note_parser._remove_html_tags(self.soup, [""]))
        expected = str(bs(self.notes, "html.parser"))
        self.assertEqual(expected, actual)
    

if __name__ == '__main__':
    unittest.main()
