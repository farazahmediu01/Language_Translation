from deep_translator import GoogleTranslator, single_detection
from keys import api_key
import requests
from bs4 import BeautifulSoup
import people_also_ask

def status_paa(response, ppa: list):
    if response:
        ppa.append(True)
    else:
        ppa.append(False)


# variables
text = "never give up"
languages =  GoogleTranslator.get_supported_languages()[:5] + ["urdu", "english"]# only 5 languages
translations = list()
ppa = list() # people_also_ask


# contain a list included all translations
for language in languages:
    result = GoogleTranslator(source='auto', target=language).translate(text=text) # video only include text not text=text
    translations.append(result)

for text in translations:
    response = people_also_ask.get_related_questions(text)
    status_paa(response, ppa)

print(translations)
print()
print(ppa)











# print(translations)
