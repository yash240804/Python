#A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
d = int(input())
c = int(input())
n = int(input())
c = c / 1000
d = d + c
print(d * n)
