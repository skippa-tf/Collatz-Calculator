def collatz(number):
    global n
    if number %2 == 0:
        n = number // 2
        print('Step #' + str(x + 1) + ' ' + str(n))
    else:
        n = 3 * number + 1
        print('Step #' + str(x + 1) + ' ' + str(n))

while True:
    try:
        n = int(input('Enter an integer: '))
    except ValueError:
        print('Please enter an integer.')
    else:
        break

x = 0

while n != 1:
    collatz(n)
    x += 1
