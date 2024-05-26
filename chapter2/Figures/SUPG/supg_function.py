import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "modern"
text_kwargs = dict(fontsize=14)

# Define the points
points = np.array([[0, 0], [1, 1], [2, 0]])
offset = 0.2  # Epsilon parameter for offset

# Plot the linear hat function
x = np.linspace(0, 2, 101)
y = np.piecewise(x, [x < 1, x >= 1], [lambda x: x, lambda x: -x + 2])
y_supg_1 = x[x <= 1] + offset
y_supg_2 = -x[x >= 1] + 2 - offset

# Calculate the slope of the function
slope = (y[1] - y[0]) / (x[1] - x[0])

# Calculate the intersection points
x_intersect_1 = points[0, 0] + offset / slope
x_intersect_2 = points[2, 0] - offset / slope

# Plot the points with offset
plt.plot(x, y, "k--", label="Galerkin test function")
plt.plot(x[x <= 1], y_supg_1, "k-", label="SUPG test function")
plt.plot([1, 1], [1 + offset, 1 - offset], "k-")
plt.plot(x[x >= 1], y_supg_2, "k-")

# Plot the partially opaque filled area
angle = np.arctan(slope) * 180 / np.pi
plt.text(
    0.5,
    0.5 + offset / 2,
    r"$ \varepsilon \propto |u|\Delta x$",
    horizontalalignment="center",
    verticalalignment="center",
    rotation=angle,
    **text_kwargs
)
plt.text(
    1.5,
    0.5 - offset / 2,
    r"$ \varepsilon \propto -|u|\Delta x$",
    horizontalalignment="center",
    verticalalignment="center",
    rotation=-angle,
    **text_kwargs
)

# Plot the partially opaque filled area
plt.fill_between(x[x <= 1], y[x <= 1], y_supg_1, color='lightgray', alpha=0.5)
plt.fill_between(x[x >= 1], y[x >= 1], y_supg_2, color='lightgray', alpha=0.5)

# Plot lines with the same angle as the function
plt.plot([points[0, 0], x_intersect_1], [points[0, 1], 0], "k-", linewidth=1)
plt.plot([points[2, 0], x_intersect_2], [points[2, 1], 0], "k-", linewidth=1)

# Plot the line at y=0 with markers
plt.axhline(y=0, color="black")
# Plot the vertical bars at y=0
plt.plot([0, 0], [0, -0.05], "k-", linewidth=1)
plt.plot([1, 1], [0, -0.05], "k-", linewidth=1)
plt.plot([2, 2], [0, -0.05], "k-", linewidth=1)

# Add arrow below x-axis with text
plt.annotate(
    "Positive x",
    xy=(0.9, -0.2), xytext=(1.1, -0.2),
    arrowprops=dict(facecolor='black', arrowstyle='->'),
    **text_kwargs
)

# Hide the axis
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.xticks([])  # Hide ticks on x-axis
plt.yticks([])  # Hide ticks on y-axis

plt.legend(**text_kwargs)
plt.axis('equal')
plt.tight_layout()
plt.show()
