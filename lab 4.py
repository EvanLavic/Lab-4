
f = open("Telnum.txt", "r")

lines = f.read().splitlines()

answer = []
lc = 2
for i in lines:
    if len(i) > 12:
        lc = 3
    answer.append("+1" + i[lc:])

print (answer)