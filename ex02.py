def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def print_first_10_primes():
    count = 0
    number = 2
    while count < 10:
        if is_prime(number):
            print(number, end=" ")
            count += 1
        number += 1


if __name__ == "__main__":
    print_first_10_primes()
