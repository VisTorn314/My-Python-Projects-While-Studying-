while True:
    try:
        weight = float(input("Введите вес (кг): "))
        growth_cm = float(input("Введите рост (см): "))
        if growth_cm <= 0:
            print("Рост должен быть больше нуля!")
            continue
        break
    except ValueError:
        print("Ошибка! Введите числа.")

    growth_m = growth_cm / 100
    imt = weight / (growth_m ** 2)

    print(f"Ваш индекс массы тела: {imt:.1f}")
    # интерпретация...

    choice = input("Хотите ещё? (Y/N): ").upper()
    if choice == 'N':
        print("До свидания!")
        break