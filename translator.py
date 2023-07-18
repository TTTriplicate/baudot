intake = open('baudot.csv')
results = []
for i, line in enumerate(intake):
    results.append('')
    code = line.split(',')
    for field in code:
        if field == '●':
            continue
        elif field == '⬤' or field == '⬤\n':
            results[i] += '1'
        else:
            results[i] += '0'
intake.close()
with open('result.txt', 'w') as output:
    output.write('\n'.join(results))
output.close()