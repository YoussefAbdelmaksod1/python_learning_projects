import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12,6))
from random import choice
def random_walk(num):
    step_option = [1, -1]
    choice_step = choice(step_option)
    walk = []
    step = choice(step_option)
    walk.append(step)
    for i in range(1, num):
        next_step = walk[-1] + choice(step_option)
        walk.append(next_step)
    return walk

def plot_rnwalks(num_of_walks_required, num_of_steps):
    lab_list=(range(1,num_of_walks_required+1))
    for i in range(num_of_walks_required):
        plt.plot(random_walk(num_of_steps),label="Plot no" + " "+str(lab_list[i]))
        plt.xlabel("Steps")
        plt.ylabel("Distance from origin")
        plt.legend(loc="best")
    plt.show()
plot_rnwalks(5,100000)
