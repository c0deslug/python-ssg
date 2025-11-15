from textnode import *
from block_markdown import *
from gencontent import *
import inspect
import os, shutil

def get_source_dir():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def get_static_dirpath(script_path):
    directory = os.path.dirname(script_path)
    return os.path.join(directory, 'static')

def get_public_dirpath(script_path):
    directory = os.path.dirname(script_path)
    return os.path.join(directory, 'public')



def main():
    #TN_Object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(TN_Object)

    script_path = get_source_dir()
    static_dir_path = get_static_dirpath(script_path)
    public_dir_path = get_public_dirpath(script_path)
    content_dir_path = "./content"
    template_path = "./template.html"

    print(static_dir_path)
    print(public_dir_path)

    shutil.rmtree(public_dir_path)
    print("Deleted public folder contents to prepare for copying, creating a new one...")
    os.mkdir(public_dir_path)

    print("Copying static files to public directory...")
    copy_folder_to_public(static_dir_path, public_dir_path)

    print("Generating page...")
    generate_page_recursive(
        content_dir_path,
        template_path,
        public_dir_path
    )

    #os.path.relpath(get_script_dir())


main()