# Day-3.4 Pizza Order
# Menu for Pizzas
def menu():
    small_pizza = 15
    medium_pizza = 20
    large_pizza = 25
    pepperoni_small = 2
    pepperoni_medium = 3
    pepperoni_large = 3
    cheese_cost = 1
    return small_pizza, medium_pizza, large_pizza, pepperoni_small, pepperoni_medium, pepperoni_large, cheese_cost



def logic_for_pizza_order(size, pepperoni, cheese,small_pizza, medium_pizza, large_pizza, pepperoni_small, pepperoni_medium, pepperoni_large, cheese_cost):
    # for small size pizza
    if size == "s" and pepperoni == "y" and cheese == "y":
        return small_pizza + pepperoni_small + cheese_cost
    elif size == "s" and pepperoni == "y" and cheese == "n":
        return small_pizza + pepperoni_small
    elif size == "s" and pepperoni == "n" and cheese == "y":
        return small_pizza + cheese_cost
    elif size == "s" and pepperoni == "n" and cheese == "n":
        return small_pizza  
    # for medium size pizza
    if size == "m" and pepperoni == "y" and cheese == "y":
        return medium_pizza + pepperoni_medium + cheese_cost
    elif size == "m" and pepperoni == "y" and cheese == "n":
        return medium_pizza + pepperoni_medium
    elif size == "m" and pepperoni == "n" and cheese == "y":
        return medium_pizza + cheese_cost
    elif size == "m" and pepperoni == "n" and cheese == "n":
        return medium_pizza
    # for large size pizza
    if size == "l" and pepperoni == "y" and cheese == "y":
        return large_pizza + pepperoni_large + cheese_cost
    elif size == "l" and pepperoni == "y" and cheese == "n":
        return large_pizza + pepperoni_large
    elif size == "l" and pepperoni == "n" and cheese == "y":
        return large_pizza + cheese_cost
    elif size == "l" and pepperoni == "n" and cheese == "n":
        return large_pizza


def main():
    print("Welcome to python pizza delivery")
    menu()
    size = input("What Size Pizza Do You want? S,M,L: ").lower()
    pepperoni = input("Do You Want Pepperoni? Y or N: ").lower()
    cheese = input("Do You Want Extra Cheese? Y or N: ").lower()
    small_pizza = 15
    medium_pizza = 20
    large_pizza = 25
    pepperoni_small = 2
    pepperoni_medium = 3
    pepperoni_large = 3
    cheese_cost = 1
    result = logic_for_pizza_order(size,pepperoni,cheese, small_pizza, medium_pizza, large_pizza, pepperoni_small, pepperoni_medium, pepperoni_large, cheese_cost)
    print(result)

if __name__ == "__main__":
    main()
