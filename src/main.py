MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def get_phrase():
    str_phrase = str(input("Please enter a phrase to be converted into Morse Code:\nAcceptable Characters are letters, numbers, and symbols: ,.?/-()"))
    return str_phrase

def upper_phrase():
    return get_phrase().upper()

def split_phrase():
    return [char for char in upper_phrase() if char != ' ']

def get_morse():
    return [MORSE_CODE_DICT[i]for i in split_phrase()]

if __name__ == "__main__":
    get_morse()