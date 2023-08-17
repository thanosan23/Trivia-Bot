from translate import Translator

def translate_text(text, language='fr'):
    translator = Translator(to_lang=language)
    translated_text = translator.translate(text)
    return translated_text