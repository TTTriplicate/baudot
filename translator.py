intake = open('baudot.csv')
results = []
for i, line in enumerate(intake):
    results.append('')
    code = line.split(',')
    code = [code[0]] + [code[1]] + [code[2]] + [code[5]] + [code[4]] + [code [3]]
    for field in code:
        if field == '●':
            continue
        elif field == '⬤' or field == '⬤\n':
            results[i] += '1'
        else:
            results[i] += '0'
intake.close()

interpreter = {
    '01000': '\n',
    '00010': '',
    '10111': 'q',
    '10011': 'w',
    '00001': 'e',
    '01010': 'r',
    '10000': 't',
    '10101': 'y',
    '00111': 'u',
    '00110': 'i',
    '11000': 'o',
    '10110': 'p',
    '00011': 'a',
    '00101': 's',
    '01001': 'd',
    '01101': 'f',
    '11010': 'g',
    '10100': 'h',
    '01011': 'j',
    '01111': 'k',
    '10010': 'l',
    '10001': 'z',
    '11101': 'x',
    '01110': 'c',
    '11110': 'v',
    '11001': 'b',
    '01100': 'n',
    '11100': 'm',
    '11111': '*',
    '00000': ' ',
    '00100': ' ',
    '11011': '^'
}

with open('current.txt','w') as current:
    current.write(''.join(results))
with open('read.txt', 'w') as writer:
    writer.write(''.join([interpreter[i] for i in results]))

