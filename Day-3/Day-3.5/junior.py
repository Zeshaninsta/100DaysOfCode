# Day-3.5 Love Calculator
true = "true"
love = "love"
Your_Name = input("enter your name: ")
Her_Name = input("enter Her name: ")
name = Your_Name + Her_Name
true_count = 0
love_count = 0
print(name)
for i in true:
    count = name.count(i)
    true_count += count
for i in love:
    count = name.count(i)
    love_count += count

result = str(true_count) + str(love_count)
print(f"Your Love Score is : {result}%")
