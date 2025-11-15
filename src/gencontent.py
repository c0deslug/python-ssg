import os
from block_markdown import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    mdfile = open(from_path, 'r')
    markdown = mdfile.read()
    mdfile.close()
    tmplfile = open(template_path, 'r')
    template = tmplfile.read()
    tmplfile.close()

    node = markdown_to_html_node(markdown)
    html = node.to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)



def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title = ""
    for block in blocks:
        if block.startswith("# "):
            title = block.strip("# ")
    if title == "":
        raise Exception("No valid title supplied")
    return title