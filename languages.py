import spacy

LANGUAGE_MODEL_MAP = {'pl': 'pl_core_news_sm',
                      'en': 'en_core_web_sm'}


def get_model(language):
    if language in LANGUAGE_MODEL_MAP:
        return spacy.load(LANGUAGE_MODEL_MAP[language])
    else:
        # TODO: Add other languages (get model name based on language code and download it if needed)
        raise NotImplementedError('No model found for language: {}'.format(language))
