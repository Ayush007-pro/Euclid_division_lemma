while True:
    input1 = int(input('Enter the first value: '))
    input2 = int(input('Enter the second value: '))

    if input1 > input2:
        a = input1
        b = input2
    else:
        b = input1
        a = input2

    dividend = a 
    divisor = b

    string_dividend = str(dividend)
    string_divisor = str(divisor)

    r = 1

    while (r != 0):

        r = dividend % divisor

        dividend = divisor
        divisor = r

    result_HCF = dividend

    string_HCF = str(result_HCF)

    print('\nHCF of', string_dividend, '&', string_divisor, 'is', string_HCF,'\n')