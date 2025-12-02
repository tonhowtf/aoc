with open("OwO.txt") as f:
    lines = [line.strip() for line in f.read().split(',')]


invalid_codes = []

def format_numbers(code):
    return code.split('-')

def is_invalid(code: str):
    d = int(len(code) / 2)
    if code[d:] == code[:d]:
        invalid_codes.append(code)

def awnser(list: list):
    awnser = 0
    for i in invalid_codes:
        awnser += int(i)
    return awnser



for line in lines:
    s, e = format_numbers(line)
    n1 = int(s)
    n2 = int(e)
    for j in range(n1, n2):
        is_invalid(str(j))


print(format_numbers('2157315-2351307')[0])
print(awnser(invalid_codes))