# 1. Вывести на экран парные числа от 2 до 50

for i in range(2, 51, 2):  # 25 итераций цикла
    print(i)

for i in range(2, 51):  # 49 итераций цикла
    if i % 2 == 0:
        print(i)

# 2. Вывести числа кратные 3, но не кратные 5 от 1 до 50

for i in range(3, 51):  # 48 итераций цикла
    if i % 3 == 0 and i % 5 != 0:
        print(i)

for i in range(3, 51, 3):  # 16 итераций цикла
    if i % 5 != 0:
        print(i)

# 3. Вывести числа от 1 до 25 в 3 степени

for i in range(1, 26):
    print(i ** 3)