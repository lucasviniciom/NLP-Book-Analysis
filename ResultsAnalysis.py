import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", color_codes=True)
pal = sns.color_palette("rocket_r")


data_file = r"C:\Users\lucas\Documents\Python\NLP\datanlu.txt"
dt = (open(data_file, "r")).read()



dict = {"usage": {"text_units": 5, "text_characters": 50000, "features": 3}, "language": "en", "entities": [{"type": "Person", "text": "Neal", "sentiment": {"score": 0.300999, "mixed": "1", "label": "positive"}, "relevance": 0.956196, "emotion": {"sadness": 0.555901, "joy": 0.583313, "fear": 0.163971, "disgust": 0.103152, "anger": 0.475075}, "count": 42, "confidence": 1}, {"type": "Person", "text": "Louanne", "sentiment": {"score": -0.605162, "mixed": "1", "label": "negative"}, "relevance": 0.50148, "emotion": {"sadness": 0.200038, "joy": 0.583319, "fear": 0.154528, "disgust": 0.654842, "anger": 0.459947}, "count": 8, "confidence": 1}, {"type": "Person", "text": "Leon Levinsky", "sentiment": {"score": 0.508389, "mixed": "1", "label": "positive"}, "relevance": 0.202614, "emotion": {"sadness": 0.332995, "joy": 0.379312, "fear": 0.167118, "disgust": 0.022147, "anger": 0.267178}, "count": 3, "confidence": 0.999999}, {"type": "Location", "text": "Denver", "sentiment": {"score": -0.287601, "mixed": "1", "label": "negative"}, "relevance": 0.194412, "emotion": {"sadness": 0.566758, "joy": 0.599087, "fear": 0.108402, "disgust": 0.089595, "anger": 0.12068}, "count": 18, "confidence": 1}, {"type": "Person", "text": "Hal Chase", "sentiment": {"score": 0.413351, "label": "positive"}, "relevance": 0.187304, "emotion": {"sadness": 0.092848, "joy": 0.734375, "fear": 0.047488, "disgust": 0.118176, "anger": 0.054897}, "disambiguation": {"subtype": ["Athlete"], "name": "Hal_Chase", "dbpedia_resource": "http://dbpedia.org/resource/Hal_Chase"}, "count": 3, "confidence": 0.999492}, {"type": "Person", "text": "Allen", "sentiment": {"score": -0.356703, "mixed": "1", "label": "negative"}, "relevance": 0.183899, "emotion": {"sadness": 0.286464, "joy": 0.561409, "fear": 0.13653, "disgust": 0.108175, "anger": 0.233032}, "count": 8, "confidence": 1}, {"type": "Location", "text": "Iowa", "sentiment": {"score": -0.471826, "mixed": "1", "label": "negative"}, "relevance": 0.181488, "emotion": {"sadness": 0.5248, "joy": 0.558093, "fear": 0.146782, "disgust": 0.122068, "anger": 0.558357}, "count": 13, "confidence": 1}, {"type": "Location", "text": "Chicago", "sentiment": {"score": -0.537545, "mixed": "1", "label": "negative"}, "relevance": 0.155589, "emotion": {"sadness": 0.602999, "joy": 0.65592, "fear": 0.172181, "disgust": 0.06873, "anger": 0.161164}, "count": 10, "confidence": 1}, {"type": "Person", "text": "Bob Malkin", "sentiment": {"score": 0.311759, "mixed": "1", "label": "positive"}, "relevance": 0.154248, "emotion": {"sadness": 0.22873, "joy": 0.359982, "fear": 0.124505, "disgust": 0.302488, "anger": 0.167912}, "count": 2, "confidence": 0.999898}, {"type": "Person", "text": "Allen Ginsberg", "sentiment": {"score": 0.308586, "mixed": "1", "label": "positive"}, "relevance": 0.145675, "emotion": {"sadness": 0.101451, "joy": 0.72643, "fear": 0.121439, "disgust": 0.047765, "anger": 0.050352}, "disambiguation": {"subtype": ["FilmCharacter", "MusicalArtist", "Writer", "AwardNominee", "AwardWinner", "MusicalGroupMember", "OperaCharacter", "FilmActor", "TVActor"], "name": "Allen_Ginsberg", "dbpedia_resource": "http://dbpedia.org/resource/Allen_Ginsberg"}, "count": 4, "confidence": 1.0}], "concepts": [{"text": "Coming out", "relevance": 0.891916, "dbpedia_resource": "http://dbpedia.org/resource/Coming_out"}, {"text": "On the Road", "relevance": 0.864377, "dbpedia_resource": "http://dbpedia.org/resource/On_the_Road"}, {"text": "Allen Ginsberg", "relevance": 0.838194, "dbpedia_resource": "http://dbpedia.org/resource/Allen_Ginsberg"}, {"text": "Neal Cassady", "relevance": 0.801854, "dbpedia_resource": "http://dbpedia.org/resource/Neal_Cassady"}, {"text": "Beat Generation", "relevance": 0.784961, "dbpedia_resource": "http://dbpedia.org/resource/Beat_Generation"}], "categories": [{"score": 0.715307, "label": "/automotive and vehicles/cars/car culture"}, {"score": 0.710628, "label": "/art and entertainment/shows and events"}, {"score": 0.687486, "label": "/automotive and vehicles/auto parts"}, {"score": 0.649734, "label": "/society/unrest and war"}, {"score": 0.640588, "label": "/family and parenting/children"}], "warnings": ["Text content exceeds 50000 character limit. Only first 50000 characters processed..."]}

