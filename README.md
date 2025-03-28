# Linguistics Robin

Linguistics Robin is a Python linguistics collection that stemmed from a phonetics only library (which is why there is currently more phonetic tooling). Right now, the following algorithms are implemented and supported:

 * Soundex
 * Metaphone
 * Double-Metaphone
 * Refined Soundex
 * Fuzzy Soundex
 * Lein
 * Matching Rating Approach
 * New York State Identification and Intelligence System (NYSIIS)
 
In addition, the following distance metrics:

 * Hamming
 * Levenshtein

More will be added in the future. Please refer to the issues list for algorithms slated for the future.

Pull requests are always welcome to assist with the addition of new algorithms.

## Installation

The module is available in PyPI, just use `pip install linguistics_robin`.


## Usage

```python
>>> from linguistics_robin import Soundex
>>> soundex = Soundex()
>>> soundex.phonetics('Rupert')
'R163'
>>> soundex.phonetics('Robert')
'R163'
>>> soundex.sounds_like('Robert', 'Rupert')
True
```

The same API applies to every algorithm, e.g:

```python
>>> from linguistics_robin import Metaphone
>>> metaphone = Metaphone()
>>> metaphone.phonetics('discrimination')
'TSKRMNXN'
```

You can also use the `distance(word1, word2, metric='levenshtein')` method to find the distance between 2 phonetic representations.

```python
>>> from linguistics_robin import RefinedSoundex
>>> rs = RefinedSoundex()
>>> rs.distance('Rupert', 'Robert')
0
>>> rs.distance('assign', 'assist', metric='hamming')
2
```