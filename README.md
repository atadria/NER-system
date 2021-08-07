# NER-system
Multi-language NER system based on the spaCy library. 

Function to obtain list of NER entities:
`ner.get_entities`:
* `--text` - text to process
* `--language` - language code

output:

* list of entities, each entity is a Python dict

Currently only 2 languages are supported. 