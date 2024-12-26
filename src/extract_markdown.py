import re


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def markdown_to_blocks(text):
    splitted_text = text.split("\n\n")
    blocks = []

    for block in splitted_text:
        if block == "":
            continue
        else:
            blocks.append(block.strip())

    return blocks


# def extract_title(markdown):
#     array_of_lines = markdown.split("\n")
#     header = None

#     if array_of_lines[0].startswith("# ", 0, 2):
#         return array_of_lines[0].strip("# ")

#     if header == None:
#         raise Exception("No header found in document")

#     return header
