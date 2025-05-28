import timeit
from itertools import permutations

def algorithmic_method(books):
    def helper(lst, path, used, res):
        if len(path) == len(lst):
            res.append(path[:])
            return
        for i in range(len(lst)):
            if not used[i]:
                used[i] = True
                path.append(lst[i])
                helper(lst, path, used, res)
                path.pop()
                used[i] = False
    result = []
    helper(books, [], [False] * len(books), result)
    return result

def python_method(books):
    return list(permutations(books))

def optimized_method(books, genres):
    # Только варианты, где не бывает подряд двух книг одного жанра
    n = len(books)
    all_perm = permutations(range(n))
    valid = []
    for p in all_perm:
        ok = True
        for i in range(1, n):
            if genres[p[i]] == genres[p[i-1]]:
                ok = False
                break
        if ok:
            # Формируем красивый вывод: Книга1 (роман), Книга2 (фэнтези), ...
            valid.append(tuple(f"{books[j]} ({genres[j]})" for j in p))
    return valid

if __name__ == '__main__':
    K = 6
    books = ["Книга" + str(i+1) for i in range(K)]
    genres = ["роман", "фэнтези", "детектив", "роман", "фэнтези", "детектив"]

    print(f"Список книг: {books}")
    print(f"Жанры:      {genres}\n")

    alg = algorithmic_method(books)
    print("Алгоритмический способ — первые 5 вариантов:")
    for arr in alg[:5]:
        print(arr)
    print(f"Всего вариантов: {len(alg)}\n")

    py = python_method(books)
    print("Python-метод — первые 5 вариантов:")
    for arr in py[:5]:
        print(arr)
    print(f"Всего вариантов: {len(py)}\n")

    t_alg = timeit.timeit(lambda: algorithmic_method(books), number=2)
    t_py  = timeit.timeit(lambda: python_method(books), number=2)
    print(f"Скорость (2 повтора): algorithmic = {t_alg:.4f}s, python = {t_py:.4f}s\n")

    # Варианты без двух подряд одинаковых жанров — с подписями жанров
    optimal = optimized_method(books, genres)
    print("Варианты без двух подряд одинаковых жанров (первые 5):")
    for arr in optimal[:5]:
        print(arr)
    print(f"Количество таких вариантов: {len(optimal)}\n")

    if optimal:
        print("Пример оптимального варианта:", optimal[0])
