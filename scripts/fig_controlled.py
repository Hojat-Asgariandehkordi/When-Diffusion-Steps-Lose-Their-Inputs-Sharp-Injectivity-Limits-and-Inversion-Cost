"""Fig. 3 (one column): fixed-stage weight sweep. w2 = 15/16 - w1, stage held fixed.
(a) source error, (b) inverse work, (c) forward fidelity, (d) smallest random directional gain."""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import style, data
from common import save

style.apply()
C = style.COL
IV = {r"$2\to1/8$": ("#2B2F33", "s", -0.1), r"$1\to1/16$": ("#8A949D", "^", 0.1)}
xs = list(range(len(data.SWEEP_W1)))
xl = ["$-6.56$", "$-1/2$", "$-1/8$", "$0$", "$1/8$", "$1/2$"]
fig, axs = plt.subplots(2, 2, figsize=(style.COLWIDTH, 2.95), sharex=True)
fig.subplots_adjust(left=0.13, right=0.985, top=0.86, bottom=0.12, wspace=0.42, hspace=0.36)
(a, b), (c, d) = axs
panels = [
    (a, lambda i, k: data.SWEEP[k][i][1], r"source RMS $e_x$", True),
    (b, lambda i, k: data.SWEEP[k][i][2], r"inverse forwards $N_f$", False),
    (c, lambda i, k: data.SWEEP_EXTRA[k][i][0], r"forward RMS $e_{\rm flow}$", True),
    (d, lambda i, k: data.SWEEP_EXTRA[k][i][1], r"min. gain $g_{\rm rand}$", False),
]
for (ax, get, lab, logy), tag in zip(panels, "abcd"):
    ax.axvspan(-0.5, 2.5, color="#F6E9E3", lw=0, zorder=0)
    ax.axvline(3, color=C["ref"], lw=0.6, zorder=1)
    for k, (col, mk, dx) in IV.items():
        ax.plot([x + dx for x in xs], [get(i, k) for i in xs], marker=mk, color=col, lw=0.9, ms=3.4,
                mec="white", mew=0.4, zorder=3)
    if logy:
        ax.set_yscale("log")
    ax.set_ylabel(lab, labelpad=1)
    ax.text(-0.3, 1.04, f"({tag})", transform=ax.transAxes, fontsize=8.8, fontweight="bold", va="bottom")
    ax.set_xticks(xs, xl, rotation=45, fontsize=7.6)
    ax.tick_params(axis="y", labelsize=7.8)
    ax.set_xlim(-0.5, 5.5)
a.set_ylim(1e-5, 3); a.axhline(data.RECOVERY_THRESHOLD, color=C["ref"], lw=0.7, ls=(0, (3, 2)))
a.minorticks_off(); a.set_yticks([1e-5, 1e-3, 1e-1])
b.axhline(160, color=C["ref"], lw=0.7, ls=(0, (3, 2))); b.set_ylim(0, 175); b.set_yticks([0, 80, 160])
c.minorticks_off(); c.set_ylim(0.02, 0.25); c.set_yticks([0.02, 0.05, 0.1, 0.2]); c.set_yticklabels(["0.02", "0.05", "0.1", "0.2"])
d.set_ylim(0.05, 0.28)
# recovered counts as an axis strip above panel (a), outside the data region
rec = [r[0] for r in data.SWEEP[r"$2\to1/8$"]]
for x, k in zip(xs, rec):
    a.text(x, 1.02, f"{k}", transform=a.get_xaxis_transform(), ha="center", va="bottom", fontsize=7.5,
           color=C["Heun1"] if k == 0 else C["muted"])
for ax in (c, d):
    ax.set_xlabel(r"first weight $w_1$", labelpad=1)
h = [Line2D([], [], color=col, marker=mk, ms=3.6, lw=0.9, mec="white", mew=0.4, label=k)
     for k, (col, mk, _) in IV.items()]
fig.legend(handles=h, loc="upper center", ncol=2, bbox_to_anchor=(0.55, 1.0), columnspacing=1.5,
           fontsize=8, title=None)
save(fig, "controlled")
