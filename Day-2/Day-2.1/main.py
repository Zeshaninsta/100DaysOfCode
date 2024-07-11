# logic for Two Digit Number addition
def two_digit_number_add(num):
    if len(num) < 2:
        print("number should have 2 digit")
    elif len(num) > 2:
        print("number should have 2 digit")
    else:
        result = int(num[0]) + int(num[1])
        return result

# main function
def main():
    print("Enter Two Digit Number: ")
    num = input()
    result = two_digit_number_add(num)
    if result:
        print(result)
    

if __name__ == "__main__":
    main()
