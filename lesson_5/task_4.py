# Програма отримує число N.
# Роздрукувати квадрати цілих чисел починаючи від 0 де кожен квдарат числа не повиннен бути більшими за значення в числі N

n = int(input("Enter your number >>> "))

for i in range(1,n+1):
    if i*i <= n:
        print(i * i)
    else:
        break