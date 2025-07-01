from textnode import TextNode, TextType

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