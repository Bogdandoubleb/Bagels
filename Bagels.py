import random

NUM_DIGITS = 3
MAX_DIGITS = 10


def main():
    print('''Бейглз - логическая игра, правила следующие:
Вам необходимо угадать загаданное число.'''.format(NUM_DIGITS))

    while True: # Основной цикл игры
        # Переменная, в которой хранится загаданное число:
        secretNum = getSecretNum()
        print("Я загадал число! Попробуй его отгадать!")
        print("У тебя {} попыток.".format(MAX_GUESSES))

        numGuesses = 1
        while num_Guesses <= MAX_GUESSES:
            guess = " "
            # Продолжаем итерацию до получения правильной догадки.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Попытка №{}: ".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numCluesses += 1

            if guess == secretNum:
                break # Игра окончена, выходим из цикла.
            if numGuesses > MAX_GUESSES:
                print("У тебя закончились попытки, попробуй в другой раз:)")
                print("Ответ был:{}.".format(secretNum))

        # Спрашиваем жертву, хочет ли он сыграть снова?
        print("Хочешь сыграть снова? Напиши \"Да\" или \"Нет\"")
        if not input('> ').lower().startswith('Да'):
            break
    print("Спасибо за игру, но мог бы попытаться снова...")


def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789') # Создаёт список цифр от 0 до 9
    random.shuffle(numbers) # Перетасовывает цифры случайным образом.

    # Берём первые NUM_DIGITS цифр из списка для нашего секретного числа:
    secretNum = ' '
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getCluess(guess, secretNum):
    """Возварщает строку с подказками:"""
    if guess == secretNum:
        print("Молодчина! Сыграй ещё!")


    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Правильная цифра на неправильном месте.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

        
if __name__ == '__main__':
    main()