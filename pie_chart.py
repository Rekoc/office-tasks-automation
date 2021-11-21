import matplotlib.pyplot as plt
from demo_pandas import main
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

data_frame = main()
# make data
x = data_frame["colonne_1"]
colors = plt.get_cmap('Greens')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()