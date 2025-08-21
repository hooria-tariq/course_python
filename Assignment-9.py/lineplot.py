import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10]) 
y = np.array([1,2,3,4,5,6,7,8,9,10])

plt.plot(x, y, marker="o",color="grey") 

font1 = {'family':'serif','color':'black','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Simple Line Plot", fontdict = font1)
plt.xlabel("X Values", fontdict = font2)
plt.ylabel("Y Values", fontdict = font2)

plt.grid(color = 'darkblue',linestyle = "dotted", linewidth = 0.5)

plt.plot(x,y, color='darkblue')

plt.savefig("lineplot.png") 
plt.show()

