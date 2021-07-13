#%% 
import numpy as np
np.random.seed(163)
df_thresh = 0.95
minimum_number_of_rounds_player = 21
dfs_checks = []
for i in range(500):
    if i < minimum_number_of_rounds_player:
        dfs_checks.append(False)
    else:
        current_check = np.random.rand() > df_thresh
        if True in dfs_checks:
            dfs_checks.append(True)
        else:
            dfs_checks.append(current_check)

# %%
