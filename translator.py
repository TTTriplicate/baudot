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
with open('result_correct_offset_binary.txt', 'w') as output:
    output.write('\n'.join(results))
output.close()