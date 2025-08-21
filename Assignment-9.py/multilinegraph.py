import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])   
y1 = x                    
y2 = x**2                 

plt.plot(x, y1, label="y = x", color="purple", linestyle="solid", marker="*", ms=12)
plt.plot(x, y2, label="y = x^2", color="hotpink", linestyle="dashed", marker="o" )

plt.xlabel("X-Values", fontsize=12, color="Grey")
plt.ylabel("Y-Values", fontsize=12, color="Grey")
plt.title("Multiple Lines on One Graph", fontsize=18, color="Brown")


plt.legend()
plt.savefig("multilinegraph.png")    
plt.show()
