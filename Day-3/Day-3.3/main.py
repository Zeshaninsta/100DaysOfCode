# LEAP YEAR
# logic for calculating leap year
def leap_year(year):
    if year % 4 == 0  and year % 100 != 0 or year % 400 == 0:
        return "it's a leap year"
    else:
        return "it's not a leap year"

# main function
def main():
    print("Welcome to Leap Year Calculator")
    year = int(input("please provide A Year: "))
    result = leap_year(year)
    print(result)


if __name__ == "__main__":
    main()
