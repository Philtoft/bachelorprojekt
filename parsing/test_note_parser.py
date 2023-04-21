import unittest
from note_parser import NoteParser as np


class TestNoteParser(unittest.TestCase):
    def removeTableTags(self):
        self.noteparser = np('table.html')
        with open("./notes/table.html", "r") as f:
            tablesRemoved = self.noteparser._remove_html_table_tags(f.read())
            self.assertEquals(
                tablesRemoved, "<p>Lorem ipsum dollor site amet</p>")


if __name__ == '__main__':
    unittest.main()
