def fibonacci():

    a = 1
    b = 1
    n = int(input('Enter number of digits: '))


    while len(str(b)) < n:
        a, b = b, a + b
    return b

print(fibonacci())


    



