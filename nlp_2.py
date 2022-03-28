### Imports
from textblob import TextBlob
import nltk
from pathlib import Path

import pandas as pd

# nltk.download('stopwords')
from nltk.corpus import stopwords

stops = stopwords.words("english")

# print(stops)

blob = TextBlob("Today is a beautiful day.")
# print(blob.words)

cleanlist = [i for i in blob.words if i not in stops]
# print(cleanlist)

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())
# print(blob.word_counts["juliet"])

items = blob.word_counts.items()
print(items)

items = [i for i in items if i[0] not in stops]
# print(items)

from operator import itemgetter

sorted_items = sorted(items)
# print(sorted_items[:20])

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:20])

df = pd.DataFrame(sorted_items[:20], columns=["Words", "Count"])
print(df)
import matplotlib.pyplot as plt

df.plot.bar(x="Words", y="Count", legend=False)
plt.gcf().tight_layout()
plt.show()
