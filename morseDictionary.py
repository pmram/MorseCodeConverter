MorseDictionary = {
    "A": "·-",
    "B": "-···",
    "C": "-·-·",
    "D": "-··",
    "E": "·",
    "F": "··-·",
    "G": "--·",
    "H": "····",
    "I": "··",
    "J": "·---",
    "K": "-·-",
    "L": "·-··",
    "M": "--",
    "N": "-·",
    "O": "---",
    "P": "·--·",
    "Q": "--·-",
    "R": "·-·",
    "S": "···",
    "T": "-",
    "U": "··-",
    "V": "···-",
    "W": "·--",
    "X": "-··-",
    "Y": "-·--",
    "Z": "--··",
    "·": "·-·-·-",
    ",": "--··--",
    "?": "··--··",
    "/": "-··-·",
    "@": "···-·-",
    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·",
    "0": "-----",
}


def morse_converter(
        text: str,
        separator: str = " ",
        missing_char: str = "$"
) -> str:
    """
    Converts a text string into a Morse Code equivalent string.
    :param missing_char: String to replace the character where no correspondence was found
    :param separator: String to separate each Morse Code character
    :param text: String to be converted
    :return: String converted to Morse Code
    """
    if separator is None:
        separator = " "
    if missing_char is None:
        missing_char = "$"

    morse_array = []
    for char in text:
        upper_char = char.upper()
        try:
            morse_array.append(MorseDictionary[upper_char])
        except KeyError:
            morse_array.append(missing_char)

    morse_string = separator.join(morse_array)
    return morse_string
