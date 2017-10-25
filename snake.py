CESAR_DICTIONARY = {v: k for k, v in {'s': 'L', 'b': 's', 'w': 'O', 'z': 'G', 'c': 'o', 'J': 'y',
                                      'V': 't', 'P': 'w', 'B': 'f', 'Z': 'q', 'F': 'k', 'O': 'N',
                                      'u': 'A', 'W': 'r', 'K': 'K', 'a': 'D', 'v': 'l', 'g': 'S',
                                      'f': 'x', 'x': 'c', 'N': 'e', 'p': 'b', 'U': 'a', 'j': 'P',
                                      'o': 'Q', 'i': 'I', 'M': 'd', 't': 'U', 'H': 'V', 'X': 'i',
                                      'Y': 'T', 'R': 'H', 'h': 'X', 'L': 'z', 'G': 'F', 'A': 'W',
                                      'm': 'n', 'T': 'u', 'l': 'B', 'C': 'Z', 'q': 'p', 'D': 'v',
                                      'I': 'g', 'n': 'h', 'y': 'C', 'S': 'j', 'k': 'M', 'd': 'J',
                                      'Q': 'E', 'e': 'Y', 'r': 'R', 'E': 'm'}.items()}


def get_decoded(char):
    if char in CESAR_DICTIONARY:
        return CESAR_DICTIONARY[char]
    return char


def main():
    with open('snake.txt', 'r') as txt_f:

        data = txt_f.read()

        data = " ".join([word[::-1] for word in "".join([' ' if char.isdigit() else get_decoded(char)
                                                         for char in data]).split(' ')])

        print(data)


if __name__ == '__main__':
    main()
