"""Supplement: failure percentages across inverse ceilings, with exact binomial 95% CIs."""
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


maps = ["Euler2", "Heun1", "Midpoint1", "DPM++2S", "Heun2"]
dx = dict(zip(maps, np.linspace(-0.16, 0.16, 5)))
fig, axes = plt.subplots(2, 3, figsize=(style.TEXTWIDTH_SUPP * 0.9, 3.25), sharex=True, sharey=True,
                         gridspec_kw=dict(hspace=0.16, wspace=0.08))
for i, arm in enumerate(["clean", "noisy"]):
    for j, inv in enumerate(data.CONTROLS[arm]):
        ax = axes[i, j]
        for m in maps:
            ks = data.CONTROLS[arm][inv][m]
            x = np.arange(3) + dx[m]
            p = 100 * np.array(ks) / N
            ci = np.array([cp(k, N) for k in ks]) * 100
            ax.errorbar(x, p, yerr=[p - ci[:, 0], ci[:, 1] - p], color=C[m], marker=style.MARK[m], ms=3.8,
                        mec="white", mew=0.4, lw=0.9, elinewidth=0.7, capsize=1.6, capthick=0.7, zorder=3)
        ax.set_ylim(-3, 100); ax.set_yticks([0, 25, 50, 75, 100])
        ax.set_xticks(range(3), data.CEILINGS); ax.set_xlim(-0.4, 2.4)
        if i == 0:
            ax.set_title(inv, fontweight="bold", pad=3)
    axes[i, 0].set_ylabel(f"{arm.capitalize()} failures (%)")
fig.text(0.54, 0.07, "Iterative traversal ceiling (forward + backward)", ha="center", fontsize=8)
fig.subplots_adjust(bottom=0.18, top=0.93, left=0.09, right=0.99)
h = [Line2D([], [], color=C[m], marker=style.MARK[m], ms=4, mec="white", mew=0.4, lw=0.9, label=m) for m in maps]
fig.legend(handles=h, loc="lower center", ncol=5, bbox_to_anchor=(0.54, -0.045), columnspacing=1.6)
save(fig, "controls")
