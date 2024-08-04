def program_logic(seed, names):
    import random
    random.seed(seed)
    result = random.shuffle(names)
    pick = names[0]
    return pick

def main():
    seed = int(input("create seed number: "))
    names = input("please Provide everyone names with comma separated: ").split(", ")
    result = program_logic(seed, names)
    print(f"{result} is going to pay")


if __name__ == "__main__":
    main()
