cerealList = []
food = True

while food == True:
    cereal = input("What is your favourite cereal?")
    if cereal == "sultrana and bran":
        print(cerealList)
        quit()
    elif cereal == "weetbix":
        print(cerealList)
        quit()
    else:
        cerealList.append(cereal)
