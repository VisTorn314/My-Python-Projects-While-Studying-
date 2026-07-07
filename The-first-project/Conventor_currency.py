print("""
█▀▀ █░█ █▀█ █▀█ █▀▀ █▄░█ █▀▀ █▄█   █▀▀ █▀█ █▄░█ █░█ █▀▀ █▀█ ▀█▀ █▀▀ █▀█   █░█ ▄█
█▄▄ █▄█ █▀▄ █▀▄ ██▄ █░▀█ █▄▄ ░█░   █▄▄ █▄█ █░▀█ ▀▄▀ ██▄ █▀▄ ░█░ ██▄ █▀▄   ▀▄▀ ░█""")

while True:
    while True:
        try:
            money = float(input("Введите рубли для конвертации в доллары: "))
            break
        except ValueError:
            print("Это не число (Пример: 2)")

    result = money * 0.0128
    print(f"Рублей: {money} в Долорах: {result}")
    
    chois = input("Продолжить(Y/N)? ")
    
    if chois == 'N':
        print("Программа закрылась")
        break