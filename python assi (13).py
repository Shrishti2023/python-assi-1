#13.Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime
def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year-birth_year
birth_year = int(input("enter your bith year:"))
print("youe age is:",calculate_age(birth_year))