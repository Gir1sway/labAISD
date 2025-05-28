import numpy as np
import matplotlib.pyplot as plt

def load_matrix():
    A = np.loadtxt("matrix_data.txt", dtype=int)
    if A.shape[0] != A.shape[1]:
        exit("Матрица должна быть квадратной")
    return A

def is_diag_symmetric(A):
    # Проверка симметрии относительно главной диагонали
    return np.allclose(A, A.T)

def build_F(A):
    F = A.copy()
    n = A.shape[0] // 2
    E = A[:n, :n]
    B = A[:n, n:]
    D = A[n:, :n]
    C = A[n:, n:]
    symmetric = is_diag_symmetric(A)
    print(f"\nA симметрична относительно главной диагонали? {'Да' if symmetric else 'Нет'}")
    if symmetric:
        print("Меняем C и B симметрично")
        F[n:, n:], F[:n, n:] = np.fliplr(B), np.fliplr(C)
    else:
        print("Меняем C и E несимметрично")
        F[n:, n:], F[:n, :n] = E.copy(), C.copy()
    return F

def compute_result(A, F, K):
    det_A, diag_F = np.linalg.det(A), np.trace(F)
    print(f"\nОпределитель A: {det_A:.2f}\nСумма диагонали F: {diag_F}")
    if np.linalg.det(F) == 0:
        return "ОШИБКА: матрица F необратима"
    if det_A > diag_F:
        print("det(A) > сумма диагонали F: вычисляем A^-1 * A^T - K * F^-1")
        return np.linalg.inv(A) @ A.T - K * np.linalg.inv(F)
    else:
        print("det(A) <= сумма диагонали F: вычисляем (A^T + G - F^T) * K")
        G = np.tril(A)
        return (A.T + G - F.T) * K

def plot_graphs(F):
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    axs[0].imshow(F, cmap='viridis')
    axs[0].set_title("Тепловая карта")
    axs[1].plot(F.sum(axis=1), marker='o')
    axs[1].set_title("Сумма по строкам")
    axs[2].hist(F.flatten(), bins=10, color='skyblue')
    axs[2].set_title("Гистограмма значений")
    for ax in axs: ax.grid(True)
    plt.tight_layout(); plt.show()

def main():
    K = int(input("Введите K: "))
    A = load_matrix()
    print("\nA:\n", A)
    F = build_F(A)
    print("\nF:\n", F)
    R = compute_result(A, F, K)
    print("\nРезультат:\n", R)
    plot_graphs(F)

main()
