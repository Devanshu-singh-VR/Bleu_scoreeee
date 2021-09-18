import nltk

t = 'hello how are you i am good here'
m = 'hello baby are you i am fine here'
hypothesis = m.split()
reference = t.split()
#there may be several references
BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
print(BLEUscore)