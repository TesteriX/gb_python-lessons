# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

allCnt = int(input("Введите количество элементов: "))
i = 0
myList = []

while i < allCnt:
    varToAppend = input(f"Введите значение №{i + 1}: ")
    myList.append(varToAppend)
    i += 1

popLastEl = False if (allCnt % 2) == 0 else True

if popLastEl:
     lastElem = myList.pop(-1)

myList[::2], myList[1::2] = myList[1::2], myList[::2]

if popLastEl:
    myList.append(lastElem)

print(myList)
