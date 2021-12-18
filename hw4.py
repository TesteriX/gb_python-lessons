# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numb = int(input('Ввдите целое положительное число:'))

answer = numb % 10
numb = numb // 10

while numb > 0:
    bufAnswer = numb % 10
    if bufAnswer > answer:
        answer = bufAnswer
    numb = numb // 10

print(f"Самая большая цифра в вашем числе {answer}")
