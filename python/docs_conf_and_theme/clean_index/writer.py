from docutils import nodes
from sphinx.writers.text import TextTranslator

class CleanIndexWriter(TextTranslator):

    def depart_title(self, node):
        # type: (nodes.Node) -> None
        if isinstance(node.parent, nodes.section):
            char = self._title_char
        else:
            char = '^'
        text = None  # type: unicode
        text = ''.join(x[1] for x in self.states.pop() if x[0] == -1)  # type: ignore
        self.stateindent.pop()
        # title = ['', "<b>%s</b>"%text, '']  # type: List[unicode]
        title = ['', "%s"%text, ' --']  # type: List[unicode]
        if len(self.states) == 2 and len(self.states[-1]) == 0:
            # remove an empty line before title if it is first section title in the document
            title.pop(0)
        self.states[-1].append((0, title))

