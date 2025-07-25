#Ask user to enter a year
year = int(input("Enter a year: "))

#Check if it is a leap year
if (year % 4 == 0):
 print("Year is a leap year")

else:
 print("Year is not a leap year")