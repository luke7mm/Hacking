# Python and api hacking practice. Code copied from:
# https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import praw
from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

# API setup

reddit = praw.Reddit(
    client_id="GpWBc-W46aC3CvnQIkT8TQ",
    client_secret="ZJIcf_odA1chkOHfGIDRVG1Nha0FBQ",
    password="4ZGVtqi3TSZ.G84",
    user_agent="testscript by u/Lukemahan",
    username="Lukemahan",
)

headlines = set()

for submission in reddit.subreddit('politics').new(limit=None):
    headlines.add(submission.title)
    display.clear_output()
    print(len(headlines))

nltk.download('vader_lexicon')

sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:3], width=100)

# pandas

df = pd.DataFrame.from_records(results)
df.head()

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()

df2 = df[['headline', 'label']]
df2.to_csv('reddit_headlines_labels.csv',
           mode='a', encoding='utf-8', index=False)


# Positive headlines


print("Positive headlines:\n")
pprint(list(df[df['label'] == 1].headline)[:5], width=200)

print("\nNegative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:5], width=200)

print(df.label.value_counts())

print(df.label.value_counts(normalize=True) * 100)


fig, ax = plt.subplots(figsize=(8, 8))

counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

plt.show()


input("Press the <Enter> key on the keyboard to exit.")

quit()
