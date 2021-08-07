import argparse

from languages import get_model


def get_entity_dict(entity):
    return {
        'text': entity.text,
        'type': entity.label_,
        'start_pos': entity.start,
        'end_pos': entity.end
    }


def get_entities(text, language):
    # TODO: reuse model
    model = get_model(language)
    doc = model(text)
    entities = []
    for ent in doc.ents:
        entities.append(get_entity_dict(ent))
    return entities


def main(text, language):
    entities = get_entities(text, language)
    print(entities)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--language')
    parser.add_argument('--text')
    arguments = vars(parser.parse_args())
    main(**arguments)
