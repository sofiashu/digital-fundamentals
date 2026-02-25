quntity = int(input("Введите общее количество произведенных капсул: "))
capacity = int(input("Введите количество капсул в одной упаковке: "))

packs = quntity // capacity
surplus = quntity % capacity

print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{packs}\nОстаток капсул:\t\t{surplus}")