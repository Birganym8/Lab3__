def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):

    return [num for num in numbers if is_prime(num)]

numbers = [2, 3, 4, 5, 8, 13, 18, 19, 21]
primes = filter_prime(numbers)
print(f"Prime numbers: {primes}")

