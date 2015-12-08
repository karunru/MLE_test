import numpy as np
import matplotlib.pyplot as plt

n = 10 #試行回数
r1 = 8 #表になった数
r2 = 3 #表になった数

#系列を作成(使わなかった)
#X = ["T"] * n
#for i in range(r):
#	X[i] = "H"
#
#np.random.shuffle(X)
#print(X)

theta = np.arange(0,1,0.01) #0から1まで0.01刻みでthetaを動かす
P1 = np.power(theta, r1) * np.power(1-theta, n-r1) #r1の時の確率
P2 = np.power(theta, r2) * np.power(1-theta, n-r2) #r2の時の確率

#最大値(推定値)を表示
print(r1/n)
print(r2/n)

plt.plot(theta, P1, "b") #P1のグラフ
plt.plot([r1/n,r1/n],[0,P1[r1/n/0.01]], "b:") #P1の最大値のとこの点線
plt.plot(theta, P2, "r") #P2のグラフ
plt.plot([r2/n,r2/n],[0,P2[r2/n/0.01]], "r:") #P2の最大値のとこの点線
plt.show()

