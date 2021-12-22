# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и
# словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
# (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
# (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# "название": ["компьютер", "принтер", "сканер"],
# "цена": [20000, 6000, 2000],
# "количество": [5, 2, 7],
# "ед": ["шт."]
# }

# запросить ключи
# запросить значения

dataKeysBuf = input("Введите доступные параметры товаров через пробел: ")
dataKeys = dataKeysBuf.split(" ")
countGoods = 0
goods = []
while True:
    print("Добавить товар? Введите цифру 1 чтобы добавить товар")
    print("или цифру 2 чтобы закончить и увидеть анализ")
    isWrite = int(input("Ввод: "))
    if isWrite == 2:
        break
    elif isWrite != 1:
        print("Ошибка ввода")
        break
    else:
        idGoods = ''
        attrGoods = {}
        countGoods += 1
        idGoods = int(input("Введите номер товара: "))
        for attr in dataKeys:
            attrGoods[attr] = input(f"Введите значение параметра {attr}: ")
        goods.append(tuple([idGoods, attrGoods]))

if countGoods > 0:
    analysis = {}
    for analysisKeys in dataKeys:
        analysis.update({analysisKeys: []})

    for elementTuple in goods:
        for elementDict in elementTuple:
            iKey = 0
            if type(elementDict) != int:
                while iKey < len(dataKeys):
                    if elementDict.get(dataKeys[iKey]) != '':
                        analysis[dataKeys[iKey]].append(elementDict.get(dataKeys[iKey]))
                    iKey += 1

            #print(analysis)
                #analysis[dataKeys[iKey]] = list(set(analysis[dataKeys[iKey]]))

    print(analysis)
else:
    print("Вы не добавили товары")
    print("Выполнение программы остановлено")