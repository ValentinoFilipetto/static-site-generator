from split_nodes import *


def text_to_textnodes(text):
    nodes = split_nodes_delimiter(
        [TextNode(text, TextType.NORMAL_TEXT)], "**", TextType.BOLD_TEXT
    )
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
