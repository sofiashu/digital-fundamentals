f = open("C:/Users/honor/OneDrive/Рабочий стол/Шурмелева_СА/inventory.txt", "w", encoding="utf-8")

reagent_name = input("Введите название реактива: ")
quantity = input("Количество реагента: ")

print(f"Реактив {reagent_name} поступил на склад в количестве {quantity} шт.", file=f)

f.close()