import sys
import unittest

if __name__ == "__main__":
    # Setup import from other directory
    sys.path = [sys.path[0]+"/../src/"]+sys.path

from util import file

class test_file(unittest.TestCase):

    def test_load_text_file(self):
        expResult = "This is a test\nThis is a new line"
        result = file.load_file("/test-files/load-test.txt")
        self.assertEqual(expResult, result)

    def test_file_exists(self):
        self.assertEqual(True, file.exists("./test-files/load-test.txt"))
        self.assertEqual(False, file.exists("./test-files/not-a-file.txt"))

    def test_get_folder_content(self):
        expResult = ["file1.txt", "file2.txt", "file5.txt"]
        result = file.get_folder_content("./test-files/folder-test/")
        self.assertEqual(expResult, result)

if __name__ == "__main__":
    unittest.main()
