import unittest
from leafnode import LeafNode
from parentnode import ParentNode
from split_nodes import *


class TestSplitNodesDelimeter(unittest.TestCase):

    def test_single_node_with_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" word", TextType.NORMAL_TEXT),
            ],
        )

    def test_single_node_with_bold_delimiter(self):
        node = TextNode("This is text with a **bold block** word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("bold block", TextType.BOLD_TEXT),
                TextNode(" word", TextType.NORMAL_TEXT),
            ],
        )

    def test_single_node_with_italic_delimiter(self):
        node = TextNode("This is text with a *italic block* word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC_TEXT)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("italic block", TextType.ITALIC_TEXT),
                TextNode(" word", TextType.NORMAL_TEXT),
            ],
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC_TEXT)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
            ],
            new_nodes,
        )

    def test_missing_closing_delimiter(self):
        node = TextNode("Hello *world", TextType.NORMAL_TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.ITALIC_TEXT)

    def test_missing_invalid_delimiter(self):
        node = TextNode("Hello *world*", TextType.NORMAL_TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "#", TextType.ITALIC_TEXT)

    def test_single_node_with_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.NORMAL_TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
        )

    def test_double_node_with_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.NORMAL_TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode(
                    "to youtube",
                    TextType.LINK,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
        )

    def test_with_no_links(self):
        node = TextNode(
            "This is text without a link",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text without a link", TextType.NORMAL_TEXT),
            ],
        )

    def test_single_node_with_image(self):
        node = TextNode(
            "This is text with an image ![boot dev](./../image)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_images([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an image ", TextType.NORMAL_TEXT),
                TextNode("boot dev", TextType.IMAGE, "./../image"),
            ],
        )

    def test_double_node_with_images(self):
        node = TextNode(
            "This is text with an image ![boot dev](./../image) and ![youtube](./../images/youtube)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_images([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an image ", TextType.NORMAL_TEXT),
                TextNode("boot dev", TextType.IMAGE, "./../image"),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode(
                    "youtube",
                    TextType.IMAGE,
                    "./../images/youtube",
                ),
            ],
        )


if __name__ == "__main__":
    unittest.main()
