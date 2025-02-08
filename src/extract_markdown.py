from enum import Enum
import re


class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"
    PARAGRAPH = "paragraph"


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def markdown_to_blocks(text):
    blocks = re.split(r"\n\s*\n", text)  # Split on two or more newlines
    return [block.strip() for block in blocks if block.strip()]


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
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.PARAGRAPH
        return BlockType.U_LIST
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.U_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.O_LIST
    return BlockType.PARAGRAPH


def extract_title(markdown):
    array_of_lines = markdown.split("\n")

    if array_of_lines[0].startswith("# ", 0, 2):
        return array_of_lines[0].strip("# ")
    else:
        raise Exception("No header found in document")
