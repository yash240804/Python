#Given a positive real number, print its first digit to the right of the decimal point.
import math
n = float(input())
n = n * 10
n = math.floor(n)
n = n % 10
print(n)