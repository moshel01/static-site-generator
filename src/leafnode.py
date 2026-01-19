from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag = tag, value = value, props = props)

    def to_html(self):
        if self.value is None and self.tag != 'img':
            raise ValueError("LeafNode requires a value if the tag is not 'img'")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        if self.value is None:
            return f'<{self.tag}{props_html}>'
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'
