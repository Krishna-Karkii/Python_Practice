import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots()

# plotting the graph
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

# customizing the labels of the graph
ax.set_title("Squared Numbers", fontsize=20)
ax.set_xlabel("Numbers", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)
ax.tick_params(labelsize=14)

# setting the tick range fo x-axis and y-axis, setting tick-label-format to plain
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")

# show the output of the plot
plt.show()
