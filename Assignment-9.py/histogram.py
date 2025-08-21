import matplotlib.pyplot as plt
import numpy as np

data = (7,8,5,6,5,7,8,9,6,5,7,6,8,9,7,6,5,8,9,7)

plt.figure(figsize=(8,5))
plt.hist(data)        

plt.savefig("histogram.png")     
plt.show()