i = 0
j = 0
k = 1
sum = 0

# 4 million
while i < 4000000:
    i = j + k
    j = k
    k = i

    if (i % 2 == 0):
        sum += i

print(sum)
