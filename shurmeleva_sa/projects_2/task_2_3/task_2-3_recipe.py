name_medium = input("Введите название питательной среды: ").upper()
concentration = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации (°C): ")

with open("C:/Users/honor/OneDrive/Рабочий стол/Шурмелева_СА/recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"{name_medium}\n\n")
    recipe.write(f"{concentration}\n")
    recipe.write(f"{temperature}\n")

print(f"\nФайл 'recipe.txt' успешно сформирован!")