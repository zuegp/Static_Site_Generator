

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stript_blocks = []
    for block in blocks:
        if block != "":
            stript_blocks.append(block.strip())
    return stript_blocks