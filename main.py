from deep_translator import GoogleTranslator
from keys import api_key
from pathlib import Path
import pandas as pd
import people_also_ask
import itertools
import os


def genrate_file_name():
    path = Path("programs/output/")
    files = list(path.iterdir())
    last_file_name = files[-1]
    get_id = last_file_name.name[19:][:-4]
    new_id = str(int(get_id) + 1)
    new_name = "translation_output_" + new_id + ".csv"
    return new_name

# variables
file = Path("programs/output/translation_output_0.csv")
csv_name = file.name
is_file_exists = file.exists()
text = input("\nEnter text which you want to translate: ")
ppa = list()  # people_also_ask
translations = list()


print("\nGoogle Translate contains about 109 languages translating text in all languages might be time consuming depending on internet speed.")
print("In how many languages you want to translate your entered text?\n")

# error checking for input must be a number
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

# contain a list includes all translations
for language in languages:
    result = GoogleTranslator(source='auto', target=language).translate(
        text=text)  # video only include text not text=text
    translations.append(result)
print("Translation complete")
print("Scraping start")

# containing a list included all people ask also status.
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

# df.to_csv(str(uuid.uuid4()) + '.csv')
# print("\nCompleted..\n")

if is_file_exists:
    csv_name = genrate_file_name()
else:
    os.makedirs(Path("programs/output"))

df.to_csv(Path("programs/output") / csv_name )