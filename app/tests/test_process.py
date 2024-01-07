"""Pruebas del archivo process."""
import pytest

from app.process import num_characters, num_words, text_analysis


@pytest.mark.parametrize(
    "text,expected",
    [
        ("texto", 5),
        ("", 0),
        ("texto con varias palabras", 26),
    ],
)
def test_num_characters(text, expected):
    """Pruebas de la funcion num_characters."""
    assert num_characters(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("texto de ejemplo", 3),
        ("", 0),
        ("texto mas largo con mas palabras", 6),
        ("aeiou", 1),
        ("a e i o u", 5),
    ],
)
def test_num_words(text, expected):
    """Pruebas de la funcion num_words."""
    assert num_words(text) == expected


def test_text_analysis():
    """Pruebas de la funcion text_analysis."""
    assert text_analysis("Texto de ejemplo") == (
        "Texto tiene 16 caracteres"
        "<br>"
        "Texto tiene 3 palabras"
    )
