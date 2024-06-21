import numpy as np
import matplotlib.pyplot as plt
from TensorMetric3D import pretty_axes


def plot_tria(m, ax):
    # Plot the triangle
    ax.plot(
        [m[0, 0], m[1, 0], m[2, 0], m[0, 0]],
        [m[0, 1], m[1, 1], m[2, 1], m[0, 1]],
        color="#aa0000",
        linewidth=2,
    )  # Blue line with width 2

    # Set equal aspect ratio and grid
    ax.set_aspect("equal")

    return


def plot_eigenvals_eigenvecs(eigvals, eigvecs, ctr, ax):
    # Origin point
    origin = np.array(ctr)

    # Scaled eigenvectors
    vec1 = eigvals[0] * eigvecs[:, 0]
    vec2 = eigvals[1] * eigvecs[:, 1]

    # Plot the arrows for the eigenvectors
    ax.quiver(
        *origin,
        *vec1,
        color="#00007f",
        scale=1,
        scale_units="xy",
        angles="xy",
        width=0.005,
        label=r"$\tilde\lambda_1$" + f": {eigvals[0]:.2f}"
    )
    ax.quiver(
        *origin,
        *vec2,
        color="#005500",
        scale=1,
        scale_units="xy",
        angles="xy",
        width=0.005,
        label=r"$\tilde\lambda_2$" + f": {eigvals[1]:.2f}"
    )
    ax.set_aspect("equal")
    # Add a legend
    ax.legend(loc="upper center", ncol=2)

    return


fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(7, 5))

h = np.sqrt(3)
r = h / np.sqrt(3)
an = np.pi * np.array([1 / 2, 7 / 6, 11 / 6])
X = np.array([r * np.cos(an), r * np.sin(an)]).T

M = X.T.dot(X)
eigvals, eigvecs = np.linalg.eigh(M)
eigvals = np.sqrt(2 * eigvals / 3)
M_scaled_1 = eigvecs.dot(np.diagflat(eigvals)).dot(eigvecs.T)


an = np.linspace(0, 2 * np.pi, 100)
x, y = M_scaled_1.dot(np.array([np.cos(an), np.sin(an)]))
plot_tria(X, ax[0])
ax[0].plot(x, y, color="k", linewidth=0.5)

plot_eigenvals_eigenvecs(eigvals, eigvecs, [0, 0], ax[0])

X_1 = np.array([[1.0, 2.0], [1.8, 1.0], [2.2, 3.4]])
X_1 -= np.mean(X_1, axis=0)
M_1 = X_1.T.dot(X_1)
eigvals, eigvecs = np.linalg.eig(M_1)

eigvals = np.sqrt(2 * eigvals / 3)
M_scaled_1 = eigvecs.dot(np.diagflat(eigvals)).dot(eigvecs.T)
x, y = M_scaled_1.dot(np.array([np.cos(an), np.sin(an)]))

plot_tria(X_1, ax[1])
ax[1].plot(x, y, color="k", linewidth=0.5)

plot_eigenvals_eigenvecs(eigvals, eigvecs, [0, 0], ax[1])


# X_2 = np.array([[1.0, 0.5], [0.5, 0.0], [1.0, 0.0]])
# X_2 -= np.mean(X_2, axis=0)
# M_2 = X_2.T.dot(X_2)
# eigvals, eigvecs = np.linalg.eigh(M_2)
# M_scaled_2 = eigvecs.dot(np.diagflat(np.sqrt(2 * eigvals))).dot(eigvecs.T)
# x, y = M_scaled_2.dot(np.array([r * np.cos(an), r * np.sin(an)]))
# plot_tria(X_2, ax[2])
# ax[2].plot(x, y)
# plot_eigenvals_eigenvecs(eigvals, eigvecs, [0, 0], ax[2])


pretty_axes(ax[0])
pretty_axes(ax[1])
# pretty_axes(ax[2])
ax[0].set_xlim(-1.25, 1.25)
ax[0].set_ylim(-1.5, 2)
plt.tight_layout()
plt.show()


print(M)
