from predictor import Predictor

def test_predict_age():
    assert 3 <= Predictor.predict_age(3,5) <= 5
    assert 0 <= Predictor.predict_age(0,7) <= 7
    assert -15.0 <= Predictor.predict_age(-15.0,5.0) <= 5.0
    assert Predictor.predict_age(1,1) == 1
    #assert Predictor.predict_age("a", 35)