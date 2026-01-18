from textnode import TextType, TextNode
import re

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
                    if text[i] != '':
                        if i % 2 == 0:
                            new_nodes.append(TextNode(text[i], TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(text[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    image_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_matches

def extract_markdown_links(text):
    link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
        else:
            current_text = node.text
            for i in range(len(images)):
                sections = current_text.split(f"![{images[i][0]}]({images[i][1]})", 1)
                before = sections[0]
                after = sections[1]
                if before != '':
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
                current_text = after
            if current_text != '':
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes
    


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
        else:
            current_text = node.text
            for i in range(len(links)):
                sections = current_text.split(f"[{links[i][0]}]({links[i][1]})", 1)
                before = sections[0]
                after = sections[1]
                if before != '':
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
                current_text = after
            if current_text != '':
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    node = split_nodes_image(node)
    node = split_nodes_link(node)
    node = split_nodes_delimiter(node, '**', TextType.BOLD)
    node = split_nodes_delimiter(node, '_', TextType.ITALIC)
    node = split_nodes_delimiter(node, '`', TextType.CODE)
    return node
