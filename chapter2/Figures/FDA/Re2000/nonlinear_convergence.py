import re
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from labelines import *
from matplotlib.ticker import NullLocator


text_kwargs = dict(fontsize=12)


def extract_initial_residuals(logfile):
    residuals = defaultdict(list)
    current_timestep = None

    with open(logfile, "r") as file:
        for line in file:
            # Match and update the current timestep
            timestep_match = re.search(r"Increment de CompteurTemps\s*:\s*(\d+)", line)
            if timestep_match:
                current_timestep = int(timestep_match.group(1))
                continue

            # Extract the initial residual for the current timestep
            if "Initial Residual" in line and current_timestep is not None:
                residual_match = re.search(
                    r"Initial Residual\s*:\s*([\d\.e\+\-]+)", line
                )
                if residual_match:
                    residuals[current_timestep].append(float(residual_match.group(1)))

    residuals = {k: np.array(v) for k, v in residuals.items()}
    return residuals


def compute_convergence_orders(residuals):
    convergence_orders = {}
    for timestep, residuals_array in residuals.items():
        if len(residuals_array) > 1:  # Need at least two points to fit
            p = np.mean(np.log10(residuals_array[1:] / residuals_array[:-1]))
            convergence_orders[timestep] = -p
        else:
            convergence_orders[timestep] = None  # Not enough data to fit
    return convergence_orders


logfile = "out_Re2000.log"  # Replace this with your log file name
residuals = extract_initial_residuals(logfile)
convergence_orders = compute_convergence_orders(residuals)

for timestep, residual_list in sorted(residuals.items()):
    print(f"Timestep {timestep}:")
    for i, residual in enumerate(residual_list, start=1):
        print(f"  Subiteration {i}: {residual}")
    if convergence_orders[timestep] is not None:
        print(f"  Convergence order: {convergence_orders[timestep]:.4f}")
    else:
        print("  Convergence order: Not enough data to compute")


fig, ax = plt.subplots(ncols=2, figsize=(8, 3.5))

# Plot convergence orders
for timestep, residual_list in sorted(residuals.items()):
    if convergence_orders[timestep] is not None:
        ax[1].plot(timestep, convergence_orders[timestep], "k.", markersize=2)

# Plot residuals
for k, residual in enumerate(list(residuals.values())):
    if k > 0 and k % 10 == 0:
        ax[0].semilogy(residual, "k-", alpha=0.05, zorder=2)

# Set labels and limits for the first plot
ax[0].set_xlabel(r"Subiteration", **text_kwargs)
ax[0].set_ylabel(r"Residual", **text_kwargs)
ax[0].set_xlim(0, 10)
ax[0].set_ylim(1e-7, 1e5)
ax[0].minorticks_on()
ax[0].grid(
    which="both", linestyle="--", linewidth=0.5, color="gray", alpha=0.5, zorder=1.5
)
ax[0].set_xticks(np.arange(0, 11, 1))  # Set integer ticks on the x-axis

# Add reference curves with slopes 3 and 4
x = np.linspace(1, 10, 100)
y3 = 10 ** (-1 * (x - 1) + 6)
y4 = 10 ** (-2 * (x - 1) + 9)
y5 = 10 ** (-4 * (x - 1) + -1)
slope_3 = ax[0].plot(x, y3, color="#aa0000", label=r"1", zorder=0.5)
slope_4 = ax[0].plot(x - 1, y4, color="#aa0000", label=r"2", zorder=0.5)
slope_5 = ax[0].plot(x - 1, y5, color="#aa0000", label=r"4", zorder=0.5)

# Set labels and limits for the second plot
ax[1].set_xlabel(r"Iteration", **text_kwargs)
ax[1].set_ylabel(r"Convergence order", **text_kwargs)
ax[1].set_xlim(0, len(list(residuals.values())))
ax[1].set_ylim(0, 6)
ax[1].minorticks_on()
ax[1].grid(
    which="both", linestyle="--", linewidth=0.5, color="gray", alpha=0.5, zorder=1.5
)

ax[1].vlines(
    [2000, 5000],
    0,
    6,
    "#aa0000",
    linestyles="dashed",
    alpha=0.75,
    label=r"Treated range",
)


offset = 50
# Add the opaque background fields and vertical text
start, end, alpha, text = [0, 2000, 0.1, "Developing flow "]
ax[1].axvspan(start, end, facecolor="#aa0000", alpha=alpha)
ax[1].text(
    start + 2 * offset, 5.95, text, rotation=90, va="top", ha="left", **text_kwargs
)
ax[1].text(
    end - offset,
    5.95,
    "Jet hits outlet",
    rotation=90,
    va="top",
    ha="right",
    **text_kwargs,
)

start, end, alpha, text = [2000, 5000, 0.3, "Reentering flow"]
ax[1].axvspan(start, end, facecolor="#aa0000", alpha=alpha)
ax[1].text(
    start + 2 * offset, 5.95, text, rotation=90, va="top", ha="left", **text_kwargs
)
ax[1].text(
    end - offset / 2,
    5.95,
    "Stabilization",
    rotation=90,
    va="top",
    ha="right",
    **text_kwargs,
)

start, end, alpha, text = [
    5000,
    7500,
    0.1,
    "Towards steady-state",
]
ax[1].axvspan(start, end, facecolor="#aa0000", alpha=alpha)
ax[1].text(
    end - 2 * offset, 0.05, text, rotation=90, va="bottom", ha="right", **text_kwargs
)


ax[0].xaxis.set_minor_locator(NullLocator())

labelLines(slope_3 + slope_4 + slope_5, xvals=np.array([6.5, 4, 1]), zorder=0.5)
plt.tight_layout()
plt.savefig("nonlinear_convergence.pdf", bbox_inches="tight")
plt.show()
