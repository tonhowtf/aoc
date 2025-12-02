with open("OwO.txt") as f:
    lines = [line.strip() for line in f.read().split(',')]


invalid_codes = []

def format_numbers(code: str):
    return code.split('-')
    

def is_invalid(code: str):
    n = len(code)
    for r in range(1, n):
        if n % r == 0:
            p = code[:r]
            if p * (n // r) == code:
                invalid_codes.append(code)
                return

def awnser(codes):
    awnser = 0
    for i in codes:
        awnser += int(i)
    return awnser

for line in lines:
    s, e = format_numbers(line)
    n1 = int(s)
    n2 = int(e)
    for j in range(n1, n2 + 1):
        is_invalid(str(j))


print(awnser(invalid_codes))