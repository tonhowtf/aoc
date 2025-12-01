with open("UwU.txt") as f:
    lines = [line.strip() for line in f]

dial = 50
count = 0

for i in lines:
    d = i[0]
    v = int(i[1:])
    for _ in range(v):
        if d == 'L':
            dial = (dial - 1) % 100
        else:
            dial = (dial + 1) % 100
        if dial == 0:
            count += 1
        

print(count)