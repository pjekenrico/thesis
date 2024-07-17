import numpy as np
import matplotlib.pyplot as plt
from labelines import *

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "modern"
text_kwargs = dict(fontsize=11)

# Whole Blood (Chien 1970)
whole_blood = np.array(
    [
        [0.010873663448830376, 183.06698253941224],
        [0.020391581407372315, 158.58863930582206],
        [0.05207668779653065, 111.35910804972181],
        [0.1024665868289747, 76.00651956109354],
        [0.19921339577476285, 54.4106846630952],
        [0.49118398736100044, 32.490555015548516],
        [1.0134985391654492, 21.345286696888845],
        [1.9244827299585137, 14.569340325075569],
        [5.033241777322772, 9.847406086942673],
        [10.138618464200459, 7.39343700575972],
        [20.417527805575748, 6.10631018954675],
        [45.207615730489934, 5.091175015939907],
        [102.50382112428173, 4.164540323248402],
        [187.69948749022768, 3.783917229949994],
        [396.1997983249697, 3.640070410721601],
    ]
).T

# Whole Serum (Chien 1970)
serum = np.array(
    [
        [0.01, 17.539317548690274],
        [0.019558112096932454, 17.36299165420171],
        [0.04874411413696429, 15.923151693665918],
        [0.09696759795306831, 15.318580077896533],
        [0.19520507113517466, 14.596977206340194],
        [0.46954905067884445, 12.885967062469668],
        [0.9452472555170419, 12.278955786765625],
        [1.902686508337919, 12.155393891396384],
        [4.743174487761368, 10.133641982323583],
        [9.552216084309368, 8.290051837252802],
        [19.00893781817537, 6.978716992917471],
        [45.198738465086166, 5.494705131761565],
        [93.19116567999356, 4.851252912537643],
        [183.25132811150053, 4.202414712985309],
        [391.51065529189583, 3.710185638521836],
    ]
).T

selected_data = np.array(
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
# plt.plot(
#     shear_rate,
#     carreau_yasuda(shear_rate, mu_0=0.195, mu_inf=0.0033, lam=43, n=0.37),
#     "k",
#     label=r"C-Y, Chien\,\textit{et al.}\,(1970)",
#     zorder=0.5,
# )
plt.scatter(
    whole_blood[0],
    whole_blood[1],
    alpha=0.5,
    c="#aa0000",
    label=r"RBC\,+\,Plasma",
)
plt.scatter(
    *serum,
    alpha=0.25,
    c="#aa0000",
    label=r"\hspace{-1cm}RBC\,+\,albumin-Ringer",
)


plt.xscale("log")
plt.yscale("log")
plt.xlabel(r"$\dot{\gamma}\,[s^{-1}]$", **text_kwargs)
plt.ylabel(r"$\mu$\,[m $\mathrm{Pa} \cdot$ s]", **text_kwargs)
yticks = [2, 5, 10, 20, 50, 100, 200, 500]
plt.yticks(yticks, yticks)
xticks = [0.01, 0.1, 1, 10, 100, 1000]
plt.xticks(xticks, xticks)
plt.xlim([0.01, 1000])
plt.ylim([2, 500])

plt.grid(
    which="both", linestyle="--", linewidth=0.5, color="gray", alpha=0.5, zorder=1.5
)
lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
fig.legend(
    lines, labels, loc="upper center", ncol=len(lines), framealpha=0, **text_kwargs
)
fig.subplots_adjust(right=0.975, left=0.086, wspace=0.375, bottom=0.155)
plt.savefig("carreau-yasuda_chien.pdf")
plt.show()
