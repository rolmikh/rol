while True:
    print("Введите количество переменных:")
    number1 = int(input())
    print("Введите номер операции:")
    print(" ")
    print("1 - Сложение")
    print("2 - Умножение")
    print("3 - Вычитание")
    print("4 - Деление")
    print(" ")
    operation = int(input())
    count = 0
    if operation == 1:
        while(int(number1) > int(count)):
            print("Введите число: ")
            number = int(input())
            if (count == 0):
                plus =  number
                count = count + 1 
            else:
                plus = plus +  number
                count = count + 1 
        print("Результат: ", int(plus)) 
    elif operation == 2:
        while(int(number1) > int(count)):
            print("Введите число: ")
            number = int(input())
            if (count == 0):
                umn = number
                count = count + 1 
            else:
                umn = umn * number
                count = count + 1      
        print("Результат: ", int(umn))
    elif operation == 3:
        while(int(number1) > int(count)):
            print("Введите число: ")
            number = int(input())
            if (count == 0):
                minus = number
                count = count + 1 
            else:
                minus = minus - number
                count = count + 1           
        print("Результат: ", int(minus))
    elif operation == 4:
        while(int(number1) > int(count)):
            print("Введите число: ")
            number = int(input())
            if number != 0:
                if (count == 0):
                    delenie = number
                    count = count + 1 
                else:
                    delenie = delenie / number
                    count = count + 1 
            else:
               print("Ошибка! Попробуйте еще раз!")
        print("Результат: ", int(delenie))
    else:
        print("Ошибка! Попробуйте еще раз!")

   
