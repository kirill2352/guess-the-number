import random 

def generate_number():
    return random.randint(1, 100)

def get_number():

    while True:

        number = int(input("Введите число (от 1 до 100): "))

        if number >= 1 and number <= 100:
            return number

        print("Нужно число от 1 до 100")

def check_numbers(guess, secret_number):

    if guess > secret_number:
        return "Введите меньше число"

    elif guess < secret_number:
        return "Введите больше число"

    else:
        return "Вы угадали!"

generate = generate_number()

while True:
    guess = get_number()
    check = check_numbers(guess, generate)
    print(check)