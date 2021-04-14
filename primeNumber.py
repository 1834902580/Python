import math

num = int(input('Enter a number: '))


def prime(prime_number):
    for i in range(2, int(math.sqrt(prime_number) + 1)):
        if prime_number % i == 0:
            return False
    return True


for i in range(1, num + 1):
    if prime(i):
        print(i)
