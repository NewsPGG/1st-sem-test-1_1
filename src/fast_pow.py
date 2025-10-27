def fastPow(number, power):
    if power == 0:
        return 1
    if power < 0:
        return 1 / fastPow(number, -power)
    else:
        result = number
        while power != 1:
            result *= result
            power = power // 2
        return result
