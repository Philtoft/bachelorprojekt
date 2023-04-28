import re
from markdown import Markdown, Extension
from markdown.preprocessors import Preprocessor

class RemoveInlineCode(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        # md.registeredExtensions(self)
        md.preprocessors.register(RemoveCodeTagsPreprocessor(md), 'remove_code_tags', 175)

class RemoveCodeTagsPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            if line.startswith('```'):
                new_lines.append(line)
            else:
                new_lines.append(line.replace("`", ""))
        return new_lines