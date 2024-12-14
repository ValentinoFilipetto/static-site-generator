import unittest
from leafnode import LeafNode
from parentnode import ParentNode

leaves_only_node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

recursive_node = ParentNode(
    "p",
    [
        leaves_only_node,
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

recursive_node_two = ParentNode(
    "p",
    [
        LeafNode("i", "italic text"),
        leaves_only_node,
        ParentNode(
            "p",
            [
                LeafNode("h2", "Hello World"),
                LeafNode("h2", "Hello Python"),
            ],
        ),
    ],
)

node_no_children = ParentNode("p", [])

nested_node = ParentNode("div", [ParentNode("p", [LeafNode("b", "Bold text")])])


class TestParentNode(unittest.TestCase):
    def test_leaves_only_node_test(self):
        self.assertEqual(
            leaves_only_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_recursive_node(self):
        self.assertEqual(
            recursive_node.to_html(),
            "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_recursive_node_two(self):
        self.assertEqual(
            recursive_node_two.to_html(),
            "<p><i>italic text</i><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><h2>Hello World</h2><h2>Hello Python</h2></p></p>",
        )

    def test_nested_node(self):
        self.assertEqual(nested_node.to_html(), "<div><p><b>Bold text</b></p></div>")

    def test_node_no_children(self):
        self.assertEqual(
            node_no_children.to_html(),
            "<p></p>",
        )


if __name__ == "__main__":
    unittest.main()
