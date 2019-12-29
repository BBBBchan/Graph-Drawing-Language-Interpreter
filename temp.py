import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)

x = [  0. , 2. ,  4. ,  6. ,  8. ,10.]
y = [1. ,0. ,  -1.  , -2.  , -3. ,  -4.]
ax.scatter(x,y)
plt.show()