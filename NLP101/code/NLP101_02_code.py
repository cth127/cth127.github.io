from spacy.lang.en import English
from spacy.pipeline import Sentencizer
from nltk.tokenize import sent_tokenize
import time

sent1 = 'On August 27, 2018, in connection with the consummation of the Merger, Cotiviti Corporation, a Delaware corporation (“Cotiviti Corporation”), and Cotiviti Domestic Holdings, Inc., a Delaware corporation (together with Cotiviti Corporation, the “Borrowers”), each a subsidiary of Cotiviti, repaid in full all outstanding loans, together with interest and all other amounts due in connection with such repayment, under that certain Amended and Restated First Lien Credit Agreement, dated as of September 28, 2016, by and among the Borrowers,  Cotiviti Intermediate Holdings, Inc., a Delaware corporation, the lenders party thereto, and JPMorgan Chase Bank, N.A. as administrative agent for the lenders party thereto (the “Existing Credit Agreement”), and terminated all commitments thereunder. The termination of the Existing Credit Agreement became effective at the effective time of the Merger (the “Effective Time”) on August 27, 2018.'
sent2 = 'At the Effective Time, each share of Cotiviti common stock, par value $0.001 per share (“Common Stock”), issued and outstanding immediately prior to the Effective Time (including shares of Common Stock that were issued as restricted Common Stock that vested on or prior to the date of the consummation of the Merger, but excluding (i) any shares of Common Stock held directly by Verscend, Merger Sub or any of their subsidiaries immediately prior to the Effective Time, (ii) shares of Common Stock held in treasury of Cotiviti and (iii) shares of Common Stock held by any stockholder who has not voted in favor of the adoption of the Merger Agreement or consented thereto in writing and who has properly exercised appraisal rights of such shares of Common Stock in accordance with Section 262 of the Delaware General Corporate Law and has not effectively withdrawn or lost the right to appraisal under Delaware law),  was cancelled and extinguished and automatically converted into the right to receive $44.75 in cash (the “Merger Consideration”), payable to the holder thereof, without interest and less any applicable withholding taxes or other amounts required to be withheld therefrom under applicable law.'

# spaCy
start = time.time()
nlp = English()
doc1 = nlp(sent1)
doc2 = nlp(sent2)
sentencizer = Sentencizer()
res1 = sentencizer(doc1)
res2 = sentencizer(doc2)
for sent in res1.sents :
    print(sent.text)
for sent in res2.sents :
    print(sent.text)
print("time :", time.time() - start)

# NLTK
start = time.time()
print(sent_tokenize(sent1))
print(sent_tokenize(sent2))
print("time :", time.time() - start)
