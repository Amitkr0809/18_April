# WAP to find the ones and zeros in number using bitwise operators in python
num = int(input("enter number : "))

def binary(num):
    return"{0:b}".format(int(num))
z = binary(num)
print(z)





count0 = 0
count1 = 0

for i in z:
    if i == "0":
        count0 = count0+1
    else:
        count1 = count1+1

print("count0 -",count0)
print("count1 -",count1)
