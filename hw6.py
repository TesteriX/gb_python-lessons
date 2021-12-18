# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена
# составит не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.

nowDistance = int(input("Введите текущий километраж: "))
wantDistance = int(input("Введите желаемую дистанцию: "))

currDay = 1
# шаг один день
stepRangeDay = 1
# stepRangePercent = %
stepRangePercent = 10

while nowDistance < wantDistance:
    currDay += stepRangeDay
    nowDistance = nowDistance + nowDistance / 100 * stepRangePercent
    print(f"День: {currDay} Дистанция {nowDistance}")

print(f"В день номер {currDay} спортсмент достигнет результата не менее {wantDistance} км")
