# 2. Write a Python program for following conditions.
# • If n is single digit print square of it.
# • If n is two digit print square root of it.
# • If n is three digit print cube root of it.
n = int(input("Enter the no. "))
count = 0
temp = n
while(n > 0):
    n = n // 10
    count = count + 1
if(count == 1):
    print(temp ** 2)
if(count == 2):
    print(temp ** 0.5)
if(count == 3):
    print(temp ** 1/3)