
from pprint import pprint
import goslate
gsd = goslate.Goslate(service_urls=['http://translate.google.fr'])
gs = goslate.Goslate()
sun_fr = gsd.lookup_dictionary('sun', 'fr')

print('Goslate')
pprint(sun_fr)

from nltk.translate import AlignedSent, Alignment

algnsent = AlignedSent(['klein', 'ist', 'das', 'Haus'],  # you need parralle
                       ['the', 'house', 'is', 'small'],  # corpora
                       Alignment.fromstring('0-2 1-3 2-1 3-0'))
# and alignements

print("nltk translate")
print(algnsent.words, algnsent.mots)
