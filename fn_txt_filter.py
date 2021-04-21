import re

def rep(line):
    pattern = "-[0-9]{1,2}\/[0-9]{1,2}이후[가-힣]{2,4}"
    replaced = re.sub(pattern, "", line)
    return replaced

l = []
with open('f2.txt') as f:
    for line in f.readlines():
        l.append(rep(line).replace('\n', ''))

with open('./f3.txt', 'w+') as f:
    for item in l:
        f.write(str(item) + '\n')

