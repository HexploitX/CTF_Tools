dot = '25'
dash = '41'
space = '20'

alph = {
    dot + dash: 'A',
    dash + dot + dot + dot: 'B',
    dash + dot + dash + dot: 'C',
    dash + dot + dot: 'D',
    dot: 'E',
    dot + dot + dash + dot: 'F',
    dash + dash + dot: 'G',
    dot + dot + dot + dot: 'H',
    dot + dot: 'I',
    dot + dash + dash + dash: 'J',
    dash + dot + dash: 'K',
    dot + dash + dot + dot: 'L',
    dash + dash: 'M',
    dash + dot: 'N',
    dash + dash + dash: 'O',
    dot + dash + dash + dot: 'P',
    dash + dash + dot + dash: 'Q',
    dot + dash + dot: 'R',
    dot + dot + dot: 'S',
    dash: 'T',
    dot + dot + dash: 'U',
    dot + dot + dot + dash: 'V',
    dot + dash + dash: 'W',
    dash + dot + dot + dash: 'X',
    dash + dot + dash + dash: 'Y',
    dash + dash + dot + dot: 'Z',
    dot + dash + dash + dash + dash: '1',
    dot + dot + dash + dash + dash: '2',
    dot + dot + dot + dash + dash: '3',
    dot + dot + dot + dot + dash: '4',
    dot + dot + dot + dot + dot: '5',
    dot + dot + dot + dot + dash: '6',
    dash + dash + dot + dot + dot: '7',
    dash + dash + dash + dot + dot: '8',
    dash + dash + dash + dash + dot: '9',
    dash + dash + dash + dash + dash: '0'
}


def decode_morse(hex_str):
    hex_str = hex_str.replace(" ", "")
    hex_bytes = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
    words = []
    current_word = []

    for byte in hex_bytes:
        if byte == space:
            if current_word:
                words.append("".join(current_word))
                current_word = []
        else:
            current_word.append(byte)

    if current_word:
        words.append("".join(current_word))

    print(words)

    decoded_text = "".join((alph.get(word, '?') for word in words))

    return decoded_text


hex_str = input('Enter hex bytes: ').strip()
decoded = decode_morse(hex_str)
print(decoded)
