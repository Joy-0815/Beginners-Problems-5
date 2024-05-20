count = 0

FoodList = []
food = True

for num in range (0,8):
    food = input("What is your favourite food?").lower()
    if food == "pesto":
      count += 1
    else:
      FoodList.append(food)
        
print(count,"people like pesto")
for num in range (count):
    print("I like pesto")

print("Other foods:")
print(FoodList)
