import timeit
import pandas as pd
import matplotlib.pyplot as plt

# Рекурсивные функции
def rec_F(n):
    if n == 1:
        return 1
    return (-1 if n % 2 else 1) * (rec_F(n-1) - 2 * rec_G(n-1))

def rec_G(n):
    if n == 1:
        return 1
    # Вызываем rec_F(n-1), rec_G(n-1) для вычисления G
    return rec_F(n-1) / factorial(2*n) + 2 * rec_G(n-1)

def factorial(k):
    # Итеративный факториал (для рекурсии тоже!)
    res = 1
    for i in range(2, k+1):
        res *= i
    return res

# Итеративные функции
def iter_F(n):
    F = [0] * (n+2)
    G = [0] * (n+2)
    F[1] = 1
    G[1] = 1
    fact = 1
    for k in range(2, n+1):
        fact = fact * (2*k-1) * (2*k)   # факториал (2n)! накапливаем
        F[k] = (-1 if k % 2 else 1) * (F[k-1] - 2 * G[k-1])
        G[k] = F[k-1] / fact + 2 * G[k-1]
    return F[n]

def iter_G(n):
    F = [0] * (n+2)
    G = [0] * (n+2)
    F[1] = 1
    G[1] = 1
    fact = 1
    for k in range(2, n+1):
        fact = fact * (2*k-1) * (2*k)
        F[k] = (-1 if k % 2 else 1) * (F[k-1] - 2 * G[k-1])
        G[k] = F[k-1] / fact + 2 * G[k-1]
    return G[n]

if __name__ == '__main__':
    ns = list(range(1, 13))  # чтобы не было слишком больших факториалов
    results = []

    for n in ns:
        t_rec = timeit.timeit(lambda: rec_F(n), number=5)
        t_it = timeit.timeit(lambda: iter_F(n), number=5)
        results.append((n, rec_F(n), iter_F(n), t_rec, t_it))

    # Таблица
    df = pd.DataFrame(results, columns=['n', 'Rec_F(n)', 'Iter_F(n)', 'Rec_time', 'Iter_time'])
    print(df.to_string(index=False))

    # График
    plt.figure(figsize=(8, 5))
    plt.plot(df['n'], df['Rec_time'], 'o--', label='Recursion')
    plt.plot(df['n'], df['Iter_time'], 'o-', label='Iteration')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Сравнение времени: рекурсия vs итерация для F(n)')
    plt.legend()
    plt.grid(True)
    plt.show()
