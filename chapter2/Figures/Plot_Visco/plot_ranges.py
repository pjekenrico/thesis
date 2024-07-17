import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "modern"
text_kwargs = dict(fontsize=11)


def carreau_yasuda(shear_rate):
    mu_0 = 0.0456
    mu_inf = 0.0032
    lam = 10.03
    n = 0.344
    mu = mu_inf + (mu_0 - mu_inf) * (1 + (lam * shear_rate) ** 2) ** ((n - 1) / 2)
    return mu * 1e3


def casson_model(shear_rate, Htc, m=100):

    mu0 = 0.073 * Htc + 0.599
    tau_0 = 0.888 * Htc - 23.753

    mu = (
        np.sqrt(mu0) + np.sqrt(tau_0 * (1 - np.exp(-m * shear_rate)) / shear_rate)
    ) ** 2

    return mu


shear_rate = np.logspace(-2, 4, 100)

ranges = [
    (np.min(shear_rate), 1, 0.1, "Below range"),
    (1, 10, 0.2, "Aneurysm shear rates"),
    (10, 600, 0.3, "Artery shear rates"),
    (600, np.max(shear_rate), 0.4, "Above range"),
]

fig, ax = plt.subplots(figsize=(7.5, 3))
plt.plot(shear_rate, casson_model(shear_rate, 35.6), "k", label=r"Modified Casson")
plt.plot(shear_rate, carreau_yasuda(shear_rate), "k--", label=r"Carreau-Yasuda")
plt.plot(
    shear_rate,
    3.2 * np.ones_like(shear_rate),
    "k-.",
    label=r"Newtonian",
)
plt.vlines(
    [1, 600],
    1,
    1000,
    "#aa0000",
    linestyles="dashed",
    alpha=0.75,
    label=r"Treated range",
)

# Add the opaque background fields and vertical text
for start, end, alpha, text in ranges:
    ax.axvspan(start, end, facecolor="#aa0000", alpha=alpha)
    ax.text(end * 0.95, 900, text, rotation=90, va="top", ha="right", **text_kwargs)

plt.xlim([np.min(shear_rate), np.max(shear_rate)])
plt.ylim([1, 1000])
plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"$\dot{\gamma}\,[s^{-1}]$", **text_kwargs)
plt.ylabel(r"$\mu\,[m \mathrm{Pa} \cdot s]$", **text_kwargs)
yticks = [1, 10, 100, 1000]
plt.yticks(yticks, yticks)
xticks = [0.01, 0.1, 1, 10, 100, 1000, 10000]
plt.xticks(xticks, xticks)

plt.grid(which="both", linestyle="--", linewidth=0.5, color="gray", alpha=0.5, zorder=0)

lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
lines = lines[:4]
labels = [
    r"Modified Casson",
    r"Carreau-Yasuda",
    r"Newtonian",
    r"Treated range",
]
fig.legend(lines, labels, loc="upper center", ncol=4, framealpha=0, **text_kwargs)
fig.subplots_adjust(right=0.975, left=0.086, wspace=0.375, bottom=0.155)
plt.savefig("ranges.pdf")
plt.show()
