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

def copy_folder_to_public(static_dir_path, public_dir_path):

    folder_content = os.listdir(static_dir_path)
    print("Content of folder:")
    print(folder_content)
    # Got list of files/folders, check if file copy it, if dir call copy_folder_to_public
    for item in folder_content:
        item_path = os.path.join(static_dir_path, item)
        print (f"Item path is {item_path}")
        if os.path.isfile(item_path) is True:
            print(f"Copying {item} to public folder.")
            shutil.copy(item_path, public_dir_path)
        else:
            print ("Item is folder, invoking folder copy on it.")
            pubsub = os.path.join(public_dir_path, item) # public subfolder
            os.mkdir(pubsub) # needs to be in the public path so replace static location with public first
            copy_folder_to_public(item_path, pubsub)




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
    generate_page(
        os.path.join(content_dir_path, "index.md"),
        template_path,
        os.path.join(public_dir_path, "index.html"),
    )

    #os.path.relpath(get_script_dir())


main()