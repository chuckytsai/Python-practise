# 用於合併list 為tuples
# 會自動判別2個list的多寡
x = [1, 2, 3, 4, 5, 6]
y = ["a", "b", "c"]

for a, b in zip(x, y):
    print(a, b)
