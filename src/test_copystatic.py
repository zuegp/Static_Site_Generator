import unittest

from copystatic import extract_title

class Testcopystatic(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is a title

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        title = extract_title(md)
        self.assertEqual(title, "This is a title")

    def test_extract_title_notitle(self):
        md = """
This is a title

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        with self.assertRaises(ValueError, msg=("no header found!")):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()