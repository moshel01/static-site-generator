from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return self.value
        else:
            if self.tag == 'p':
                return f"<p>{self.value}</p>"
            elif self.tag == 'a':
                return f'<a {self.props_to_html()}>{self.value}</a>'
            elif self.tag == 'b':
                return f'<b>{self.value}</b>'
            elif self.tag == 'i':
                return f'<i>{self.value}</i>'
            elif self.tag == 'blockquote':
                return f'<blockquote>{self.value}</blockquote>'
            elif self.tag == 'code':
                return f'<code>{self.value}</code>'
            elif self.tag == 'img':
                return f'<img {self.props_to_html()} />'
