#!/usr/bin/env python3

# Python program to find the shortest
# path between a given source cell
# to a destination cell.
import argparse

import numpy as np
from collections import deque

# Below lists details all 4 possible movements from a cell


row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# Function to check if it is possible to go to position (row, col)
# from current position. The function returns false if row, col:
# is not a valid position or has value 0,2 or it is already visited
def isValid(mat, visited, row, col):
    return (row >= 0) and (row < M) and (col >= 0) and (col < N) \
           and (mat[row][col] == 0 or mat[row][col] == 2)  and not visited[row][col]


# Find Shortest Possible Route in a matrix mat from source
# cell (i, j) to destination cell (x, y)
def BFS(mat, i, j, x, y):

    # construct a matrix to keep track of visited cells
    visited = [[False for x in range(N)] for y in range(M)]

    # create an empty queue
    q = deque()

    # mark source cell as visited and enqueue the source node
    visited[i][j] = True

    # (i, j, dist) represents matrix cell coordinates and its
    # minimum distance from the source
    q.append((i, j, 0))

    # stores length of longest path from source to destination
    min_dist = float('inf')

    # run till queue is empty
    while q:

        # pop front node from queue and process it
        (i, j, dist) = q.popleft()

        # (i, j) represents current cell and dist stores its
        # minimum distance from the source

        # if destination is found, update min_dist and stop
        if i == x and j == y:
            min_dist = dist
            break

        # check for all 4 possible movements from current cell
        # and enqueue each valid movement
        for k in range(4):
            # check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if isValid(mat, visited, i + row[k], j + col[k]):
                # mark next cell as visited and enqueue it
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))

    if min_dist != float('inf'):
        return min_dist
        #print("The shortest path from source to destination has length", min_dist)
    else:
        print("Destination can't be reached from given source")


# Shortest path in a Maze
if __name__ == '__main__':

    # parse the input argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--board')
    args = parser.parse_args()


    # parse the input file
    ar = np.genfromtxt(args.board, delimiter=",")
    mat = ar.astype('int32')

    # get M rows x N columns matrix dimentions
    M = len(mat)
    N = len(mat[0])

    # Get a list of all ghost coordinates and pacman coordinates from the matrix
    ghost_list = []
    for x in range(N):
        for y in range(M):
            if mat[x][y] == 2:
                ghost_list.append([x,y])
            if mat[x][y] == 3:
                a=x
                b=y

    # Find shortest path from pacman to all ghosts
    result_list=[]
    for ghost in ghost_list:
        result_list.append([(ghost[0],ghost[1]), BFS(mat, a, b, ghost[0], ghost[1])])


    result_list.sort(key=lambda result_list: result_list[1])
    print(result_list)


