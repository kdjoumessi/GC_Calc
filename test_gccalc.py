from gccalc import calc_gc_content # import *
import pytest

def test_mid_gc():
    """
    if the function works in the way we are expected it to work, we should get 50% with 
    this input
    """
    seq = "GCGCGCGCGCATATATATAT"
    exp = 50.0
    obs = calc_gc_content(seq)
    assert obs == exp 

def test_hight_gc():
    seq = "GCGCGCGCGCGCGCGCGC"
    exp = 100.0
    obs = calc_gc_content(seq)
    assert obs == exp

def test_low_gc():
    seq = "ATATATATATATATATA"
    exp = 0.0
    obs = calc_gc_content(seq)
    assert obs == exp

def test_empty_gc():
    seq = ""
    exp = 0.0
    obs = calc_gc_content(seq)
    assert obs == exp

@pytest.mark.skip(reason="(cleaning not yet implemented)")
def test_invalid_characters():
    seq = "GGGGGCCCCCAAAAATTTTTXXXXX"
    exp   = 50.0
    obs = calc_gc_content(seq)
    assert obs == exp

#test_mid_gc()
#test_hight_gc()
#test_low_gc()
