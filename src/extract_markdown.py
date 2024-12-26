from enum import Enum
import re


class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered list"
    O_LIST = "ordered list"
    PARAGRAPH = "paragraph"


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


def is_quote_block(text):
    splitted_block = text.split("\n")

    for line in splitted_block:
        if line.strip() == "":
            continue
        elif line.strip().startswith("> "):
            continue
        else:
            return False

    return True


def is_unordered_list_block(text):
    splitted_block = text.split("\n")

    for line in splitted_block:
        if line.strip() == "":
            continue
        elif line.strip().startswith("* ") or line.strip().startswith("- "):
            continue
        else:
            return False

    return True


def is_ordered_list_block(text):
    splitted_block = text.split("\n")
    cleaned_list = [item for item in splitted_block if item.strip()]

    for i in range(len(cleaned_list)):
        if cleaned_list[i].strip().startswith(f"{i + 1}. "):
            continue
        else:
            return False

    return True


def block_to_block_type(block):

    match block:
        case _ if bool(re.match(r"^#{1,6}\s", block)):
            return BlockType.HEADING
        case _ if block.strip().startswith("```") and block.strip().endswith("```"):
            return BlockType.CODE
        case _ if is_quote_block(block) == True:
            return BlockType.QUOTE
        case _ if is_unordered_list_block(block) == True:
            return BlockType.U_LIST
        case _ if is_ordered_list_block(block) == True:
            return BlockType.O_LIST
        case _:
            return BlockType.PARAGRAPH


# def extract_title(markdown):
#     array_of_lines = markdown.split("\n")
#     header = None

#     if array_of_lines[0].startswith("# ", 0, 2):
#         return array_of_lines[0].strip("# ")

#     if header == None:
#         raise Exception("No header found in document")

#     return header
