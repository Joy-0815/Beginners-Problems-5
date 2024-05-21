cerealList = []

while True:
    cereal = input("What is your favourite cereal?")
    if cereal == "sultrana and bran" or cereal == "weetbix":
        print(cerealList)
        break
    else:
        cerealList.append(cereal)
