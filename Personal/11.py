#Given an integer. Print its tens digit.
n = int(input("Enter the integer "))
n = n // 10
print("The tens digit of integer is", (n%10))