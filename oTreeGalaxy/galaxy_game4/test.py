#%% 
import numpy as np
np.random.seed(163)
dfs_checks = []
for i in range(500):
    if i < 20:
        dfs_checks.append(False)
    else:
        current_check = np.random.rand() > 0.85
        if True in dfs_checks:
            dfs_checks.append(True)
        else:
            dfs_checks.append(current_check)
rewards = {}
for planet in range(1, 366): #for each planet
    rewards[planet] = {}
    current_planet_center = np.random.randint(1, 10)*10 
    for r in range(1, 466): #number of exploiting choice
        rewards[planet][r] = np.random.randint(current_planet_center - 10, current_planet_center + 10)
# %%
for i in range(1, 10):
    payoff = sum([rewards[3][r] for r in range(i, i+3)])
    print(payoff)

# %%
