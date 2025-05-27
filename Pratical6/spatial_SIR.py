import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
colors = ['white', 'yellow', 'green']  # white: healthy, yellow: infected, green: Healed
cmap = ListedColormap(colors)
population = np.zeros((100, 100))
out_break = np.random.choice(range(100), 2)
population[out_break[0], out_break[1]] = 1
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
im = ax.imshow(population, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
def update(frame):
    print(f"frames now: {frame}")
    global population
    new_population = population.copy()
    for x in range(100):
        for y in range(100):
            if population[x, y] == 1:
                p = np.random.binomial(1, 0.05)
                if p == 1:
                    new_population[x, y] = 2
            if population[x, y] == 1:
                if y == 0:
                    continue
                if population[x, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x, y - 1] == 0:
                        new_population[x, y - 1] = 1
            if population[x, y] == 1:
                if y == 99:
                    continue
                if population[x, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x, y + 1] == 0:
                        new_population[x, y + 1] = 1
            if population[x, y] == 1:
                if x == 0:
                    continue
                if population[x - 1, y] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x - 1, y] == 0:
                        new_population[x - 1, y] = 1
            if population[x, y] == 1:
                if x == 99:
                    continue
                if population[x + 1, y] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x + 1, y] == 0:
                        new_population[x + 1, y] = 1
            if population[x, y] == 1:
                if x == 99 or y == 0:
                    continue
                if population[x + 1, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x + 1, y - 1] == 0:
                        new_population[x + 1, y - 1] = 1
            if population[x, y] == 1:
                if x == 99 or y == 99:
                    continue
                if population[x + 1, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x + 1, y + 1] == 0:
                        new_population[x + 1, y + 1] = 1
            if population[x, y] == 1:
                if x == 0 or y == 0:
                    continue
                if population[x - 1, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x - 1, y - 1] == 0:
                        new_population[x - 1, y - 1] = 1
            if population[x, y] == 1:
                if x == 0 or y == 99:
                    continue
                if population[x - 1, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x - 1, y + 1] == 0:
                        new_population[x - 1, y + 1] = 1
    population = new_population
    im.set_data(population)
    return im,
ani = FuncAnimation(fig, update, frames=1000, interval=200, blit=True)
plt.show()
