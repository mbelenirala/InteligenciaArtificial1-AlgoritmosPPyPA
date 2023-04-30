# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time
from colorama import init
from colorama import Fore, Back, Style


## Functions
def printMaze(maze,height,width):
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")
			elif (maze[i][j] == '0'):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			elif(i==0 and j == 0):
				print(Fore.BLUE + str(maze[i][j]), end=" ")	
			elif(i==9 and j == 9):
				print(Fore.BLUE + str(maze[i][j]), end=" ")	
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")

		print('\n')

from tkinter import *
from colorama import Fore  # Opcional si quieres seguir usando Colorama para los colores de consola

def printMaze2(maze, height, width, text_widget):
    # Configurar las tags de los colores
    text_widget.tag_config('white', background='white')
    text_widget.tag_config('green', background='green')
    text_widget.tag_config('blue', background='blue')
    text_widget.tag_config('red', background='red')

    # Recorrer la matriz y agregar cada carácter con su respectiva tag
    for i in range(height):
        for j in range(width):
            if maze[i][j] == 'u':
                text_widget.insert(END, maze[i][j], 'white')
            elif maze[i][j] == '0':
                text_widget.insert(END, maze[i][j], 'green')
            elif i == 0 and j == 0:
                text_widget.insert(END, maze[i][j], 'blue')
            elif i == height-1 and j == width-1:
                text_widget.insert(END, maze[i][j], 'blue')
            else:
                text_widget.insert(END, maze[i][j], 'red')
        text_widget.insert(END, '\n')  # Agregar salto de línea al final de cada fila


# Find number of surrounding cells
def surroundingCells(maze, rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == '0'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == '0'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == '0'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == '0'):
		s_cells += 1

	return s_cells

def generateMaze():
	## Main code
	# Init variables
	wall = 'x'
	cell = '0'
	unvisited = 'u'
	height = 10
	width = 10
	maze = []
	entrada = 'I'
	salida = 'F'

	# Initialize colorama
	init()

	# Denote all cells as unvisited
	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited)
		maze.append(line)

	# Randomize starting point and set it a cell
	starting_height = int(9)
	starting_width = int(9)
	if (starting_height == 0):
		starting_height += 1
	if (starting_height == height-1):
		starting_height -= 1
	if (starting_width == 0):
		starting_width += 1
	if (starting_width == width-1):
		starting_width -= 1

	# Mark it as cell and add surrounding walls to the list
	maze[starting_height][starting_width] = cell
	walls = []
	walls.append([starting_height - 1, starting_width])
	walls.append([starting_height, starting_width - 1])
	walls.append([starting_height, starting_width + 1])
	walls.append([starting_height + 1, starting_width])

	# Denote walls in maze
	maze[starting_height-1][starting_width] = 'x'
	maze[starting_height][starting_width - 1] = 'x'
	maze[starting_height][starting_width + 1] = 'x'
	maze[starting_height + 1][starting_width] = 'x'

	while (walls):
		# Pick a random wall
		rand_wall = walls[int(random.random()*len(walls))-1]

		# Check if it is a left wall
		if (rand_wall[1] != 0):
			if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == '0'):
				# Find the number of surrounding cells
				s_cells = surroundingCells(maze,rand_wall)

				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = '0'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'x'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])


					# Bottom cell
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'x'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):	
						if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'x'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
				

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check if it is an upper wall
		if (rand_wall[0] != 0):
			if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == '0'):

				s_cells = surroundingCells(maze,rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = '0'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'x'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'x'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])

					# Rightmost cell
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'x'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check the bottom wall
		if (rand_wall[0] != height-1):
			if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == '0'):

				s_cells = surroundingCells(maze,rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = '0'

					# Mark the new walls
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'x'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'x'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'x'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)


				continue

		# Check the right wall
		if (rand_wall[1] != width-1):
			if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == '0'):

				s_cells = surroundingCells(maze,rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = '0'

					# Mark the new walls
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'x'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'x'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[0] != 0):	
						if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'x'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Delete the wall from the list anyway
		for wall in walls:
			if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
				walls.remove(wall)
		


	# Mark the remaining unvisited cells as walls
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				maze[i][j] = 'x'

	# Set entrance and exit
	for i in range(0, width):
		if (maze[1][i] == '0'):
			maze[0][i] = '0'
			break

	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == '0'):
			maze[height-1][i] = '0'
			break
	al = random.randint(2,7)
	for i in range(1,al):
		maze[al][i] = cell

	maze[0][0] = salida
	maze[9][9] = entrada
	maze[0][1] = cell
	maze[9][8] = cell

	# Print final maze
	#printMaze(maze)

	return maze 