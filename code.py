import googletrans
from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

val=input("Write text here: ")

translation = translator.translate(val)
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
