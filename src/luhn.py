def luhnСheck(cardNumber):
    digits = [int(d) for d in str(cardNumber) if d.isdigit()]
    control = digits.pop()
    parity = (len(digits)) % 2
    total = 0
    for i in range(len(digits)):
        if i % 2 == parity:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled = int(str(doubled)[0]) + int(str(doubled)[1])
                total += doubled
            total += doubled
        else:
            total += digits[i]
    return (total + control) % 10 == 0

flag = 1
while flag:
    test = input("Введите номер карты в формате XXXX XXXX XXXX XXXX или -1 для прекращения ввода: ")
    if test == "-1":
        flag = 0
        break
    else:
        if len(test) == 19 and len([i for i in test if i.isdigit()]) == 16:
            if luhnСheck(test):
                print("Correct")
            else:
                print("Incorrect")

        else:
            print("Номер карты введен в неверном формате!")
