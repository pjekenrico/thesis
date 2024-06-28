import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "modern"
text_kwargs = dict(fontsize=12)


full_data = np.loadtxt(
    "full.csv",
    delimiter=",",
    skiprows=1,
    usecols=(0, 1),
)

cut_data = np.loadtxt(
    "cut.csv",
    delimiter=",",
    skiprows=1,
    usecols=(0, 1),
)

T_end = 0.95
PI_full = (64.1167 - 16.9161) / 37.5429
PI_cut = (63.5877 - 17.1103) / 37.4279
t = np.linspace(0, T_end, len(full_data))

plt.figure(figsize=(7, 3))
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(
    t,
    full_data[:, 1],
    "k-",
    label=r"Full - PI $=$\," + f"{PI_full:.2f}",
)
ax2.plot(
    t,
    full_data[:, 0],
    "-",
    color="#aa0000",
)

ax1.plot(
    t,
    cut_data[:, 1],
    "k--",
    label=r"Cut - PI $=$\," + f"{PI_cut:.2f}",
)
ax2.plot(
    t,
    cut_data[:, 0],
    "--",
    color="#aa0000",
)

ax1.legend(loc="upper right")
ax1.set_xlabel(r"$t$\,[s]", **text_kwargs)
ax1.set_ylabel(r"$\bar{u}$\,[mm/s]", **text_kwargs)
ax2.set_ylabel(r"$p\,$[Pa]", color="#aa0000", **text_kwargs)
ax1.set_xlim([0, T_end])
ax1.set_ylim([0, 75])
ax1.set_yticks(np.linspace(0, 80, 5))
ax2.set_ylim([0, 8000])  # Adjust the limits according to your data
ax2.tick_params(axis="y", labelcolor="#aa0000")

ax1.minorticks_on()
ax2.minorticks_on()
ax1.grid(which="both", alpha=0.2)
plt.tight_layout()
plt.savefig("cut_full_comparison.pdf")
plt.show()

print()
