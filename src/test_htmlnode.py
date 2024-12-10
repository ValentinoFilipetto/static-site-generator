import unittest

from htmlnode import HTMLNode

props = {
    "href": "https://www.google.com",
    "target": "_blank",
}
node = HTMLNode("a", "My Link", None, props)
node_without_props = HTMLNode("h1", "My Title", None, None)


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_neq(self):
        self.assertNotEqual(
            node.props_to_html(), ' href="https://www.google.com"target="_blank"'
        )

    def test_no_props(self):
        with self.assertRaises(Exception):
            node_without_props.props_to_html()


if __name__ == "__main__":
    unittest.main()
