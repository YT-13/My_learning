# 3.
# Реалізувати додаток, який приймає на вхід значення чисел від 3 до 9;
# Виконує перевірку на правильність введеного числа у вказаному діапазоні.
# Якщо не в діапазоні або не число – повідомляє про проблему та закінчує роботу.
# Інакше - друкує піраміду з чисел. Введене число позначає кількість надрукованих рядів, а перший ряд складається з '1'.


while True:

    number = int(input("Введіть значення від 3 до 9"))

    if number >= 3 and number <= 9:
        for i in range(1,number+1):
            combinatlist = list(range(1,i+1)) + list(reversed(range(1, i)))
            print(combinatlist)
        break
    else:
        continue
