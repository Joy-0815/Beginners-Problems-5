numsList.sort()
print("Largest number is:", numsList[-1])
print("Smallest number is:", numsList[1])
numsList.remove(numsList[-1])
numsList.remove(numsList[1])

dived = len(numsList)

average = sum(numsList) % dived
print("The average of the rest of the numbers is",average)
