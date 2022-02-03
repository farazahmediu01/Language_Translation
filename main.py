from fnmatch import translate
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
from keys import api_key
import pandas as pd
import people_also_ask
import requests
import uuid
import itertools

# variables

text = input("\nEnter text which you want to translate: ")

print("\nGoogle Translate contains about 109 languages translating text in all languages might be time consuming depending on internet speed.")
print("In how many languages you want to translate your entered text?\n")

while True:
    n = input("Enter a number: ")
    try:
        n = int(n)
        break
    except:
        print("Enter numbers only: ")
        continue

languages = dict(itertools.islice(
    GoogleTranslator.get_supported_languages(as_dict=True).items(), n))
ppa = list()  # people_also_ask
translations = list()
print("\nProgram starts")
print("\nTranslation start")

# contain a list included all translations
for language in languages:
    result = GoogleTranslator(source='auto', target=language).translate(
        text=text)  # video only include text not text=text
    translations.append(result)
print("Translation complete")
print("Scraping start")

for text in translations:
    response = people_also_ask.get_related_questions(text)
    if response:
        ppa.append(True)
    else:
        ppa.append(False)
print("Scraping complete")
print("Preparing csv\n")


all_variables = {"String": translations, "Translated_Language": [
    f"{v}_{k}" for k, v in languages.items()], "PPA": ppa}
df = pd.DataFrame(all_variables)
print(df)

df.to_csv(str(uuid.uuid4()) + '.csv')
print("\nCompleted..\n")
