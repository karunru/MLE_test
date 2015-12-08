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

print(r1/n)
print(r2/n)

plt.plot(theta, P1, "b")
plt.plot([r1/n,r1/n],[0,P1[r1/n/0.01]], "b:")
plt.plot(theta, P2, "r")
plt.plot([r2/n,r2/n],[0,P2[r2/n/0.01]], "r:")
plt.show()

