import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.generate_walk()

fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=15)

plt.show()
