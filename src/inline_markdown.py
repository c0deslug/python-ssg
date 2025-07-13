from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newTNodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newTNodes.append(node)
            continue
        if (node.text.count(delimiter)) % 2 != 0:
            raise ValueError("Unclosed tag detected")
        split_line = (node.text).split(delimiter)
        for i, line in enumerate(split_line):
            if line == "":
                 continue
            if i % 2 == 0:
                tnode = TextNode(line, TextType.TEXT)
                newTNodes.append(tnode)
            else:
                tnode = TextNode(line, text_type)
                newTNodes.append(tnode)
    return newTNodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
    

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
    

def split_nodes_image(old_nodes):
    newTNode = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newTNode.append(node)
            continue
        
        original_text = node.text
        images = extract_markdown_images(original_text)

        if len(images) == 0:
            newTNode.append(node)
            continue

        for image in images:
            
            image_alt = image[0]
            image_link = image[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            
            if len(sections) != 2:
                raise ValueError("Markdown not closed")
            
            original_text = sections[1]
            
            if sections[0] != "":
                newTNode.append(TextNode(sections[0], TextType.TEXT))    
            newTNode.append(TextNode(image_alt, TextType.IMAGE, image_link))
        
        if original_text != "":
            newTNode.append(TextNode(original_text, TextType.TEXT))
    
    return newTNode   



def split_nodes_link(old_nodes):
    newTNode = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newTNode.append(node)
            continue
        
        original_text = node.text
        links = extract_markdown_links(node.text)

        if len(links) == 0:
            newTNode.append(node)
            continue

        for link in links:
            
            link_alt = link[0]
            link_url = link[1]
            sections = original_text.split(f"[{link_alt}]({link_url})", 1)
            
            if len(sections) != 2:
                raise ValueError("Markdown not closed")
            
            original_text = sections[1]
            
            if sections[0] != "":
                newTNode.append(TextNode(sections[0], TextType.TEXT))

            newTNode.append(TextNode(link_alt, TextType.LINK, link_url))
        
        if original_text != "":
            newTNode.append(TextNode(original_text, TextType.TEXT))
    
    return newTNode   
    pass


def text_to_text_nodes(text):

    nodes = [TextNode(text, text_type=TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes



# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     for old_node in old_nodes:
#         if old_node.text_type != TextType.TEXT:
#             new_nodes.append(old_node)
#             continue
#         split_nodes = []
#         sections = old_node.text.split(delimiter)
#         if len(sections) % 2 == 0:
#             raise ValueError("invalid markdown, formatted section not closed")
#         for i in range(len(sections)):
#             if sections[i] == "":
#                 continue
#             if i % 2 == 0:
#                 split_nodes.append(TextNode(sections[i], TextType.TEXT))
#             else:
#                 split_nodes.append(TextNode(sections[i], text_type))
#         new_nodes.extend(split_nodes)
#     return new_nodes