import tkinter as tk
from tkinter import scrolledtext, messagebox
from itertools import permutations

def find_valid_orders():
    try:
        genres_input = genres_entry.get().strip()
        if not genres_input:
            messagebox.showerror("Ошибка", "Введите жанры книг через запятую!")
            return

        genres = [x.strip() for x in genres_input.split(',')]
        n = len(genres)
        books = [f"Книга{i+1}" for i in range(n)]

        # Перебор с условием: не бывает подряд двух книг одного жанра
        all_perm = permutations(range(n))
        valid = []
        for p in all_perm:
            ok = True
            for i in range(1, n):
                if genres[p[i]] == genres[p[i-1]]:
                    ok = False
                    break
            if ok:
                valid.append(tuple(f"{books[j]} ({genres[j]})" for j in p))

        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Всего корректных вариантов: {len(valid)}\n\n")
        for arr in valid[:50]:  # Показываем до 50 вариантов, остальное можно добавить по желанию
            result_text.insert(tk.END, ", ".join(arr) + "\n")
        if len(valid) == 0:
            result_text.insert(tk.END, "Нет ни одного корректного варианта.\n")
        result_text.config(state='disabled')

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Интерфейс
root = tk.Tk()
root.title("Перестановки книг без одинаковых жанров подряд")

tk.Label(root, text="Жанры книг (через запятую):").pack(pady=5)
genres_entry = tk.Entry(root, width=60)
genres_entry.pack(pady=5)
genres_entry.insert(0, "роман, фэнтези, роман, детектив, фэнтези, детектив")

tk.Button(root, text="Найти варианты", command=find_valid_orders).pack(pady=10)

tk.Label(root, text="Варианты (первые 50):").pack()
result_text = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled')
result_text.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()
