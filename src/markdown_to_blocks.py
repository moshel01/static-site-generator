def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    new_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped != '':
            new_blocks.append(stripped)
    return new_blocks