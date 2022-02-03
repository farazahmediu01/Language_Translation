from fnmatch import translate
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
from keys import api_key
import pandas as pd
import people_also_ask
import requests
import uuid


# variables
text = "water"
languages = GoogleTranslator.get_supported_languages()
ppa = list()  # people_also_ask
translations = list()

# contain a list included all translations
for language in languages:
    result = GoogleTranslator(source='auto', target=language).translate(
        text=text)  # video only include text not text=text
    translations.append(result)

for text in translations:
    response = people_also_ask.get_related_questions(text)
    if response:
        ppa.append(True)
    else:
        ppa.append(False)


all_variables = {"String": translations, "Translated_Language": [
    f"{v}_{k}" for k, v in languages.items()], "PPA": ppa}
df = pd.DataFrame(all_variables)
df.to_csv(str(uuid.uuid4()) + '.csv')