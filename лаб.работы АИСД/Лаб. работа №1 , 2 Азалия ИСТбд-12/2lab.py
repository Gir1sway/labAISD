import re

DIGITS = {
    '0':'ноль','1':'один','2':'два','3':'три','4':'четыре',
    '5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'
}

def to_words(n):
    return ' '.join(DIGITS[d] for d in str(n))

def process(fname):
    txt = open(fname, encoding='utf-8').read()
    matches = re.findall(r'\b77\d{0,4}\b', txt)
    nums = list(map(int, matches))
    trans = [int(m[2:] or '0') for m in matches]

    print("Начальные значения:")
    print(*nums)
    print()
    print("Значения после удаления 7:")
    print(*trans)
    print()
    if trans:
        mn, mx = min(trans), max(trans)
        mid = (mn + mx) // 2
        print("Минимальное (после удаления 77):", mn)
        print("Максимальное (после удаления 77):", mx)
        print("Среднее между мин. и макс. (прописью):", to_words(mid))

if __name__ == '__main__':
    process("1lab.txt")
