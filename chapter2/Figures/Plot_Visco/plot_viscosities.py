import numpy as np
import matplotlib.pyplot as plt
from labelines import *
from matplotlib.ticker import ScalarFormatter

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "modern"
text_kwargs = dict(fontsize=11)


def casson_model(shear_rate, Htc, m=100):

    mu0 = 0.073 * Htc + 0.599
    tau_0 = 0.888 * Htc - 23.753

    mu = (
        np.sqrt(mu0) + np.sqrt(tau_0 * (1 - np.exp(-m * shear_rate)) / shear_rate)
    ) ** 2

    return mu


shear_rate = np.logspace(0, 3, 100)
mu = [
    casson_model(shear_rate, 36),
    casson_model(shear_rate, 43),
    casson_model(shear_rate, 50),
]

fig = plt.figure(figsize=(7.5, 4))
plt.plot(shear_rate, mu[0], "k", label=r"Htc=36%")
plt.plot(shear_rate, mu[1], "k", label=r"Htc=43%")
plt.plot(shear_rate, mu[2], "k", label=r"Htc=50%")
plt.plot(
    shear_rate,
    3.5145 * np.ones_like(shear_rate),
    "--",
    color="grey",
    label=r"G-W 45%",
)
plt.ylim([3, 50])
plt.vlines(
    [3, 600],
    3,
    50,
    "#aa0000",
    linestyles="dashed",
    alpha=0.75,
    label=r"Common shear-rate range",
)

plt.xscale("log")
plt.yscale("log")
labelLines(plt.gca().get_lines(), xvals=np.array([9, 40, 200, 25]), zorder=2.5)
plt.gca().xaxis.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.set_major_formatter(ScalarFormatter())
plt.xlabel(r"$\dot{\gamma}\,[s^{-1}]$", **text_kwargs)
plt.ylabel(r"$\mu\,[m \mathrm{Pa} \cdot s]$", **text_kwargs)
yticks = [3, 5, 10, 30, 50]
plt.yticks(yticks, yticks)
# plt.minorticks_on()
plt.grid(which="both", linestyle="--", linewidth=0.5, color="gray", alpha=0.5, zorder=0)

lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
lines = lines[-3:]
labels = [
    r"Mod. Casson",
    r"45\% glycerol/water solution",
    r"Common shear-rate range",
]
fig.legend(lines, labels, loc="upper center", ncol=3, **text_kwargs)
fig.subplots_adjust(right=0.932, left=0.07, wspace=0.375, bottom=0.14)
plt.savefig("casson_model.pdf")
plt.show()
