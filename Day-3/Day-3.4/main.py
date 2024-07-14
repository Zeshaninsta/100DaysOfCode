# Day-3.4 Pizza Order

def get_pizza_price():
    return{
            's': 15,
            'm': 20,
            'l': 25,
            'pepperoni_small': 2,
            'pepperoni_medium&large': 3,
            'cheese': 1
            }
def calculate_pizza_price(size,pepperoni, cheese,price):
    basic_price = price[size]
    cost = basic_price
    if pepperoni == "y":
        if size == "s":
            cost += price['pepperoni_small']
        else:
            cost += price['pepperoni_medium&large']
    if cheese == "y":
        cost += price['cheese']
    return cost


def get_user_input():
    size = input("What size of pizza do you want? S,M,Y: ").lower()
    pepperoni = input("Do you want pepperoni? ").lower()
    cheese = input("do you want a cheese? ").lower()
    return size,pepperoni,cheese



def main():
    print("Welcome to python pizza delivery")
    size,pepperoni,cheese = get_user_input()
    price = get_pizza_price()
    result = calculate_pizza_price(size,pepperoni,cheese,price)
    print(f"Your total is Payment is: ${result}")

if __name__ == "__main__":
    main()
