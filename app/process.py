"""Module to analyse text."""


def num_characters(text):
    """Cuenta caracteres en el texto."""
    return len(text)


def num_words(text):
    """Cuenta palabras en el texto."""
    return len(text.split())


def num_vowels(text):
    """Cuenta el numero de vocales."""
    count = 0
    for c in text:
        if c in "aeiouAEIOU":
            count += 1
    return count


def text_analysis(text):
    """Hace analisis del texto."""
    result = f"Texto: {text}"
    result += "<br>"
    result += f"Texto tiene {num_characters(text)} caracteres"
    result += "<br>"
    result += f"Texto tiene {num_words(text)} palabras"
    result += "<br>"
    result += f"Texto tiene {num_vowels(text)} vocales"
    return result
