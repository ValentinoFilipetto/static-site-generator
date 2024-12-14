import unittest

from leafnode import LeafNode
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

    def test_text_node_to_html(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(node.text, html_node.value)

    def test_text_node_italics(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")

    def test_text_node_bold(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")

    def test_text_node_error(self):
        node = TextNode("This is a text node", "nonexistent text type")
        with self.assertRaises(Exception):
            node.text_node_to_html_node()


if __name__ == "__main__":
    unittest.main()
