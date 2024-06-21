import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import meshio

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "modern"
text_kwargs = dict(fontsize=12)


def plot_tetra(m, ax):

    lines = combinations(m, 2)
    for x in lines:
        line = np.transpose(np.array(x))
        ax.plot3D(line[0], line[1], line[2], color="#aa0000", linewidth=2.5)

    # ax.plot_trisurf(x, y, z)
    x, y, z = m[:, 0], m[:, 1], m[:, 2]
    bbox_min = np.min([x, y, z])
    bbox_max = np.max([x, y, z])
    ax.auto_scale_xyz([bbox_min, bbox_max], [bbox_min, bbox_max], [bbox_min, bbox_max])
    ax.set_aspect("equal")


def pretty_axes(ax):
    # Customize the grid
    ax.grid(True, linestyle="--", color="gray", linewidth=0.5)

    if hasattr(ax, "zaxis"):
        # This is a 3D plot
        ax.xaxis.set_pane_color(
            (0.9, 0.9, 0.9, 0.5)
        )  # light grey with some transparency
        ax.yaxis.set_pane_color((0.9, 0.9, 0.9, 0.5))
        ax.zaxis.set_pane_color((0.9, 0.9, 0.9, 0.5))

        # Customize the axis lines and ticks for 3D
        ax.xaxis._axinfo["grid"].update(color="k", linestyle="--", linewidth=0.5)
        ax.yaxis._axinfo["grid"].update(color="k", linestyle="--", linewidth=0.5)
        ax.zaxis._axinfo["grid"].update(color="k", linestyle="--", linewidth=0.5)

        # Customize axis labels
        ax.set_xlabel("x", fontsize=12, labelpad=10)
        ax.set_ylabel("y", fontsize=12, labelpad=10)
        ax.set_zlabel("z", fontsize=12, labelpad=10)

        # Customize ticks for 3D
        ax.tick_params(axis="x", colors="black", direction="in", length=5, width=1)
        ax.tick_params(axis="y", colors="black", direction="in", length=5, width=1)
        ax.tick_params(axis="z", colors="black", direction="in", length=5, width=1)
    else:
        # This is a 2D plot
        ax.set_facecolor(
            (0.9, 0.9, 0.9, 0.5)
        )  # light grey background with some transparency

        # Customize axis labels
        ax.set_xlabel("x", fontsize=12, labelpad=10)
        ax.set_ylabel("y", fontsize=12, labelpad=10)

        # Customize ticks for 2D
        ax.tick_params(axis="x", colors="black", direction="in", length=5, width=1)
        ax.tick_params(axis="y", colors="black", direction="in", length=5, width=1)


def old_main():
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(121, projection="3d")

    r = 1
    theta = np.pi * np.array([0, 2 / 3, 4 / 3, 0])
    phi = np.array([np.arccos(-1 / 3), np.arccos(-1 / 3), np.arccos(-1 / 3), 0])
    X = np.array(
        [
            r * np.cos(theta) * np.sin(phi),
            r * np.sin(theta) * np.sin(phi),
            r * np.cos(phi),
        ]
    ).T

    plot_tetra(X, ax)
    # draw sphere
    u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    ax.plot_surface(x, y, z, color="w", edgecolor="k", alpha=0.2, linewidth=0.25)
    pretty_axes(ax)
    elev = ax.elev
    azim = ax.azim

    ax = fig.add_subplot(122, projection="3d")
    X = np.array([[0.0, 0.0, 0.0], [0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]])
    X -= np.mean(X, axis=0)
    plot_tetra(X, ax)
    M = X.T.dot(X)
    eigvals, eigvecs = np.linalg.eigh(M)
    M_scaled_2 = eigvecs.dot(np.diagflat(np.sqrt(3 / 4 * eigvals))).dot(eigvecs.T)
    x, y, z = M_scaled_2.dot(np.array([x.flatten(), y.flatten(), z.flatten()]))
    x = x.reshape(20, 10)
    y = y.reshape(20, 10)
    z = z.reshape(20, 10)
    ax.plot_surface(x, y, z, color="w", edgecolor="k", alpha=0.2, linewidth=0.25)
    # scaling hack
    bbox_min = np.min([x, y, z])
    bbox_max = np.max([x, y, z])
    ax.auto_scale_xyz([bbox_min, bbox_max], [bbox_min, bbox_max], [bbox_min, bbox_max])
    ax.set_aspect("equal")
    pretty_axes(ax)
    ax.view_init(elev=elev, azim=azim)

    plt.tight_layout()
    plt.show()
    print(M)


if __name__ == "__main__":
    old_main()
