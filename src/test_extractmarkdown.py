import unittest
from extract_markdown import *


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )

    def test_markdown_to_blocks(self):
        text = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""

        self.assertEqual(
            markdown_to_blocks(text),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n        * This is a list item\n        * This is another list item",
            ],
        )

    def test_markdown_to_blocks_excess_empty_lines(self):
        text = """
        # This is a heading




        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""

        self.assertEqual(
            markdown_to_blocks(text),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n        * This is a list item\n        * This is another list item",
            ],
        )

    # def test_extract_title(self):
    #     text = """# Lorem ipsum dolor sit amet,
    #             consectetur adipiscing elit,
    #             sed do eiusmod tempor incididunt
    #             ut labore et dolore magna aliqua."""
    #     self.assertEqual(extract_title(text), "Lorem ipsum dolor sit amet,")

    # def test_extract_title_with_subheader(self):
    #     text = """# Lorem ipsum dolor sit amet,
    #             consectetur adipiscing elit,
    #             ## sed do eiusmod tempor incididunt
    #             ut labore et dolore magna aliqua."""
    #     self.assertEqual(extract_title(text), "Lorem ipsum dolor sit amet,")

    # def test_missing_header(self):
    #     text = """## Lorem ipsum dolor sit amet,
    #             consectetur adipiscing elit,
    #             sed do eiusmod tempor incididunt
    #             ut labore et dolore magna aliqua."""

    #     with self.assertRaises(Exception):
    #         extract_title(text)


if __name__ == "__main__":
    unittest.main()
