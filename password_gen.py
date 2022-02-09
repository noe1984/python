import random

def password_gen():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    symbol = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    numbers = ['1','2','3','4','5','6','7','8','9','10']

    chars = upper + lower + symbol + numbers

    password = []

    for i in range(15):
        random_char = random.choice(chars)
        password.append(random_char)

    password = ''.join(password)
    return password

def run():
    password = password_gen()
    print('this is your new password: ' + password)


if __name__ == '__main__':
    run()