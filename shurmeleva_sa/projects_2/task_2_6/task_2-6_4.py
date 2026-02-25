print("Помогите богатырю")

direction = input("Выберите направление: ").strip().lower()

if direction == "прямо":
    print("живым не бывать")

elif direction == "направо" or direction == "вправо":
    print("коня потеряешь")    

elif direction == "налево" or direction == "влево":
    print("богатым будешь")

else:
    print("такого направления нет")   