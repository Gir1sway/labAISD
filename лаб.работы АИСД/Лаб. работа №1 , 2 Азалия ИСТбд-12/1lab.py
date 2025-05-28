DIGITS={'0':'ноль','1':'один','2':'два','3':'три','4':'четыре',
        '5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}

def to_words(n):
    return ' '.join(DIGITS[d] for d in str(n))

def process(fname):
    data=open(fname,encoding='utf-8').read().split()
    nums=[]
    trans=[]
    for x in data:
        if x.isdigit() and x.startswith('77') and int(x)<=999_999:
            nums.append(int(x))
            s=x[2:]
            trans.append(int(s) if s else 0)
    print("Начальные значения:")
    print(*nums)
    print()
    print("Значения после удаления 7:")
    print(*trans)
    print()
    if trans:
        mn,mx=min(trans),max(trans)
        mid=(mn+mx)//2
        print("Минимальное (после удаления 77):",mn)
        print("Максимальное (после удаления 77):",mx)
        print("Среднее между мин. и макс. (прописью):",to_words(mid))

if __name__=='__main__':
    process("1lab.txt")
