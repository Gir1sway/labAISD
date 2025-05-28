def read_matrix(filename):
    return [list(map(int, line.split())) for line in open(filename)]

def print_matrix(m, name):
    print(f"\n{name}:")
    for row in m:
        print(" ".join(f"{x:4}" for x in row))

def transpose(m):
    return [list(row) for row in zip(*m)]

def get_diagonal_regions(n):
    a1, a2, a3, a4 = [], [], [], []
    for i in range(n):
        for j in range(n):
            if i < j and i + j < n - 1: a1.append((i, j))
            elif i < j and i + j > n - 1: a2.append((i, j))
            elif i > j and i + j > n - 1: a3.append((i, j))
            elif i > j and i + j < n - 1: a4.append((i, j))
    return a1, a2, a3, a4

def is_region1_symmetric(A, a1):
    n = len(A)
    mid = n // 2
    # Симметрия относительно вертикали: A[i][j] == A[i][n-1-j] для всех (i, j) в области 1
    for (i, j) in a1:
        mirror_j = n - 1 - j
        if (i, mirror_j) in a1 and A[i][j] != A[i][mirror_j]:
            return False
    return True

def build_F(A):
    n = len(A)
    F = [row[:] for row in A]
    a1, a2, a3, a4 = get_diagonal_regions(n)
    symmetric = is_region1_symmetric(A, a1)
    print(f"\nСимметрична ли область 1 относительно медианы? {'Да' if symmetric else 'Нет'}")
    if symmetric:
        print("Меняем симметрично области 2 и 4")
        for (i2, j2), (i4, j4) in zip(a2, a4):
            F[i2][j2], F[i4][j4] = F[i4][j4], F[i2][j2]
    else:
        print("Меняем несимметрично области 1 и 2")
        for (i1, j1), (i2, j2) in zip(a1, a2):
            F[i1][j1], F[i2][j2] = F[i2][j2], F[i1][j1]
    return F, symmetric

def add_matrices(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def scalar_mult_matrix(K, M):
    n = len(M)
    return [[K * M[i][j] for j in range(n)] for i in range(n)]

def multiply_matrices(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def subtract_matrices(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def compute_result(A, F, K):
    n = len(A)
    AT = transpose(A)
    AA = multiply_matrices(A, A)
    AT_plus_F = add_matrices(AT, F)
    K_AT_plus_F = scalar_mult_matrix(K, AT_plus_F)
    result = subtract_matrices(AA, K_AT_plus_F)
    return AA, AT, AT_plus_F, K_AT_plus_F, result

def main():
    K = int(input("Введите K: "))
    A = read_matrix("matrix.txt")
    print_matrix(A, "Исходная матрица A")
    F, symmetric = build_F(A)
    print_matrix(F, "Матрица F после преобразования")

    AA, AT, AT_plus_F, K_AT_plus_F, result = compute_result(A, F, K)

    print_matrix(result, "Результат A*A - K*(A^T + F)")

main()
