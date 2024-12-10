import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_one(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_two(self):
        node = TextNode(
            "This is a text node", TextType.ITALIC_TEXT, "https://hello.com"
        )
        node2 = TextNode(
            "This is a text node", TextType.ITALIC_TEXT, "https://hello.com"
        )
        self.assertEqual(node, node2)

    def test_diff_one(self):
        node = TextNode(
            "This is a text node", TextType.ITALIC_TEXT, "https://hello.com"
        )
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_diff_two(self):
        node = TextNode(
            "This is a text node", TextType.ITALIC_TEXT, "https://hello.com"
        )
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
