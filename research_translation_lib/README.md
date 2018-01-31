# Research to get translation table.

Here we try to find the way to have the best traduction of our missing words

## Goslate

### Installation

```
pip3 install goslate
```

### Simple Usage
```
>>> import goslate
>>> gs = goslate.Goslate()
>>> print(gs.translate('hello world', 'de'))
hallo welt
```

### Advantages
+ Romanlization
+ Language Detection
+ Concurrent
+ with lookup_dictionary we can get a kind of translation table

### Disadvantage
+ May have some query limits
  + but issues can easely fixed

#### More information:
https://pypi.python.org/pypi/goslate#id8


## nltk IBM Models

use a nltk model to find the probability of the best alignement


### Installation

```
pip3 install nltk
```

### Simple Usage
```
from nltk.translate import AlignedSent, Alignment

algnsent = AlignedSent(['klein', 'ist', 'das', 'Haus'],  # you need parralle
                       ['the', 'house', 'is', 'small'],  # corpora
                       Alignment.fromstring('0-2 1-3 2-1 3-0'))
```

### Advantages
+ No dependencies of google server

### Disadvantage
+ Need many corpora

#### More information:
http://www.nltk.org/api/nltk.translate.html


## py-translate

use a nltk model to find the probability of the best alignement


### Installation

```
pip3 install py-translate
```

### Simple Usage
```
translate [--flags] [source] dest
```

### Example
```
# Translate Hello from French to English
$ translate fr en <<< 'Bonjour, comment allez-vous!
```

### Advantages
+ Have a huge choice of languages
+ Easy to use, just on a sentence or a file
+ Have a great documentation

### Disadvantage
+ Must be use with bash
+ Don't give us probabilities

#### More information:
https://pypi.python.org/pypi/py-translate
