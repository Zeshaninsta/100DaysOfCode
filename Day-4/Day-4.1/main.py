# Head or Tail
def game_logic(seed):
    import random
    random.seed(seed)
    Num = random.randint(0, 1)
    if Num == 1:
        return "Heads"
    elif Num == 0:
        return "Tails"


def main():
    seed = int(input("Create a seed Number: "))
    result = game_logic(seed)
    print(result)



if __name__ == "__main__":
    main()
