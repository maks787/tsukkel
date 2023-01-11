import random
n=random.randint(1,10)
while True:
    text = input("Введите число или стоп для выхода: ")
    if text == "стоп":
        print("Выход из программы! До встречи! Загадано было", n)
        break # инструкция выхода из цикла
    elif int(text) == n:
        print("Победа")
        break
    else:
        print("Попробуйте еще")



     
