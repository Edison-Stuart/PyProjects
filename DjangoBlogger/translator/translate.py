from googletrans import Translator

def trans(inText):
    translator = Translator()
    translation = translator.translate(text=inText, dest='de')
    return translation.text
