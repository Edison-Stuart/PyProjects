from ..StringFormating import greeting

def test_greeting_positive():
    assert greeting("Eddie", "Stuart") == "Hello Eddie Stuart. What's up today"

def test_greeting_negative():
    assert not greeting("Eddie", "Stuart") == "Hello EddieStuart. What's up today"
