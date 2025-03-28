import pytest
from linguistics_robin import Soundex, RefinedSoundex, FuzzySoundex, NYSIIS, Metaphone, DoubleMetaphone
from linguistics_robin.exceptions import EmptyStringError

def test_doublemetaphone():
    dm = DoubleMetaphone()

    assert dm.phonetics('maurice') == ('MRS', None)
    assert dm.phonetics('bob') == ('PP', None)
    assert dm.phonetics('walter') == ('ALTR', 'FLTR')

    with pytest.raises(EmptyStringError):
        dm.phonetics('')

def test_metaphone():
    metaphone = Metaphone()

    assert metaphone.phonetics('maurice') == 'MRS'
    assert metaphone.phonetics('bob') == 'BB'

    with pytest.raises(EmptyStringError):
        metaphone.phonetics('')

def test_nysiis():
    nysiis = NYSIIS()

    assert nysiis.phonetics('bob') == 'BAB'
    assert nysiis.phonetics('aa') == 'A'
    assert nysiis.phonetics('b') == 'B'
    assert nysiis.phonetics('cat') == 'CAT'
    assert nysiis.phonetics('s') == 'S'
    assert nysiis.phonetics('w') == 'W'

    with pytest.raises(EmptyStringError):
        nysiis.phonetics('')

def test_soundex():
    soundex = Soundex()
    
    assert soundex.phonetics('h') == 'H000'
    assert soundex.phonetics('hh') == 'H000'
    assert soundex.phonetics('hhh') == 'H000'
    assert soundex.phonetics('d') == 'D000'
    assert soundex.phonetics('dd') == 'D000'
    assert soundex.phonetics('ddd') == 'D000'
    assert soundex.phonetics('ddm') == 'D500'
    assert soundex.phonetics('ddmmmm') == 'D500'
    assert soundex.phonetics('Pffister') == 'P236'
    assert soundex.phonetics('Pfister') == 'P236'

    with pytest.raises(EmptyStringError):
        soundex.phonetics('')


def test_refined_soundex():
    soundex = RefinedSoundex()

    assert soundex.phonetics('h') == 'H'
    assert soundex.phonetics('d') == 'D6'

    with pytest.raises(EmptyStringError):
        soundex.phonetics('')


def test_fuzzy_soundex():
    soundex = FuzzySoundex()

    assert soundex.phonetics('Catharine') == 'K365'
    assert soundex.phonetics('Katharine') == 'K365'

    with pytest.raises(EmptyStringError):
        soundex.phonetics('')
