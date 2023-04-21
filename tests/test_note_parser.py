import unittest
from parsing.note_parser import NoteParser as np


class TestNoteParser(unittest.TestCase):
    def test_remove_table_tags(self):
        self.noteparser = np('table.html')
        with open("./tests/notes/table.html", "r") as f:
            tablesRemoved = self.noteparser._remove_html_table_tags(f.read())
            self.assertNotIn("<table>", tablesRemoved)
            self.assertNotIn("</table>", tablesRemoved)


if __name__ == '__main__':
    unittest.main()
