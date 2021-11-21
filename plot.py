import matplotlib.pyplot as plt
from demo_pandas import main
import numpy as np

plt.style.use('_mpl-gallery')

# Get data from ou DataFrame
data_frame = main()

# Create the first plot
x1 = data_frame["colonne_3"]
y1 = data_frame["colonne_5"]
colonne_3_min = data_frame["colonne_3"].min()
colonne_3_max = data_frame["colonne_3"].max()
colonne_5_min = data_frame["colonne_5"].min()
colonne_5_max = data_frame["colonne_5"].max()

# Create the second plot
x2 = data_frame["colonne_4"]
y2 = data_frame["colonne_5"]

# Plot
fig, ax = plt.subplots()
# Add the plots to the chart
ax.plot(x1, y1, linewidth=2.0, color="green")
ax.plot(x2, y2, linewidth=2.0, color="black")

# Set chart's parameters
ax.set(xlim=(colonne_3_min, colonne_3_max), xticks=np.arange(1, colonne_3_max, 10),
       ylim=(colonne_5_min, colonne_5_max), yticks=np.arange(1, colonne_5_max, 20))

# Display the chart
plt.show()