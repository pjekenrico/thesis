import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "modern"
text_kwargs = dict(fontsize=12)


waveform_1 = np.loadtxt(
    "waveform_LMU.csv",
    delimiter=",",
    skiprows=0,
)
# Flow in ICA
waveform_1[:, 1] *= 0.39 * 60 / 1000

waveform_2 = np.loadtxt(
    "waveform_Cell.csv",
    delimiter=",",
    skiprows=0,
)
waveform_2[:, 1] *= 60 / 1000


mean_1 = int(np.mean(waveform_1[:, 1]))
mean_2 = int(np.mean(waveform_2[:, 1]))

plt.figure(figsize=(7, 3))
plt.plot(
    waveform_1[:, 0],
    waveform_1[:, 1],
    "k-",
    label=r"$\bar{Q}_1 =\,$" + f"{mean_1} ml/min",
)
plt.plot(
    waveform_2[:, 0],
    waveform_2[:, 1],
    "k--",
    label=r"$\bar{Q}_2 =\,$" + f"{mean_2} ml/min",
)
plt.legend()
plt.xlabel(r"$t$\,[s]", **text_kwargs)
plt.ylabel(r"$Q$\,[ml/min]", **text_kwargs)
plt.xlim([0, 0.95])
plt.ylim([100, 500])
plt.minorticks_on()
plt.grid(which="both", alpha=0.2)
plt.tight_layout()
plt.savefig("waveform_comparison.pdf")
plt.show()

print()
