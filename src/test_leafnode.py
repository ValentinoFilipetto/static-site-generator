import unittest
from leafnode import LeafNode

props = {"href": "https://www.google.com"}
node = LeafNode("p", "This is a paragraph of text.")
node_with_props = LeafNode("a", "Click me!", props)
node_no_value = LeafNode("p", None)
node_no_tag = LeafNode(None, "This is just raw text")


class TestHTMLNode(unittest.TestCase):
    def test_no_value(self):
        with self.assertRaises(Exception):
            node_no_value.to_html()

    def test_eq(self):
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_eq_with_props(self):
        self.assertEqual(
            node_with_props.to_html(), '<a  href="https://www.google.com">Click me!</a>'
        )

    def test_raw_text(self):
        self.assertEqual(node_no_tag.to_html(), "This is just raw text")


if __name__ == "__main__":
    unittest.main()
