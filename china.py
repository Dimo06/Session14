b = 20
c = [1,2,3]

prime_numbers = [2, 3, 5, 11, 23, 29, 53]
non_prime_numbers = [4, 6, 12, 24, 30, 55]

def is_prime(num):
    """
    check if a number is prime
    :param num: the number to check
    :return: true/false
    """

    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
print("testing for prime function")
print("prime numbers:")
for i in prime_numbers:
    print(f"{i} is prime= {is_prime(i)}")

print("non prime numbers:")
for i in non_prime_numbers:
    print(f"{i} is prime= {is_prime(i)}")
