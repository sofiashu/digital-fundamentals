operator_name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")

with open("C:/Users/honor/OneDrive/Рабочий стол/Шурмелева_СА/sensor_log.txt", "w", encoding="utf-8") as sensor:
    sensor.write(f"ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    sensor.write(f"{operator_name}\t{pressure}\n")

print(f"\nДанные успешно сохранены в sensor_log.txt")