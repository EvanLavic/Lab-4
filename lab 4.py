
f = open("Telnum.txt", "r")

lines = f.read().splitlines()
f.close()
answer = []
lc = 2
for i in lines:
    if len(i) > 12:
        lc = len(i) - 10
    answer.append("+1" + i[lc:])

fw = open ("Answer.txt", "w")
fw.write(str (answer))
fw.close()