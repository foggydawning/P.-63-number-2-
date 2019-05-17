def add_max(list=[]):
    max = input("Введите 'stop' или элемент массива: ")
    if max=="stop":
        print("Вы не ввели ни одного элемента в массив!")
        return("ERROR")
    else:
        max=int(max)
        list.append(max)
        number = input("Введите 'stop' или элемент массива: ")
        while number!="stop":
            number=int(number)
            list.append(int(number))
            if number > max:
                max=number
            number = input("Введите 'stop' или элемент массива: ")
        else:
            print(max)
            return list