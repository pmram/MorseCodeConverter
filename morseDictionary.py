MorseDictionary = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    ".": "._._._",
    ",": "__..__",
    "?": "..__..",
    "/": "_.._.",
    "@": "..._._",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
}


def morse_converter(
        text: str,
        separator: str = "",
        missing_char: str = "$"
) -> str:
    """
    Converts a text string into a Morse Code equivalent string.
    :param missing_char: String to replace the character where no correspondence was found
    :param separator: String to separate each Morse Code character
    :param text: String to be converted
    :return: String converted to Morse Code
    """
    morse_array = []
    for char in text:
        upper_char = char.upper()
        try:
            morse_array.append(MorseDictionary[upper_char])
        except KeyError:
            morse_array.append(missing_char)

    morse_string = separator.join(morse_array)
    return morse_string
