# Age Calculation Logic
def logic_yourLife(age):
    Target = 90
    Days = 365
    Weeks = 52
    Months = 12
    left_Days = 90 * Days - age * Days
    left_Weeks = 90 * Weeks - age * Weeks
    left_Months = 90 * Months - age * Months
    print (f"You Have {left_Days} days, {left_Weeks} Weeks, {left_Months} Months left.")

def main():
    age = int(input("what is your current age? "))
    result = logic_yourLife(age)

if __name__ == "__main__":
    main()
