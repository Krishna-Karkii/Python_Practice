import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    # create the random walk generate
    rw = RandomWalk()
    rw.generate_walk()

    # fig for the figure, ax for plot
    fig, ax = plt.subplots()

    # create list of points to assign for a step
    points = range(rw.nums)

    ax.scatter(rw.x_values, rw.y_values, c=points, cmap=plt.cm.Reds, s=15)
    ax.set_aspect("equal")
    plt.show()

    # ask if to generate the graph again
    keep_generation = input("Do you want to generate walk? (y/n): ")
    if keep_generation.strip().capitalize() == "N":
        break
