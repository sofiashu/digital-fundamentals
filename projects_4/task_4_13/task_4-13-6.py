N = int(input("Введите число N: "))

sum = 0

for i in range(1, N+1):
    sum = sum + i*i

print("Сумма квадратов первых N натуральных чисел:", sum)