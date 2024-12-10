from textnode import TextNode, TextType


def main():
    new_node = TextNode("This is my text", TextType.BOLD_TEXT, "https://hello-world.com")
    print(new_node)


main()