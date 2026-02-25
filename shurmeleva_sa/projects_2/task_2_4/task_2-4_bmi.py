weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

bmi = float(weight / ((height/100 )** 2))

print("Отчет о состоянии здоровья")
print(f"Рост:\t{height}см\nВес:\t{weight}кг" )
print(f"Ваш ИМТ: {bmi:.2f}")