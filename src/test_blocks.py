import unittest
from block_markdown import *


class TestInlineMarkdown(unittest.TestCase):


    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_block_to_block_type(self):
        quote = """
> hello there
> this is a quote
> how are you
"""

        unordered = """
- item one
- item one
- item one
- item one
"""

        ordered = """
1. first
2. second
3. third
4. fourth
"""
        ordered_wrong_order = """
1. first
5. fifth
2. second
3. third
4. fourth
"""

        heading_one = "# heading 1"
        heading_three = "### heading 3"

        code = """
```
this is some code I wrote today
```
"""
        paragraph = "This is just some ordinary text."

        self.assertEqual(BlockType.QUOTE, block_to_block_type(quote))
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(unordered))
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(ordered))
        self.assertEqual(BlockType.HEADING, block_to_block_type(heading_one))
        self.assertEqual(BlockType.HEADING, block_to_block_type(heading_three))
        self.assertEqual(BlockType.CODE, block_to_block_type(code))
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(paragraph))
        self.assertNotEqual(BlockType.ORDERED_LIST, ordered_wrong_order)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )



if __name__ == "__main__":
    unittest.main()


