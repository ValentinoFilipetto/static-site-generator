from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("HTML error: tag is required in parent node")
        elif self.children is None:
            raise ValueError("HTML error: children is required in parent node")
        else:
            content = ""
            for child in self.children:
                if child.value is not None:
                    content = content + child.to_html()
                else:
                    res = child.to_html()
                    content = content + res

            return f"<{self.tag}>{content}</{self.tag}>"
