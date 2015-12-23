def getMult(x2, x4):

	x1 = 60 - x2
	x3 = 40 - x4

	part1 = 2*x1
	part2 = 5*x2 - x4
	part3 = 5*x3 - 3*x2 -2*x1
	part4 = 5*x4 - x3

	if part1 <= 0:
		part1 = 0
	if part2 <= 0:
		part2 = 0
	if part3 <= 0:
		part3 = 0
	if part4 <= 0:
		part4 = 0	

	multiplication = part1 * part2 * part3 * part4

	return multiplication

# Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
# Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
# Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
# Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8

# x1 + x2 + x3 + x4 	= 100
# 3x1 + 3x2 + 8x3 + 8x4 = 500

# x1 = 100 - x2 -x3 -x4
# 3(100 -x2 -x3 -x4) + 3x2 + 8x3 + 8x4 = 500  <==> 5x3 + 5x4 = 200 <==> x3 = 40 - x4

# x1 + x2 + x3 + x4 = 100 <==> x1 + x2 + 40 - x4 + x4 = 100 <==> 		x1 = 60 - x2

# 0 <= x2 <= 60
# 0 <= x4 <= 40

holder = [None] * 60

for i in range(0, 60):
	holder[i] = [None] * 40
	for j in range(0, 40):
		holder[i][j] = getMult(i, j)

newholder = [None] * 60

for i in range(0, 60):
	max_j_index = holder[i].index(max(holder[i]))
	newholder[i] = [max(holder[i]), max_j_index]

max_i_index = newholder.index(max(newholder))

print newholder[max_i_index][0]











