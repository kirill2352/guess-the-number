import random

secret = random.randint(1, 100)

while True:

    number = int(input("Введите число (от 1 до 100): "))

    if number > secret:
        print("Меньше")

    elif number < secret:
        print("Больше")

    else:
        print("Вы угадали!")
        break