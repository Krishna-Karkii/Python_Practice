import matplotlib.pyplot as plt
import numpy

# create an array to plot in graph
x = numpy.array(range(1001))
y = x ** 2
z = x * 2

plt.scatter(x, z, c=x, cmap=plt.cm.Blues, s=10)
plt.scatter(x, y, c=x,  cmap=plt.cm.Reds, s=10)

# set the properties of the chart
plt.axis([1, 1100, 1, 1_100_000])
plt.xlabel("Number", fontsize=14)
plt.ylabel("Values", fontsize=14)
plt.ticklabel_format(style="plain")

plt.show()
