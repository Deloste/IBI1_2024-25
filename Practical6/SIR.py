import numpy as np
import matplotlib.pyplot as plt
np.random.choice(range(2),4,p=[0.7,0.3])
i=1
S,I,R=9999,1,0
data={}
while i<=1000:
    i+=1
    S0=S  
    S=S-np.random.binomial(I, 0.3)*S0/10000
    R=R+np.random.binomial(I, 0.05)
    I=I+np.random.binomial(I, 0.3)*S0/10000-np.random.binomial(I, 0.05)
    data[f"step_{i}"] = {
        "S": S,
        "I": I,
        "R": R
    }
plt.plot([v["S"] for v in data.values()], label="Susceptible")
plt.plot([v["I"] for v in data.values()], label="Infected")
plt.plot([v["R"] for v in data.values()], label="Recovered")
plt.legend()
plt.show()
