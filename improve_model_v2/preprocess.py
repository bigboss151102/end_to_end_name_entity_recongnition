import spacy
from spacy.tokens import DocBin
import pickle

nlp = spacy.blank("en")

training_data = pickle.load(
    open("E:/FILE of Trong/NLP Project/ner/improve_model_v2/data/TrainData.pickle", "rb"))
testing_data = pickle.load(
    open("E:/FILE of Trong/NLP Project/ner/improve_model_v2/data/TestData.pickle", "rb"))

# the DocBin will store the example documents
db_train = DocBin()
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations['entities']:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db_train.add(doc)
db_train.to_disk(
    "E:/FILE of Trong/NLP Project/ner/improve_model_v2/data/train.spacy")

db_test = DocBin()
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations['entities']:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db_test.add(doc)
db_test.to_disk(
    "E:/FILE of Trong/NLP Project/ner/improve_model_v2/data/test.spacy")
