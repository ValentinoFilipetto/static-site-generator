from textnode import TextNode, TextType


def is_correct_delimiter(delimiter):
    return delimiter == "`" or delimiter == "**" or delimiter == "*"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res = []

    if not is_correct_delimiter(delimiter):
        raise ValueError(f"Error: {delimiter} is an invalid delimiter")

    for node in old_nodes:
        if node.text_type is not TextType.NORMAL_TEXT:
            res.append(node)

        sections = node.text.split(delimiter)
        new_list = []
        if (
            len(sections) % 2 == 0
        ):  # remember: split breaks at every delimiter, even with an empty string!
            raise ValueError("Error: missing closing delimiter")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            elif (
                i % 2 != 0
            ):  # because of .split(), non-text will always be on odd positions
                new_list.append(TextNode(sections[i], text_type))
            else:
                new_list.append(TextNode(sections[i], TextType.NORMAL_TEXT))

    res.extend(new_list)
    return res
