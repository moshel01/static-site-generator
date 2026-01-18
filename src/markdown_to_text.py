from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            if delimiter is not None:
                text = node.text.split(f'{delimiter}')
                if len(text) % 2 == 0:
                    raise Exception("invalid markdown syntax")
                real_text = []
                for i in range(len(text)):
                    if text[i] != '':  # Only append non-empty
                        if i % 2 == 0:
                            new_nodes.append(TextNode(text[i], TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(text[i], text_type))
    return new_nodes