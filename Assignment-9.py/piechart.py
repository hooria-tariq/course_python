import matplotlib.pyplot as plt
import numpy as np

hours = np.array([8, 7, 4, 2, 3])
mylabels = ["Sleeping", "School", "Hobbies", "Exercise", "Other"]
mycolors = ['#FFCBE1', '#D6E5BD', '#FFDAB4', '#BCD8EC', "#DCCCEC"]
myexplode = [0.18, 0.17, 0.14, 0.12, 0.13]

plt.figure(figsize=(8,5))

plt.pie(hours, labels = mylabels,autopct='%2.0f%%',  colors = mycolors, explode = myexplode)       


plt.legend(title = 'Daily Activities')         

plt.savefig("piechart.png")     
plt.show() 