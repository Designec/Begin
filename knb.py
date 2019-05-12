import random
print('Давайте сыграем в игру "Камень-Ножницы-Бумага"')
print('Введите число 1, 2 или 3, чтобы сделать свой выбор')
print('''
1) Камень
2) Ножницы
3) Бумага''')
allVariants = {1 : 'Камень', 2 : 'Ножницы', 3 : 'Бумага'}
while True:
    try:
        x = input('Ваш выбор: ')
        if x == "exit":
            print("Выходим из игры...")
            break
        ourChoice = int(x)
        choiceGame = random.randint(1, 3)
        if ourChoice == 1:
            if choiceGame == 1:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ', у компьютера ' + str(allVariants[choiceGame]))
                print('Ничья!')
            elif choiceGame == 2:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ', у компьютера ' + str(allVariants[choiceGame]))
                print('Вы победили!')
            else:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ', у компьютера ' + str(allVariants[choiceGame]))
                print('Вы проиграли!')
        elif ourChoice == 2:
            if choiceGame == 1:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ' у компьютера ' + str(allVariants[choiceGame]))
                print('Вы проиграли!')
            elif choiceGame == 2:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ', у компьютера ' + str(allVariants[choiceGame]))
                print('Ничья!')
            else:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ', у компьютера ' + str(allVariants[choiceGame]))
                print('Вы победили!')
        elif ourChoice == 3:
            if choiceGame == 1:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ', у компьютера ' + str(allVariants[choiceGame]))
                print('Вы победили!')
            elif choiceGame == 2:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ', у компьютера ' + str(allVariants[choiceGame]))
                print('Вы проиграли!')
            else:
                print('Вы выбрали ' + str(allVariants[ourChoice]) + ', у компьютера ' + str(allVariants[choiceGame]))
                print('Ничья!')
        else:
            print('Необходимо ввести только: 1, 2, 3')
    except ValueError:
        print('Необходимо ввести число 1, 2, 3 или exit для выхода из игры')
