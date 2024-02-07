#A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.
a1 = int(input("Enter No. of hours for first timestamp "))
a2 = int(input("Enter No. of min for first timestamp "))
a3 = int(input("Enter No. of secound for first timestamp "))
b1 = int(input("Enter No. of hours for Second timestamp "))
b2 = int(input("Enter No. of min for Second timestamp "))
b3 = int(input("Enter No. of secound for Second timestamp "))
print("Seconds between them", ((b1*60*60) + (b2*60) + b3)- ((a1*60*60) + (a2*60) + a3) )