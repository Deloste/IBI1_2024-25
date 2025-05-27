import numpy as np
import matplotlib.pyplot as plt
np.random.choice(range(2),4,p=[0.7,0.3])
for p in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]:
  S,V,I,R=int((1-p)*(10000-1)),int(p*(10000-1)),1,0
  data={}
  i=1
  while i<=1000:
    i+=1
    S0=S  
    S=S-np.random.binomial(I, 0.3)*S0/10000
    R=R+np.random.binomial(I, 0.05)
    I=I+np.random.binomial(I, 0.3)*S0/10000-np.random.binomial(I, 0.05)
    data[f"step_{i}"] = {
        "I": I
    }
  plt.plot([v["I"] for v in data.values()], label=f"{p*1.00}")
plt.xlabel("Time")
plt.ylabel("Infected People")
plt.legend()
plt.show()
