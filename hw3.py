# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

numb = input("Введите число: ")
a = int(numb)
b = int(numb+numb)
c = int(numb+numb+numb)

result = a+b+c

print(result)

a2 = int(f"{numb}")
b2 = int(f"{numb}{numb}")
c2 = int(f"{numb}{numb}{numb}")

result2 = a2+b2+c2

print(result2)

