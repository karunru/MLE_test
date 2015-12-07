import numpy as np
import matplotlib.pyplot as plt

n = 10
r1 = 8
r2 = 3

#X = ["T"] * n
#for i in range(r):
#	X[i] = "H"
#
#np.random.shuffle(X)
#print(X)

theta = np.arange(0,1,0.01)
P1 = np.power(theta, r1) * np.power(1-theta, n-r1)
P2 = np.power(theta, r2) * np.power(1-theta, n-r2)

plt.plot(theta, P1, "b")
plt.plot(theta, P2, "r")
plt.show()
