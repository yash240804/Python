#A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
d = int(input())
c = int(input())
n = int(input())
d1 = c / 100
print((d + d1) * n)
c1 = d * 100
print((c + c1) * n)
