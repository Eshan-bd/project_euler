collatz_lengths = {
        
}

def collatz_chain(n, i = 0):
    x = collatz_lengths.get(str(int(n)))
    if x != None:
        return i+x
    if (n%2 == 0):
        return collatz_chain(n/2, i+1)
    if (n == 1):
        return i+1
    return collatz_chain(3*n+1, i+1)

def main():

    max = -1
    for i in range(1, 1000000):
        x = collatz_chain(i)
        if max < x:
            max = x
            max_i = i
        collatz_lengths[str(i)] = x

    print(max_i)
    


if __name__ == '__main__':
    main()
