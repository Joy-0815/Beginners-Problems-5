numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]
numsList.sort()
print("Largest number is:", numsList[-1])
print("Smallest number is:", numsList[0])
numsList.remove(numsList[-1])
numsList.remove(numsList[0])

dived = len(numsList)

average = sum(numsList) / dived
print("The average of the rest of the numbers is",average)
