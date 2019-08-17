def find_smallestMultiple():
    i = 2518
    done = False
    while not done:
        i += 2
        done = True
        for j in range(11, 21):
            if ( i%j != 0 ):
                done = False
                break
    print(i)
        

def main():
    find_smallestMultiple()

main()

