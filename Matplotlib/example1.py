import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure() # empty figure
plt.title("Cosine function for the numbers beetwen -3 π  and 3 π  with 0.1 intervals.\n\n")


x = np.arange(-3*np.pi,3*np.pi,0.1)
y = np.cos(x)




fig, ax = plt.subplots()

ax.plot(x, y)

