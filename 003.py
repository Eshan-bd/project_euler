
def L_primeFactor(n):
    i = 2
    while i*i < n:
        if ( n % i == 0 ):
            n /= i
        i+=1
    print(n)

def main():
    L_primeFactor(600851475143)

if __name__ == '__main__':
    main()
