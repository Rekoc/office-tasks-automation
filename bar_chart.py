import matplotlib.pyplot as plt
from demo_pandas import main
import numpy as np

plt.style.use('_mpl-gallery')

# Collect the DataFrame from our previous script made with Pandas
data_frame = main()

# Plot
fig, ax = plt.subplots()

# Put the values into the chart
ax.bar(
    data_frame["colonne_1"],
    data_frame["colonne_5"],
    width=1,
    edgecolor="red",
    linewidth=0.8
)

# Configure the axis
ax.set(
    xlim=(0, 8), xticks=np.arange(0, 8),
    ylim=(0, 500), yticks=np.arange(0, 500, 50)
)

# Display the chart
plt.show()