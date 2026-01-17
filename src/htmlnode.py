class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            strings = ""
            for key, value in self.props.items():
                strings += f' {key}="{value}"'
            return strings

    def __repr__(self):
        print(f"This is HTML node with {self.tag} + {self.value} + {self.children} + {self.props}")
    