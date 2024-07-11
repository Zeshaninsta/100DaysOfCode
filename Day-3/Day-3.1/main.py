# Logic for defferentiate the Odd Number and Even Number
def odd_or_even(num):
    if num == " ":
        return "Please Provide some numbers!"
    elif num % 2 == 0:
            return "The Number You Have Entered is even"
    elif num % 2 != 0:
        return "The Number You Have Entered is Odd"

# main function
def main():
    try:

        num = int(input("please Enter a number: "))
        result = odd_or_even(num)
        print(result)
    except ValueError:
        print("Invalid input! please Enter a valid Number")


if __name__ == "__main__":
    main()
