import string

def remove_punctuation(text):
    result = ""

    for char in text:
        if char not in string.punctuation:
            result += char

    return result
