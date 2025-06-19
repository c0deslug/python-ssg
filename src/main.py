print("hello world")

from textnode import *


def main():
    TN_Object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(TN_Object)


main()