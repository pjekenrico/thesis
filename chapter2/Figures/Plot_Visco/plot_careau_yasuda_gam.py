import numpy as np
import matplotlib.pyplot as plt
from labelines import *

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "modern"
text_kwargs = dict(fontsize=11)

gamba_meas = np.array(
    [
        [0.05859453915069213, 0.4146716101694915],
        [0.27384196342643613, 0.2424170197740113],
        [1.2798022139979526, 0.113],
        [5.981164049731403, 0.060054731638418124],
        [27.953009456081922, 0.042037429378531166],
        [68.36304970929181, 0.03697722457627128],
        [95.9716269367921, 0.03690607344632779],
        [130.63857322002303, 0.03588453389830515],
        [669.7193655525426, 0.0335],
        [999.9999999999959, 0.033],
    ]
).T


def carreau_yasuda(shear_rate, mu_0=0.0456, mu_inf=0.0032, lam=10.03, n=0.344):
    mu = mu_inf + (mu_0 - mu_inf) * (1 + (lam * shear_rate) ** 2) ** ((n - 1) / 2)
    return mu * 1000


fig, ax = plt.subplots(figsize=(7.5, 3))
shear_rate = np.logspace(-2, 3, 100)
plt.plot(
    shear_rate,
    carreau_yasuda(shear_rate),
    "k",
    label=r"C-Y, Gambaruto\,\textit{et al.}\,(2011)",
)
plt.scatter(
    gamba_meas[0],
    gamba_meas[1] * 100,
    alpha=0.5,
    c="#aa0000",
    label=r"RBC\,+\,Plasma",
)

plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"$\dot{\gamma}\,[s^{-1}]$", **text_kwargs)
plt.ylabel(r"$\mu$\,[m $\mathrm{Pa} \cdot$ s]", **text_kwargs)
yticks = [2, 5, 10, 20, 50]
plt.yticks(yticks, yticks)
xticks = [0.01, 0.1, 1, 10, 100, 1000]
plt.xticks(xticks, xticks)
plt.xlim([0.01, 1000])
plt.ylim([2, 50])

plt.grid(
    which="both", linestyle="--", linewidth=0.5, color="gray", alpha=0.5, zorder=1.5
)
lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
fig.legend(
    lines, labels, loc="upper center", ncol=len(lines), framealpha=0, **text_kwargs
)
fig.subplots_adjust(right=0.975, left=0.086, wspace=0.375, bottom=0.155)
plt.savefig("carreau-yasuda_gambaruto.pdf")
plt.show()
