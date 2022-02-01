import random


def run():
    random_number = random.randint(1, 100)
    chosen_number = int(input('choose a number between 1 and 100: '))
    while random_number != chosen_number:
        if chosen_number < random_number:
            print('find a bigger number')
        else:
            print('find a smaller number')
        chosen_number = int(input('choose a number between 1 and 100: '))
    print('Congratulations you win')


if __name__ == '__main__':
    run()