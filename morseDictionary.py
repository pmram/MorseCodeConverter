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


def morseconverter(string: str) -> str:
    """
    Converts a string into another string in Morse Code
    :return: Text in Morse Code
    :param string: Text to be converted
    """
    morsestring = ""
    morsearray = []
    for char in string:
        upperchar = char.upper()
        try:
            morsearray.append(MorseDictionary[upperchar])
        except KeyError:
            morsearray.append("?")

    morsestring = "".join(morsearray)
    return morsestring

