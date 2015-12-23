import numpy as np

# Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
# Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
# Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
# Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8

def checkPositive(ingredients, total):
	A = np.dot(ingredients, total)
	CMatrix = np.sum(A,0)
	for i in range(0, CMatrix.size):
		if CMatrix[0, i] <= 0:
			return False
	return True

def getMultiplication(ingredients, total, limit):
	A = np.dot(ingredients, total)
	CMatrix = np.sum(A,0)
	
	# if checkPositive(ingredients, total):
	multiplication = 1

	for i in range(0, limit):
		multiplication *= CMatrix[0,i]

	return multiplication

def getIncrementindex(ingredients, total):
	current_value = getMultiplication(ingredients, total)
	diff_values = [0]*4
	for i in range(0, 4):				
		ingredients[0, i] += 1
		if not checkPositive(ingredients, total):
			diff_values[i] = float('-inf')
		else:
			multiplication = getMultiplication(ingredients, total, 4)
			diff_values[i] = multiplication - current_value	
		ingredients[0, i] -= 1

	theindex = diff_values.index(max(diff_values))
	return theindex

# testcase 
# ingredients = np.matrix('44, 56')
# total = np.matrix('-1, -2, 6, 3; 2, 3, -2, -1')
# print getMultiplication(ingredients, total)
# print np.dot(ingredients, total)

# PART 1

ingredients = np.matrix('1, 1, 2, 1')
total = np.matrix('2, 0, -2, 0; 0, 5, -3, 0; 0, 0, 5, -1; 0, -1, 0, 5')

while np.sum(ingredients) < 100:
	theindex = getIncrementindex(ingredients, total)
	ingredients[0, theindex] += 1
	
print getMultiplication(ingredients, total)
