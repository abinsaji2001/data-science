print("SJC23MCA-2002 : ABIN SAJI")
print("Batch : MCA 2023-25")
from nltk import ngrams
sentence = 'I reside in India'
n = 3
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
    print(grams)