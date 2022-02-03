from enum import auto
from fnmatch import translate
from unittest import result
from deep_translator import GoogleTranslator, single_detection
from keys import api_key
import requests
from bs4 import BeautifulSoup


text = "water"
languages =  GoogleTranslator.get_supported_languages()[:5] # only 5 languages
# print(lang_dict)
# print(len(lang_dict))
translation = list()
for language in languages:
    result = GoogleTranslator(source='auto', target=language).translate(text=text) # video only include text not text=text
    translation.append(result)

print(translation)

# print(transalte)