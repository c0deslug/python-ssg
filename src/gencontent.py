import os, shutil
from block_markdown import *

def copy_folder_to_public(static_dir_path, public_dir_path):

    folder_content = os.listdir(static_dir_path)
    print("Content of folder:")
    print(folder_content)
    # Got list of files/folders, check if file copy it, if dir call copy_folder_to_public
    for item in folder_content:
        item_path = os.path.join(static_dir_path, item)
        print (f"Item path is {item_path}")
        if os.path.basename(item) == '.DS_Store': # ignores MacOS created attribute files 
            continue
        if os.path.isfile(item_path) is True:
            print(f"Copying {item} to public folder.")
            shutil.copy(item_path, public_dir_path)
        else:
            print ("Item is folder, invoking folder copy on it.")
            pubsub = os.path.join(public_dir_path, item) # public subfolder
            os.mkdir(pubsub) # needs to be in the public path so replace static location with public first
            copy_folder_to_public(item_path, pubsub)


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


def generate_page_recursive(from_path, template_path, dest_path, basepath):
    print(f"Generating pages from {from_path} to {dest_path} using {template_path}")
    folder_content = os.listdir(from_path)
    print("Content of folder:")
    print(folder_content)
    for item in folder_content:
        item_path = os.path.join(from_path, item)
        print (f"Item path is {item_path}")
        if os.path.basename(item) == '.DS_Store': # ignores MacOS created attribute files 
            continue
        if os.path.isfile(item_path) is True and item_path.endswith('.md'):
                print(f"{item} is md file, generating page.")
                mdfile = open(item_path, 'r')
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
                template = template.replace('href="/', 'href="' + basepath)
                template = template.replace('src="/', 'src="' + basepath)
                #dest_dir_path = os.path.dirname(dest_path)
                #if dest_dir_path != "":
                #    os.makedirs(dest_dir_path, exist_ok=True)
                to_file = open(os.path.join(dest_path, "index.html"), "w")
                to_file.write(template)    
        else:
            print ("Item is folder, invoking page gen on it.")
            pubsub = os.path.join(dest_path, item) # public subfolder
            os.mkdir(pubsub) # needs to be in the public path so replace static location with public first
            generate_page_recursive(item_path, template_path, pubsub, basepath)




def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title = ""
    for block in blocks:
        if block.startswith("# "):
            title = block.strip("# ")
    if title == "":
        raise Exception("No valid title supplied")
    return title