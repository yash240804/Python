"""N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
The program reads the numbers N and K.It should print the two answers for the questions above."""
n = int(input("Enter number of students "))
k = int(input("Enter number of apples in baskets "))
print("Number of apples reamining in baskets", k % n)
print("Number of apples divided evenly among students", k // n)
