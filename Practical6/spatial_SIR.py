import numpy as np  # Import numpy for array handling
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from matplotlib.colors import ListedColormap  # For custom color mapping

# Define custom colormap: 0 = healthy (white), 1 = infected (yellow), 2 = healed (green)
colors = ['white', 'yellow', 'green']
cmap = ListedColormap(colors)

# Create a 100x100 grid of zeros representing healthy individuals
population = np.zeros((100, 100))

# Randomly choose one cell to be the initial outbreak
out_break = np.random.choice(range(100), 2)
population[out_break[0], out_break[1]] = 1  # Set initial infected cell

plt.figure(figsize=(6, 4), dpi=150)  # Create a figure for plotting

i = 1
while i <= 100:  # Simulate for 100 steps
    i += 1

    # Only plot every 10 steps
    if i % 10 == 0:
        plt.clf()  # Clear previous frame
        plt.imshow(population, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)  # Show current state
        plt.title(f"Step {i}")  # Display step number
        plt.pause(0.1)  # Pause to allow visual update (animation effect)

    for x in range(100):
        for y in range(100):
            # If current cell is infected
            if population[x, y] == 1:
                # Recovery phase: 5% chance to heal
                p = np.random.binomial(1, 0.05)
                if p == 1:
                    population[x, y] = 2

            # Infection spread logic

            # Spread left
            if population[x, y] == 1:
                if y == 0:
                    continue
                if population[x, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1:
                        population[x, y - 1] = 1

            # Spread right
            if population[x, y] == 1:
                if y == 99:
                    continue
                if population[x, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1:
                        population[x, y + 1] = 1

            # Spread up
            if population[x, y] == 1:
                if x == 0:
                    continue
                if population[x - 1, y] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1:
                        population[x - 1, y] = 1

            # Spread down
            if population[x, y] == 1:
                if x == 99:
                    continue
                if population[x + 1, y] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1:
                        population[x + 1, y] = 1

            # Spread down-left
            if population[x, y] == 1:
                if x == 99 or y == 0:
                    continue
                if population[x + 1, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1:
                        population[x + 1, y - 1] = 1

            # Spread down-right
            if population[x, y] == 1:
                if x == 99 or y == 99:
                    continue
                if population[x + 1, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1:
                        population[x + 1, y + 1] = 1

            # Spread up-left
            if population[x, y] == 1:
                if x == 0 or y == 0:
                    continue
                if population[x - 1, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1:
                        population[x - 1, y - 1] = 1

            # Spread up-right
            if population[x, y] == 1:
                if x == 0 or y == 99:
                    continue
                if population[x - 1, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1:
                        population[x - 1, y + 1] = 1

# Final display after simulation ends
plt.imshow(population, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
plt.title("Final State")
plt.show()

