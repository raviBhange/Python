#Q3. Write a program to find out whether a year is Leap Year or not.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Get user input
year = int(input("Enter a year: "))

# Check if the year is a leap year or not
if is_leap_year(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
