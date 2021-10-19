from ..MeanFunction import mean

def test_mean_positive():
    assert mean([7, 7, 7]) == 7

def test_mean_negative():
    assert not (mean([7, 7, 9]) == 7)
