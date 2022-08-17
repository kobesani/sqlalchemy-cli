from prompt_toolkit.completion import CompleteEvent
from prompt_toolkit.document import Document

from sqlalchemy_cli.completers import BigQueryCompleter

ce = CompleteEvent(text_inserted=True)
doc = Document("SEL")

bqc = BigQueryCompleter()
bqc.get_completions(doc, ce)

for x in bqc.get_completions(doc, ce):
    print(x)

# SELECT
