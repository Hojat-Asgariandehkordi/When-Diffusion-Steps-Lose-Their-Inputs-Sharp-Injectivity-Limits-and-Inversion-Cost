"""Fig. 4 (one column): clean-target failures vs iterative ceiling for three inverse procedures,
reused CIFAR-10 VP cohort (N=64), with exact binomial 95% intervals. Noisy arm: supplement."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.stats import beta
import style, data
from common import save

style.apply()
C = style.COL
N = data.CONTROLS_N


def cp(k, n, a=0.05):
    lo = 0.0 if k == 0 else beta.ppf(a / 2, k, n - k + 1)
    hi = 1.0 if k == n else beta.ppf(1 - a / 2, k + 1, n - k)
    return lo, hi


maps = ["Heun1", "Midpoint1", "Heun2", "Euler2", "DPM++2S"]
dx = dict(zip(maps, np.linspace(-0.2, 0.2, 5)))
titles = {"Anderson": "Anderson\n(AA)", "AA + L-BFGS": "AA +\nL-BFGS", "AA + Newton–GMRES": "AA +\nNewton–GMRES"}
fig, axes = plt.subplots(1, 3, figsize=(style.COLWIDTH, 2.2), sharey=True)
fig.subplots_adjust(left=0.13, right=0.99, top=0.7, bottom=0.18, wspace=0.1)
for ax, inv in zip(axes, data.CONTROLS["clean"]):
    for m in maps:
        ks = data.CONTROLS["clean"][inv][m]
        x = np.arange(3) + dx[m]
        p = 100 * np.array(ks) / N
        ci = np.array([cp(k, N) for k in ks]) * 100
        ax.errorbar(x, p, yerr=[p - ci[:, 0], ci[:, 1] - p], color=C[m], marker=style.MARK[m], ms=3.0,
                    mec="white", mew=0.3, lw=0.8, elinewidth=0.8, capsize=1.6, capthick=0.8, zorder=3)
    ax.set_ylim(-3, 100); ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_xticks(range(3), data.CEILINGS, fontsize=7.8); ax.set_xlim(-0.45, 2.45)
    ax.set_title(titles[inv], fontsize=8.2, fontweight="bold", pad=2, linespacing=1.0)
axes[0].set_ylabel("clean failures (%)", labelpad=1)
fig.text(0.56, 0.02, "iterative traversal ceiling (forward + backward)", ha="center", fontsize=8.4)
h = [Line2D([], [], color=C[m], marker=style.MARK[m], ms=3.6, mec="white", mew=0.3, lw=0.8, label=m)
     for m in maps]
fig.legend(handles=h, loc="upper center", ncol=5, bbox_to_anchor=(0.55, 1.0), columnspacing=0.7,
           handletextpad=0.2, handlelength=1.4, fontsize=7.9)
save(fig, "controls_main")
