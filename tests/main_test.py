
from src.main import get_phrase, upper_phrase, split_phrase, get_morse



def test_get_phrase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "This is the test phrase")
    assert get_phrase() == "This is the test phrase"

def test_get_phrase_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1234)
    assert get_phrase() == "1234"

def test_upper_phrase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "This is the test phrase")
    assert upper_phrase() == "THIS IS THE TEST PHRASE"

def test_split_phrase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Test one 2")
    assert split_phrase() == ['T', 'E', 'S', 'T', 'O', 'N', 'E', '2']

def test_get_morse(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "sos")
    assert get_morse() == ["...", "---", "..."]
