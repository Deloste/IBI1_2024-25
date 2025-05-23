import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
colors = ['white', 'yellow', 'green' ]  # white: healthy, yellow: infected, green: Healed
cmap = ListedColormap(colors)
population = np.zeros((100, 100))
out_break = np.random.choice(range(100), 2) 
population[out_break[0], out_break[1]] = 1
plt.figure(figsize=(6, 4), dpi=150) 
plt.imshow(population, cmap=cmap, interpolation='nearest',vmin=0,vmax=2)
i=1
while i<=100:
  i+=1
  for x in range(100):
    for y in range(100):
      if population[x, y] == 1:
        p=np.random.binomial(1, 0.05)
        if p==1:
          population[x, y] = 2
      if population[x, y] == 1:
        if y==0: 
          continue            
        if population[x, y-1] == 0:         
          p=np.random.binomial(1, 0.3)
          if p==1 and population[x, y-1]==0:
            population[x, y-1] = 1
      if population[x, y] == 1:
        if y==99:
            continue
        if population[x, y+1] == 0:
          p=np.random.binomial(1, 0.3)
          if p==1 and population[x, y+1]==0:
            population[x, y+1] = 1
      if population[x, y] == 1:
        if x==0:
            continue
        if population[x-1, y] ==0:         
          p=np.random.binomial(1, 0.3)
          if p==1 and population[x-1, y]==0:
            population[x-1, y] = 1
      if population[x, y] == 1:
        if x==99:
            continue
        if population[x+1, y] ==0:         
          p=np.random.binomial(1, 0.3)
          if p==1 and population[x+1, y]==0:
            population[x+1, y] = 1
      if population[x, y] == 1:
        if x==99 or y==0:
            continue
        if population[x+1, y-1] == 0:
          p=np.random.binomial(1, 0.3)
          if p==1 and population[x+1, y-1]==0:
            population[x+1, y-1] = 1
      if population[x, y] == 1:
        if x==99 or y==99:
              continue
        if population[x+1, y+1] == 0:      
            p=np.random.binomial(1, 0.3)
            if p==1 and population[x+1, y+1]==0:
             population[x+1, y+1] = 1
      if population[x, y] == 1:
        if x==0 or y==0:
            continue
        if population[x-1, y-1] == 0:
          p=np.random.binomial(1, 0.3)
          if p==1 and population[x-1, y-1]==0:
            population[x-1, y-1] = 1
      if population[x, y] == 1:
        if x==0 or y==99:
            continue
        if population[x-1, y+1] == 0:        
          p=np.random.binomial(1, 0.3)
          if p==1 and population[x-1, y+1]==0:
            population[x-1, y+1] = 1 
plt.imshow(population, cmap=cmap, interpolation='nearest',vmax=2,vmin=0)
plt.show()
