def check_prime(n):
    if (n != 2 and n%2 == 0):
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if(n % i == 0):
                return False

    return True

def sum_of_primes(n):
    sum = 0

    for i in range(2, n):
        if check_prime(i):
            sum += i

    return sum

def main():
    print(sum_of_primes(2000000))

if __name__ == '__main__':
    main()
