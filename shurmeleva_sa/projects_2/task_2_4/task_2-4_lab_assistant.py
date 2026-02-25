volume = float(input("Введите объем раствора (мл): "))

salt_mass = volume * 0.0009
water_volume = volume

with open("C:/Users/honor/OneDrive/Рабочий стол/Шурмелева_СА/recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    recipe.write("-" * 23 + "\n")
    recipe.write(f"Общий объем:\t{volume}мл\nМасса соли:\t{salt_mass:.2f}г\nОбъем воды:\t{water_volume}мл\n")