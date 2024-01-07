"""Module to analyse text."""


def num_characters(text):
    """Cuenta caracteres en el texto."""
    return len(text)


def num_words(text):
    """Cuenta palabras en el texto."""
    return len(text.split())


def text_analysis(text):
    """Hace analisis del texto."""
    result = f"Texto tiene {num_characters(text)} caracteres"
    result += "<br>"
    result += f"Texto tiene {num_words(text)} palabras"
    return result
