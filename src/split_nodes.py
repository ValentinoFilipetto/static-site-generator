from extract_markdown import extract_markdown_images, extract_markdown_links
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


def split_nodes_link(old_nodes):
    res = []

    for node in old_nodes:
        if node.text_type is not TextType.NORMAL_TEXT:
            res.append(node)

        sections = []
        extracted_links = extract_markdown_links(node.text)

        if len(extracted_links) != 0:
            for link in extracted_links:
                split_list = node.text.split(f"[{link[0]}]({link[1]})", 1)
                sections.append(split_list[0])
                sections.append(link)
                node.text = split_list[1]
        else:
            sections.append(node.text)

        new_list = []

        for section in sections:
            if sections == "":
                continue
            elif type(section) is tuple:
                new_list.append(TextNode(section[0], TextType.LINK, section[1]))
            else:
                new_list.append(TextNode(section, TextType.NORMAL_TEXT))

    res.extend(new_list)
    return res


def split_nodes_images(old_nodes):
    res = []

    for node in old_nodes:
        if node.text_type is not TextType.NORMAL_TEXT:
            res.append(node)

        sections = []
        extracted_images = extract_markdown_images(node.text)

        if len(extracted_images) != 0:
            for image in extracted_images:
                split_list = node.text.split(f"![{image[0]}]({image[1]})", 1)
                sections.append(split_list[0])
                sections.append(image)
                node.text = split_list[1]
        else:
            sections.append(node.text)

        new_list = []

        for section in sections:
            if sections == "":
                continue
            elif type(section) is tuple:
                new_list.append(TextNode(section[0], TextType.IMAGE, section[1]))
            else:
                new_list.append(TextNode(section, TextType.NORMAL_TEXT))

    res.extend(new_list)
    return res
