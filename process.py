def process_text(text):
    contents = text.split('\n')
    reformatted = "\n".join(contents[1:-2])
    
    return reformatted