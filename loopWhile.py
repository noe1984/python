def run():
    LIMIT = 1000000
    counter = 0
    power_2 = 2**counter
    while power_2 < LIMIT:
        print('la potencia de 2 elevado a la ' + str(counter) + ' es igual a ' + str(power_2))
        counter = counter + 1
        power_2 = 2**counter


if __name__ == '__main__':
    run() 