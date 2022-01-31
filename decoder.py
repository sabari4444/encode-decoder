a = ''
def decoder():
    word = input('enter the encryped code :')
    dic = {'00000': 'a', '10000': 'b', '01000': 'c', '00100': 'd', '00010': 'e', '00001': 'f', '00011': 'g',
           '00111': 'h', '00101': 'i', '01111': 'j', '01011': 'k', '01001': 'l', '01110': 'm', '01010': 'n',
           '01100': 'o', '11111': 'p', '10111': 'q',
           '11011': 'r', '11101': 's', '11110': 't', '11100': 'u', '10101': 'v', '10011': 'w', '11001': 'x',
           '11000': 'y', '10100': 'z', ' /': ' '}
    b = word
    word = word.split('-')
    length = len(word) - 1
    global a
    for sec in range(0, length):
        print((dic.get(word[sec])), end='')
    a = b

