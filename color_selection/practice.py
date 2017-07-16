import numpy as np
# from numpy.polynomial import polynomial as P


# x = np.linspace(-1,1,51)
# print("x",x)
# y = x ** 3 - x + np.random.randn(len(x))
# print("y",y)
# c, stats = P.polyfit(x,y,1)
# print("C",c)
# print("stats",stats)
#
# x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
# y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
# z = np.polyfit(x, y, 3)
# print (z)
# z = np.polyfit(x, y, 2)
# print (z)
# z = np.polyfit(x, y, 1)
# print (z)
# z = np.polyfit(x, y,0)
# print (z)
# z = np.polyfit(x, y)
# print (z)

# nx, ny = (3, 2)
# x = np.linspace(0, 1, nx)
# y = np.linspace(0, 1, ny)
# print x
# print y
# xv, yv = np.meshgrid(x, y)
# print xv
# print yv

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])
print(x)
XX, YY = np.meshgrid(x, y)
print(XX)
print(YY)