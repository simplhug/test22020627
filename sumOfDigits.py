def sumOfDigits(num):
    sum = 0
    for c in list(str(num)):
        sum += int(c)

    return sum

if __name__ == '__main__':
    a = input()
    print(sumOfDigits(a))
