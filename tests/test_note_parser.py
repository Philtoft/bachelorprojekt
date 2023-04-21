import unittest
from parsing.note_parser import NoteParser as np
from bs4 import BeautifulSoup as bs


class TestNoteParser(unittest.TestCase):

    def setUp(self) -> None:
        with open("./tests/notes/table.html", "r") as f:
            self.notes = f.read()
            self.note_parser = np(f.read())
            self.maxDiff = 10000


    def test_remove_html_tags_given_table_and_title_tags_removes_table_and_title_tags(self):
        actual = str(self.note_parser._remove_html_tags(self.notes, "table", "title"))
        self.assertNotIn("<table>", actual)
        self.assertNotIn("</table>", actual)
        self.assertNotIn("<title>", actual)
        self.assertNotIn("</title>", actual)


    def test_remove_html_tags_given_title_tag_removes_title_tags(self):
        actual = str(self.note_parser._remove_html_tags(self.notes, "title"))
        self.assertNotIn("<title>", actual)
        self.assertNotIn("</title>", actual)


    def test_remove_html_tags_given_no_tags_removes_nothing(self):
        actual = str(self.note_parser._remove_html_tags(self.notes, ""))
        expected = str(bs(self.notes))
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
