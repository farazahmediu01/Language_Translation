# from enum import auto
# from fnmatch import translate
# from unittest import result
from deep_translator import GoogleTranslator, single_detection
from keys import api_key
import requests
from bs4 import BeautifulSoup


text = "never give up"
languages =  GoogleTranslator.get_supported_languages()[:5] + ["urdu"]# only 5 languages
translations = list()
paa = list()
for language in languages:
    result = GoogleTranslator(source='auto', target=language).translate(text=text) # video only include text not text=text
    translations.append(result)





















print(translations)