#dict = {'usage': {'text_units': 1, 'text_characters': 1912, 'features': 1}, 'language': 'en', 'entities': [{'type': 'Person', 'text': 'Neal', 'sentiment': {'score': 0.437626, 'mixed': '1', 'label': 'positive'}, 'relevance': 0.964181, 'emotion': {'sadness': 0.555779, 'joy': 0.585424, 'fear': 0.125292, 'disgust': 0.094892, 'anger': 0.145464}, 'count': 9, 'confidence': 1}, {'type': 'Person', 'text': 'Hal Chase', 'sentiment': {'score': 0, 'label': 'neutral'}, 'relevance': 0.378211, 'emotion': {'sadness': 0.23918, 'joy': 0.232373, 'fear': 0.177956, 'disgust': 0.098654, 'anger': 0.085211}, 'disambiguation': {'subtype': ['Athlete'], 'name': 'Hal_Chase', 'dbpedia_resource': 'http://dbpedia.org/resource/Hal_Chase'}, 'count': 1, 'confidence': 0.95843}, {'type': 'Person', 'text': 'Hal', 'sentiment': {'score': 0.901088, 'label': 'positive'}, 'relevance': 0.34938, 'emotion': {'sadness': 0.121498, 'joy': 0.632209, 'fear': 0.024292, 'disgust': 0.075739, 'anger': 0.141834}, 'count': 3, 'confidence': 0.999975}]}

name = [i['text'] for i in dict["entities"]]
relevance = [i['relevance'] for i in dict["entities"]]
emotions = [i['emotion'] for i in dict["entities"]]
sentiment = [i['sentiment'] for i in dict["entities"]]

ordered_emot = {}
ordered_sent = {}
#Emotions é uma lista de dictionarios. ordered_dict é um dict com cada emotion e seus valores.
for i in range(len(emotions)):
    for k, v in emotions[i].items():
        ordered_emot.setdefault(k, []).append(v)
for i in range(len(sentiment)):
    for k, v in sentiment[i].items():
        ordered_sent.setdefault(k, []).append(v)

df = pd.DataFrame({'name':name, 'relevance': relevance})
for k, v in ordered_emot.items():
    df[k] = v
df['score'] = ordered_sent.get('score')

print(df)

df.drop('relevance', axis=1)
del df['relevance']
df2 = pd.melt(df, id_vars="name", var_name="emotions", value_name="intensity")
del df['score']
print(df2)
ax = sns.barplot(x='name', y="intensity",  hue="emotions", data=df2, palette=pal)
# ax2 = ax.twinx()
# ax2 = sns.lineplot(data=df, x="name", y="score")

plt.show()
