from sphinx.builders.text import TextBuilder
from .writer import CleanIndexWriter


from docutils.parsers.rst import Directive
class NullDirective(Directive):
    has_content = True

    def run(self):
        return []


class CleanTextBuilder(TextBuilder):
    name = 'index_text'
    out_suffix = '.rst.txt'

def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_builder(CleanTextBuilder)
    app.set_translator(name="index_text", translator_class=CleanIndexWriter)

    if app.buildername == "index_text":
        app.add_directive('screenshot', NullDirective)
        app.add_directive('contents', NullDirective)

    return {
        'version': 1,
    }