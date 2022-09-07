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
    str_phrase = str(input("Please enter a phrase to be converted into Morse Code:\n"))
    return str_phrase

def upper_phrase():
    return get_phrase().upper()

def split_phrase():
    return [char for char in upper_phrase() if char != ' ']

def get_morse():
    try:
        code = [MORSE_CODE_DICT[i] for i in split_phrase()]
        print(code)
        return code
    except KeyError as e:
        raise KeyError(f"Bad character: {e} -- The phrase can only contain letters, numbers, and the following symbols: ,.?/-() Please try again...")



if __name__ == "__main__":
    get_morse()