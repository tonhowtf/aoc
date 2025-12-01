with open("UwU.txt") as f:
    lines = [line.strip() for line in f]

dial = 50
count = 0


for i in lines:
    d = i[0]
    v = int(i[1:])
    if d == 'L':
        dial = (dial - v) % 100
    else:
        dial = (dial + v) % 100
    if dial == 0:
        count += 1

print(count)