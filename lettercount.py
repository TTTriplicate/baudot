hashtable = [0 for i in range(26)]

with open('decoded.txt') as intake:
    for line in intake:
        for char in line:
            if char == ' ' or char == '\n':
                continue
            else:
                print(char)
                hashtable[ord(char.lower()) - ord('a')] += 1

print(hashtable)