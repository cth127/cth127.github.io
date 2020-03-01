import spacy
import nltk
nltk.download('universal_postag')
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import time

sent1 = 'On August 27, 2018, in connection with the consummation of the Merger, Cotiviti Corporation, a Delaware corporation (“Cotiviti Corporation”), and Cotiviti Domestic Holdings, Inc., a Delaware corporation (together with Cotiviti Corporation, the “Borrowers”), each a subsidiary of Cotiviti, repaid in full all outstanding loans, together with interest and all other amounts due in connection with such repayment, under that certain Amended and Restated First Lien Credit Agreement, dated as of September 28, 2016, by and among the Borrowers,  Cotiviti Intermediate Holdings, Inc., a Delaware corporation, the lenders party thereto, and JPMorgan Chase Bank, N.A. as administrative agent for the lenders party thereto (the “Existing Credit Agreement”), and terminated all commitments thereunder. The termination of the Existing Credit Agreement became effective at the effective time of the Merger (the “Effective Time”) on August 27, 2018.'

# NLTK
start = time.time()
print(pos_tag(word_tokenize(sent1), tagset='universal_tagset'))
print("time :", time.time() - start)

# spaCy
start = time.time()
nlp = spacy.load("en_core_web_sm")
doc = nlp(sent1)
res = []
for token in doc:
    a = (str(token.text), str(token.pos_))
    res.append(a)
print(res)
print("time :", time.time() - start)
