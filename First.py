# test_twttr.py

import twttr

def test_shorten():
    assert twttr.shorten("Twitter") == "Twttr"
    assert twttr.shorten("HELLO") == "HLL"
    assert twttr.shorten("CS50") == "CS50"
    assert twttr.shorten("aeiou") == ""
    assert twttr.shorten("BCDFG") == "BCDFG"
    assert twttr.shorten("This is a test.") == "Ths s  tst."
    assert twttr.shorten("") == ""
    
if __name__ == "__main__":
    test_shorten()
    print("All tests passed.")



