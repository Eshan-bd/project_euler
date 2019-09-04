# Only works for 5 or 6 digits numbers
def check_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

def find_L_palindrome():
    max = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if check_palindrome(i*j):
                if max < i*j:
                    max = i*j
    print(max)

def main():
    find_L_palindrome()

if __name__ == '__main__':
    main()   
