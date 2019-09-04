import sys

def get_triangle_num(n):
    return int(n/2 * (n+1))

def get_divisor_count(n):
    divisor_count = 0
    for i in range(1, int(n**0.5)+1):
        if(n%i == 0):
            divisor_count += 2
    return divisor_count

def main():
    i = 499
    max = -1
    while True:
        i += 1
        num = get_divisor_count(get_triangle_num(i))
        if max < num:
            max = num
            print(max)
        if num > 500:
            print(get_triangle_num(i))
            break

if __name__ == '__main__':
    main()

