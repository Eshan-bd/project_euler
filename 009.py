import math

def sq(n):
    return n*n

def pythaX(a, b):
    # Find the unknows pythagoras number from other 2 numbers
    return math.sqrt(sq(a) - sq(b))

def pythagorean_triplet(n):
    # Return a*b*c when a + b + c = n

    for i in range(int(n/2), 0, -1):
        for j in range(int(i/2), 0, -1):
            # Check if i and j are part of a pythagorean triplet
            if ( pythaX(i, j) ) == int( pythaX(i, j) ) and ( pythaX(i, j) + j + i == n ):
                    return pythaX(i, j) * j * i
    raise Exception("{} can't be a sum of pythagorean triplet".format(n))

def main():
    print(pythagorean_triplet(1000))

if __name__ == '__main__':
    main()
