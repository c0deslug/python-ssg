from textnode import *
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

def copy_static_to_public(static_dir_path, public_dir_path):
    shutil.rmtree(public_dir_path)
    print("Deleted public folder content to prepare for copying")
    pass


def main():
    #TN_Object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(TN_Object)

    script_path = get_source_dir()
    static_dir_path = get_static_dirpath(script_path)
    public_dir_path = get_public_dirpath(script_path)

    print(static_dir_path)
    print(public_dir_path)

    copy_static_to_public(static_dir_path, public_dir_path)

    #os.path.relpath(get_script_dir())


main()