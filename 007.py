
def findPrime(n):

    i = 1
    j = 3
    primeNums = [2]
    while i<n:
        prime = True
        for k in primeNums:
            if ( j%k == 0 ):
                prime = False
        if prime == True:
            i += 1
            primeNums.append(j)
        j += 2
    print(primeNums[n])

def main():
    findPrime(10001)

if __name__ == '__main__':
    main()
