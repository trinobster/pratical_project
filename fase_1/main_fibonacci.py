def fibonacci(n):
    if(n <= 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)

def count_digits(number):
    return len(str(number))

def fibonacci_loop(n):
    if(n <= 2):
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c

def main():
    number = 1
    result = fibonacci_loop(number)
    # result = fibonacci(number)

    while(count_digits(result) != 1000):
        number = number + 1
        result = fibonacci_loop(number)

    print (count_digits(result))
    print ("Il numero cercato è = " + str(number))

if __name__== "__main__":
    main()
