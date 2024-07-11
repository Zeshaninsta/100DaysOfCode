# Logic for BMI Calculation
def BMI_Calculation(weight,height):
    BMI = weight / (height * height)
    if BMI < 18.5:
        print("You are Underweight")
    elif BMI > 18.4 and BMI < 26:
        print("You are in Normal Weight")
    elif BMI > 24 and BMI < 30:
        print("You are overweight")
    elif BMI > 30:
        print("You are Obse")
    return BMI

# Main Function
def main():
    print("Welcome to BMI Calculator")
    weight = float(input("Enter Your weight in (KG): "))
    height = float(input("Enter Your height in (m): "))
    result = BMI_Calculation(weight, height)
    print(f"Your BMI is : {result}")

if __name__ =="__main__":
    main()
