from textblob import TextBlob

text = 'I love Git and GitHub!'
blob = TextBlob(text)
print(blob.sentiment)
