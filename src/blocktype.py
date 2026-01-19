from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(block):
    if len(block) <=1:
        return BlockType.PARAGRAPH
    stripped = block.strip()
    line_split = block.split('\n')
    if block[0] == '#':
        hash_count = 1
        for char in block:
            if char == '#':
                hash_count += 1
            else:
                break
        if block[hash_count-1] == ' ' and hash_count <=7:
            return BlockType.HEADING
    if block[0:3] == '```' and block[len(block)-3:len(block)+1] == '```' and len(line_split)>1:
        return BlockType.CODE
    quote = 0
    ul = 0
    ol = 0
    for i in range(len(line_split)):
        if line_split[i][0:2] == '> ':
            quote += 1
            continue
        elif line_split[i][0:2] == '- ':
            ul += 1
            continue
        elif line_split[i].startswith(f'{ol+1}. '):
            ol += 1
            continue
        else:
            return BlockType.PARAGRAPH
    if quote == len(line_split):
        return BlockType.QUOTE
    if ul == len(line_split):
        return BlockType.UNORDERED_LIST
    if ol == len(line_split):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH