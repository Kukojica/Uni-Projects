# -*- coding: windows-1251 -*-
import pandas as pd
import natasha
#5 �������� ��������
with open('text.txt', encoding="utf8") as f:
    text = f.read().replace('\n', '')

doc = natasha.Doc(text)
segmenter = natasha.Segmenter()
doc.segment(segmenter)
morph_vocab = natasha.MorphVocab()
emb = natasha.NewsEmbedding()
ner_tagger = natasha.NewsNERTagger(emb)

dates_extractor = natasha.DatesExtractor(morph_vocab)
n = 0
for i in doc.sents:
    n+=1
    print(f'����������� �{n} - {i.text}')

doc.tag_ner(ner_tagger)
print(doc.spans[:5])
doc.ner.print()

for span in doc.spans:
    span.normalize(morph_vocab)
print(doc.spans[:5])
#{_.text: _.normal for _ in doc.spans if _.text != _.normal}
for i in dates_extractor(text):
    print(i.fact.day, i.fact.month, i.fact.year)

#6
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
eng_text = '''
Whether for 10 minutes or a whole day, it now costs a flat fee of �50 (?43) to park in certain streets in The Hague, including roads around the popular Scheveningen beach.
The pilot scheme in the Dutch city on the North Sea coast, which will last a year, aims to discourage tourists and 
visitors from blocking up the historic centre and seaside roads, particularly on sunny days.
Residents have for years complained that they cannot find a parking space in the centre of the city and at Scheveningen.
To try to change this, the city is making it as expensive to park for a quick stop as for a whole day.
Jurriaan Esser, a spokesperson for the council, said the pilot was starting in a selection of streets so that the �collateral damage� could be measured before considering whether to extend it. Residents and businesses with parking permits will in effect gain priority in the largely residential streets.
'''

rus_text = '''
� ����� ������ �������� Cruise, ������������� General Motors, �������� ���������� �� �������������� ������������� ����������� ����� �� ����� ���-���������. 
�� �� ������ � �������������� ������ ���������� �������� Waymo, ������������� Google, � �� ���� ������ � ������ ����� �����. 
���������� The Washington Post ����������, ������ ������� ������ ��� ���� ��������� ������� ������������� ��������� ������������-���������. 
������� ������������� ����� ���������� ������� �� ��������� � � ���������, ��� � ��� ������ ����� ���������� ��� ���������.
� �������� ������ �� ������ � ���-��������� ������������ ���� ���������� ����� Jaguar. 
��������� ������� �����, ��� ���������� ������. ��������, ������� ����� ������, ������ ������, ��� ��������� ����������: �� ����� �������������� ������ �� ����.
�� ������ ��������������� The Washington Post ����� �����, ������ ����� �������� � � ������� ������-���������, ������� ������������� ��������� � �������������� ������������ ������, � � �� �������� ��-�� ��������� ������ � �������������� �������� ���������� ������� � ������ �������������� � ���������.
���� ������ ���-�� �������, �����, �������� �� �����, � ���������� � ��������� � �������� ������� ����������, ����������� ����� ����������. � ����� ������ ����� ������, ��� � ���� ��� ������. 
��� ����� ������� ���������������, � �������� � ���� �� ������.
������ ������� ����������, ����� ��������, ���������� ����������� � �������������� ���������������� ����� � ���������, ��� ��� ������������� �������� �� 15 �����.
� �� �� ����� �������� �������� �����������, ��� ������������ ������� ������ �������� ������� ��������, ��� ������� ��������.
'''

eng_tokens = nltk.word_tokenize(eng_text)
eng_tagged = nltk.pos_tag(eng_tokens)
eng_entities = nltk.chunk.ne_chunk(eng_tagged)
print(eng_entities)

rus_tokens = nltk.word_tokenize(rus_text)
rus_tagged = nltk.pos_tag(rus_tokens)
rus_entities = nltk.chunk.ne_chunk(rus_tagged)
print(rus_entities)

#7
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

X_train = ["entrepreneur", "environment", "effect", 'determine', 'measure', 'affect', 'faddy', 'salty', 'talkative']
y_train = ["Noun", "Noun", "Noun", 'Verb', 'Verb', 'Verb', 'Adj', 'Adj', 'Adj']
X_test = ["overlap", "overpay", 'ergative']
y_test = ['Noun', 'Verb', 'Adj']

vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

clf = MultinomialNB()
clf.fit(X_train_vectors, y_train)

predicted = clf.predict(X_test_vectors)
print(predicted)
print("Accuracy: ", accuracy_score(predicted, y_test))