from googletrans import Translator

def rendering(lang, word):
    translator = Translator()
    return translator.translate(word, dest=lang)
