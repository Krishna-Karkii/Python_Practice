import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn-v0_8-white")
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Reds)

# set the labels of the chart
ax.set_title("Cubic Chart", fontsize=20)
ax.set_xlabel("Numbers", fontsize=14)
ax.set_ylabel("Cubic Values", fontsize=14)
ax.tick_params(labelsize=14)

# set the axis values, set the tick-label-format to plain
ax.axis([0, 1100, 0, 1_100_000_000])
ax.ticklabel_format(style="plain")

plt.show()
