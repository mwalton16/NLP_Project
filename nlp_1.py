from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences

#print(sentences)

words = blob.words

#print(words)

#print(blob.tags)

#print(blob.noun_phrases)

### Sentiment Analysis
'''
print(blob.sentiment.polarity)

for i in sentences:
    print(round(i.sentiment.polarity,3))
'''

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text,analyzer = NaiveBayesAnalyzer())
print(blob.sentiment)

for i in blob.sentences:
    print(i.sentiment.p_pos)

spanish = blob.translate(to = 'es')
print(spanish)

chinese = blob.translate(to = 'zh')
print(chinese)

french = blob.translate(to = 'fr')
print(french)

russian = blob.translate(to = 'ru')
print(russian)

hindi = blob.translate(to = 'hi')
print(hindi)

english = chinese.translate(to = 'en')
print(english)