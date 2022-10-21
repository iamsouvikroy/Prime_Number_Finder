import operator

def main():
    while 10 > 0:
        f = 0
        num = int(input("Enter a number: "))
        for i in range(num+1):
            if i != 0:
                test = num/i
                int_test = int(test)
                if int_test == test:
                    f = operator.add(f, 1)
                else:
                    pass
            else:
                continue
        if f > 2:
            print('No, ' + f'{num}' + ' is not a prime number.')
        else:
            print('Yes, ' + f'{num}' + ' is a prime number.')


if __name__ == '__main__':
    main()
