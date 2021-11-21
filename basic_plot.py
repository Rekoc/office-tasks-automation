import matplotlib.pyplot as plt

# Create a figure containing a single axes.
fig, ax = plt.subplots()
# Plot some data on the axes.
ax.plot(
    [1, 2, 3, 4, 5, 6, 7],
    [7, 6, 2, 5, 7, 3, 4]
)
# Display the chart
plt.show()