import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,0,0]]



def possible(row,column,n):

	#checking whether the number is in the row
	for i in range(9):
		if grid[row][i] == n:
			return False

	#checking whether the number is in the column
	for i in range(9):
		if grid[i][column] == n:
			return False

	#checking in the square
	x0 = row//3 * 3
	y0 = column//3 * 3

	for i in range(3):
		for j in range(3):
			if grid[x0+i][y0+j] == n:
				return False
	return True

def solve():
	global grid
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				for n in range(1,10):
					if possible(i,j,n):
						grid[i][j] = n
						solve()
						grid[i][j] = 0 

				return

	print(np.matrix(grid))
	input('more solution?')


solve()
