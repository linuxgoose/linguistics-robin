import pytest
from linguistics_robin import Soundex, RefinedSoundex, FuzzySoundex
from linguistics_robin.exceptions import EmptyStringError


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
