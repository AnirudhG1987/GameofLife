import numpy as np


class Grid(object):

    def __init__(self,*args):
        if len(args) == 1:
            # this loads a text file as a list, each string is a list, important to definte the type
            # this splits each string to its characters and then makes a numpy array
            #vectorize is used to convert string to number
            self.grid = np.vectorize(self.XandOtonum)(np.array([list(x) for x in np.loadtxt(args[0],dtype=np.str)]))
            (self.row,self.col) = self.grid.shape

        elif len(args)>2:
            self.row = args[0]
            self.col = args[1]
            # self.grid = np.zeros((row,col),dtype=np.int)
            self.grid = np.random.random_integers(0, 1, (self.row, self.col))

    def printVec(self):
        print np.vectorize(self.numtoXandO)(self.grid)

    def stringGrid(self):
        temp = ''
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] > 0:
                    temp += 'x'
                else:
                    temp += '-'
            temp += '\n'
        return temp

    def numtoXandO(self, x):
        if x >0:
            return "x"
        else:
            return "-"

    def XandOtonum(self, x):
        return np.where(x == 'X', 1, 0)

    def neighbour_count(self, row, col):
        count = 0
        #print "current row col ",row,col
        if row < self.row-1:
            up_row = row + 1
        else:
            up_row = row
        if row > 0:
            down_row = row - 1
        else:
            down_row = row
        if col < self.col-1:
            up_col = col + 1
        else:
            up_col = col
        if col > 0:
            down_col = col - 1
        else:
            down_col = col
        #print up_row, up_col, down_row, down_col
        # dont do up_row+1, up_col  + 1 .. it will be diff for c++
        for i in range(down_row, up_row + 1):
            for j in range(down_col, up_col + 1):
                if self.grid[i][j] > 0:
                    count+=1
        # dont count current cell
        if self.grid[row][col] > 0:
            return count-1
        else:
            return count

    def print_neighbour_grid(self):
        for i in range(self.row):
            for j in range(self.col):
                print self.neighbour_count(i,j),
            print

    # function that updates the grid for 1 generation
    def generation_evolution(self):
        g_scratch = np.copy(self.grid)
        for i in range(self.row):
            for j in range(self.col):
                neigh_count = self.neighbour_count(i,j)
                if neigh_count <= 1:
                    # make sure its the scratch grid
                    g_scratch[i][j] = 0
                elif neigh_count == 2:
                    if self.grid[i][j] > 0:
                        g_scratch[i][j]+= 1
                elif neigh_count == 3:
                    g_scratch[i][j]+=1
                elif neigh_count > 3:
                    g_scratch[i][j] = 0
         # once done with entire grid changing, copy it to the original grid
        self.grid = g_scratch