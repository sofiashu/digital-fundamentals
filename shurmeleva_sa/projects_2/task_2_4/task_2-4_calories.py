proteins = int(input("Введите массу белков (г): "))
fats = int(input("Введите массу жиров (г): "))
carbs = int(input("Введите массу углеводов (г): "))

calories = int((proteins*4)+(fats*9)+(carbs*4))

print(f"{calories} ккал")