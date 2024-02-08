#Given a three-digit number. Find the sum of its digits.
n = int(input("Enter no. "))
a = n % 10
n = n // 10
b = n % 10
n = n // 10
c = n % 10
print(a + b + c)