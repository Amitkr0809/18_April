# Check if the number is power of 2 or not

x = int(input("enter number : "))


def isPowerOfTwo(x):
    return (x and (not (x & (x - 1))))


if (isPowerOfTwo(x)):
    print('Yes')
else:
    print('No')
