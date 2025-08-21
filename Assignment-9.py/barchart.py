import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Ali", "Sara", "John", "Ayesha", "Tom"])
y = np.array([80, 90, 70, 85, 60])
mycolors = ['#FFCBE1', '#D6E5BD', '#FFDAB4', '#BCD8EC', "#DCCCEC"]

font1 = {'family':'serif','color':'brown','size':23}
font2 = {'family':'serif','color':'#47443D','size':13}

plt.title("Students Record", fontdict = font1)
plt.xlabel("Student Names", fontdict = font2)
plt.ylabel("Marks", fontdict = font2)

plt.bar(x,y, color= mycolors)
plt.savefig("barchart.png") 
plt.show()
