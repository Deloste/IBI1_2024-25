import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

# Define color mapping: white=healthy(0), yellow=infected(1), green=recovered(2)
colors = ['white', 'yellow', 'green']  
cmap = ListedColormap(colors)

# Initialize 100x100 population grid with all healthy individuals
population = np.zeros((100, 100))

# Randomly select initial outbreak location
out_break = np.random.choice(range(100), 2)
population[out_break[0], out_break[1]] = 1  # Set initial infected point

# Create visualization figure
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
im = ax.imshow(population, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)

def update(frame):
    # Print current frame number for debugging
    print(f"frames now: {frame}")
    
    # Create buffer for simultaneous updates
    global population
    new_population = population.copy()
    
    # Process each cell in the grid
    for x in range(100):
        for y in range(100):
            # Recovery process: 5% chance infected becomes recovered
            if population[x, y] == 1:
                p = np.random.binomial(1, 0.05)
                if p == 1:
                    new_population[x, y] = 2
            
            # Infection spread to left neighbor (30% chance)
            if population[x, y] == 1:
                if y == 0:
                    continue
                if population[x, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x, y - 1] == 0:
                        new_population[x, y - 1] = 1
            
            # Infection spread to right neighbor (30% chance)
            if population[x, y] == 1:
                if y == 99:
                    continue
                if population[x, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x, y + 1] == 0:
                        new_population[x, y + 1] = 1
            
            # Infection spread to top neighbor (30% chance)
            if population[x, y] == 1:
                if x == 0:
                    continue
                if population[x - 1, y] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x - 1, y] == 0:
                        new_population[x - 1, y] = 1
            
            # Infection spread to bottom neighbor (30% chance)
            if population[x, y] == 1:
                if x == 99:
                    continue
                if population[x + 1, y] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x + 1, y] == 0:
                        new_population[x + 1, y] = 1
            
            # Infection spread to bottom-left neighbor (30% chance)
            if population[x, y] == 1:
                if x == 99 or y == 0:
                    continue
                if population[x + 1, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x + 1, y - 1] == 0:
                        new_population[x + 1, y - 1] = 1
            
            # Infection spread to bottom-right neighbor (30% chance)
            if population[x, y] == 1:
                if x == 99 or y == 99:
                    continue
                if population[x + 1, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x + 1, y + 1] == 0:
                        new_population[x + 1, y + 1] = 1
            
            # Infection spread to top-left neighbor (30% chance)
            if population[x, y] == 1:
                if x == 0 or y == 0:
                    continue
                if population[x - 1, y - 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x - 1, y - 1] == 0:
                        new_population[x - 1, y - 1] = 1
            
            # Infection spread to top-right neighbor (30% chance)
            if population[x, y] == 1:
                if x == 0 or y == 99:
                    continue
                if population[x - 1, y + 1] == 0:
                    p = np.random.binomial(1, 0.3)
                    if p == 1 and new_population[x - 1, y + 1] == 0:
                        new_population[x - 1, y + 1] = 1
    
    # Update global population state
    population = new_population
    im.set_data(population)
    return im,

# Create animation with 1000 frames, 200ms interval
ani = FuncAnimation(fig, update, frames=1000, interval=200, blit=True)
plt.show()
