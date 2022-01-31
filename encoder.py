null =''
def encoder():
    sentence = input('enter to encrypt : ')
    sentence = sentence.lower()
    dic = {'a': '00000', 'b': '10000', 'c': '01000', 'd': '00100', 'e': '00010', 'f': '00001', 'g': '00011',
           'h': '00111',
           'i': '00101', 'j': '01111', 'k': '01011', 'l': '01001', 'm': '01110', 'n': '01010', 'o': '01100',
           'p': '11111',
           'q': '10111',
           'r': '11011', 's': '11101', 't': '11110', 'u': '11100', 'v': '10101', 'w': '10011', 'x': '11001',
           'y': '11000',
           'z': '10100', ' ': ' /', '.': '0000', '?': '1000', '!': '0001'}
    global null
    for sec in range(0, len(sentence)):
        null = null + dic.get(sentence[sec]) + '-'
    print(str(null))
