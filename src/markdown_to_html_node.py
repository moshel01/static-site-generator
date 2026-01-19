from blocktype import BlockType
from markdown_to_text import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type
from htmlnode import *
from textnode import *
from text_node_to_html_node import *
from parentnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.PARAGRAPH:
            raw = block
            lines = [line.strip() for line in raw.split('\n')]
            filtered = [line for line in lines if line]
            paragraph_text = ' '.join(filtered)
            children_nodes.append(ParentNode(tag='p', children=text_to_children(paragraph_text)))

        elif blocktype == BlockType.HEADING:
            hash_count = 0
            for char in block:
                if char == '#':
                    hash_count += 1
                else:
                    break
            children_nodes.append(ParentNode(tag = f'h{hash_count}', children = text_to_children(block[hash_count:].lstrip())))

        elif blocktype == BlockType.QUOTE:
            split = block.split('\n')
            quote = ''
            for line in split:
                quote += f"{line.lstrip('> ')}\n"
            children_nodes.append(ParentNode(tag = 'blockquote', children= text_to_children(quote)))

        elif blocktype == BlockType.CODE:
            split = block.split('\n')
            inner_lines = split[1:-1]
            clean_lines = [line.lstrip() for line in inner_lines]
            new = '\n'.join(clean_lines) + '\n'
            code_text_node = TextNode(new, TextType.CODE)
            code_leaf = text_node_to_html_node(code_text_node) 
            children_nodes.append(ParentNode(tag = 'pre', children = [code_leaf]))
        
        elif blocktype == BlockType.UNORDERED_LIST:
            split = block.split('\n')
            ul_nodes = []
            for line in split:
                if line.strip() != '':
                    ul_nodes.append(ParentNode(tag = 'li', children = text_to_children(line.lstrip('- '))))
            children_nodes.append(ParentNode(tag = 'ul', children = ul_nodes))
        
        elif blocktype == BlockType.ORDERED_LIST:
            split = block.split('\n')
            ol_nodes = []
            for i in range(len(split)):
                if split[i].strip() != '':
                    ol_nodes.append(ParentNode(tag = 'li', children = text_to_children(split[i].lstrip(f'{i+1}. '))))
            children_nodes.append(ParentNode(tag = 'ol', children = ol_nodes))

    block_node = ParentNode(tag = 'div', children = children_nodes)
    return block_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_children = []
    for tn in text_nodes:
        html_children.append(text_node_to_html_node(tn))
    return html_children