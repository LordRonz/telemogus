from utils.utils import *

def test_sus():
    res = sus_in_string('djpokamesusamegum jajade')
    assert res == True
    res = sus_in_string('ahahaha asu su')
    assert res == False
