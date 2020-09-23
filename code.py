#This is a translator app that will translate any given text in dari and pashtu to English
import googletrans
from googletrans import Translator, constants
from pprint import pprint

#init the Google API translator
translator = Translator()

val=input("Write text here: ")

translation = translator.translate(val)
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
