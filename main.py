import gameoflife_class
#import Tkinter

row = int(raw_input("Number of rows: "))
col = int(raw_input("Number of cols: "))

#print np.random.random_integers(0,1,(row, col))
g_initial = gameoflife_class.Grid(row,col, True)
#print g_initial.print_grid()
g_initial.printVec()
print "#"*50
#g_initial.print_neighbour_grid()
for i in range(500):
    g_initial.generation_evolution()
    #print
    #print "="*50
    #print

print g_initial.stringGrid()
print "#"*50
g_initial.generation_evolution()
print g_initial.stringGrid()
#top = Tkinter.Tk()
#top.mainloop()
#op.mainloop()