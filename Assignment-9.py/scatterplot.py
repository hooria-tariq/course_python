import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([2,4,1,5,7])
colors = np.array(["hotpink","purple","cyan","brown","magenta"])

plt.xlabel("X-axis", fontsize=12, color="darkgrey")
plt.ylabel("Y-axis", fontsize=12, color="darkgrey")
plt.title("Scatter Plot",fontsize=22, color="black")

plt.scatter(x, y, c=colors, marker="D")
plt.savefig("scatterplot.png")
plt.show()

