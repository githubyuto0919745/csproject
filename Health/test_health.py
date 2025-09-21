from health import (
    
    calculate_bmi,
    read_ideal_weight,
    calculate_RDA,
)
from pytest import approx
import pytest
from datetime import datetime



def test_calculate_bmi():
    assert calculate_bmi(157,68) == approx(23.0, rel=0.1) 
    assert calculate_bmi(146,58) == approx(30.5, rel=0.1) 
    assert calculate_bmi(180,71) == approx(25.0, rel=0.1) 
    assert calculate_bmi(190,75) == approx(23.5, rel=0.1) 

def test_read_ideal_weight():
    assert read_ideal_weight('ideal_weight.csv', 0, 68) == (125, 158)
    assert read_ideal_weight('ideal_weight.csv', 0, 58) == (91, 115)
    assert read_ideal_weight('ideal_weight.csv', 0, 70) == (132,167 )
    assert read_ideal_weight('ideal_weight.csv', 0, 74) == (148, 186)

def test_calculate_RDA():
    assert calculate_RDA(56.0,70.0) == (63)
    assert calculate_RDA(53.0,65.0) == (59.0)

pytest.main(["-v", "--tb=line", "-rN", __file__])    