import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions, EntitiesOptions, KeywordsOptions, CategoriesOptions, ConceptsOptions
from IBM_Auth import *
import matplotlib.pyplot as plt
import pandas as pd

authenticator = IAMAuthenticator(f"{apikey}")
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/41704412-d719-41e4-9e65-70158517e68e/v1/analyze?version=2019-07-12')


text_file = r"C:\Users\lucas\Documents\Python\NLP\ontheroad.txt"
data_file = r"C:\Users\lucas\Documents\Python\NLP\datanlu.txt"

with open(text_file,"r") as txt:
    text = txt.read()
    #print(text)
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(
            categories=CategoriesOptions(limit=5),
            concepts=ConceptsOptions(limit=5),
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=10),
            #keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2)
            )).get_result()

    txt.close()

#print(response)
data = json.dumps(response, indent=2)
print(data)

with open(data_file, 'w') as outfile:
    json.dump(response, outfile)
    outfile.close()



# names = [i['text'] for i in data["entities"]]
# df = pd.DataFrame({'names':name})
#
# print(df)
