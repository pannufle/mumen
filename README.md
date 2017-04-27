# MuMEN

[![GitHub release][release-image]][release-url]
[![Build][travis-image]][travis-url]
[![Dependencies][requires-image]][requires-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]
[![MIT License][license-image]][license-url]

## Specifications
1. Input pairs of words from the MEN dataset and output translated pairs in a target language
2. Input pairs of words from the MEN dataset and output a set of questions formatted for YACAB
3. Input a YACAB dump containing a list of crowdsourced annotations and output a MEN dataset

## Useful stuff

### Dictionaries
[WordNet](http://wordnet.princeton.edu/), [FreeDict](http://freedict.org/en/) and [JMDict](http://edrdg.org/jmdict/j_jmdict.html)

### Arabic Preprocessing

The [Stanford Arabic NLP Toolkit](https://nlp.stanford.edu/projects/arabic.shtml) offers:

* A dependency parser trained on the Penn Arabic Treebank
* A word segmenter
* A POS tagger

The [Microsoft Arabic NLP Toolkit](https://www.microsoft.com/en-us/research/project/arabic-toolkit-service-atks/) offers:

* A diacritizer
* A NER
* A morphological analyzer
* A speller
* A transliterator

In terms of corpora, if Wikipedia is not enough we could use the [Gigaword corpus](https://catalog.ldc.upenn.edu/LDC2003T12). Apparently it contains
nearly 400 million words.

### Japanese Preprocessing

There are several popular tools in the Japanese NLP community:
* [Mecab](https://taku910.github.io/mecab/) a POS tagger and morphological
analyzer for Japanese
* [Cabocha](http://taku910.github.io/cabocha/) a dependency-structure analyzer

Both are coded in C++ by [Taku Kudo](http://chasen.org/~taku/index.html.en)
but there are some Python wrappers available on GitHub.

* [Kuromoji](http://www.atilika.org/) also does the same thing as Mecab, but
is coded in Java. It seems well maintained (see their [GitHub](https://github.com/atilika/kuromoji)).

In terms of corpora, a good list is available [here](https://www.ninjal.ac.jp/english/database/type/corpora/) and the
balanced corpus of contemporary written Japanese
([BCCWJ](http://pj.ninjal.ac.jp/corpus_center/bccwj/en/)) contains roughly
100 million words (I have a copy of the corpus) but with extensive
morphological annotation.

[release-image]:https://img.shields.io/github/release/akb89/mumen.svg?style=flat-square
[release-url]:https://github.com/akb89/mumen/releases/latest
[travis-image]:https://img.shields.io/travis/akb89/mumen.svg?style=flat-square
[travis-url]:https://travis-ci.org/akb89/mumen
[coverage-image]:https://img.shields.io/codeclimate/coverage/github/akb89/mumen.svg?style=flat-square
[coverage-url]:https://codeclimate.com/github/akb89/mumen/coverage
[quality-image]:https://img.shields.io/codeclimate/github/akb89/mumen.svg?style=flat-square
[quality-url]:https://codeclimate.com/github/akb89/mumen
[license-image]:http://img.shields.io/badge/license-MIT-000000.svg?style=flat-square
[license-url]:LICENSE.txt
[requires-url]: https://requires.io/github/akb89/mumen/requirements
[requires-image]: https://img.shields.io/requires/github/akb89/mumen.svg?style=flat-square
