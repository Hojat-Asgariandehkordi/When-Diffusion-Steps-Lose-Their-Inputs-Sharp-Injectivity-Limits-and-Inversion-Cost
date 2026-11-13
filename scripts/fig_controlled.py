"""Supplement: fixed-stage weight sweep (source RMS and iterative work vs w1)."""
import matplotlib.pyplot as plt
import style, data
from common import save

style.apply()
C = style.COL
cols = {r"$2\to1/8$": (C["DPM++2S"], "s", -0.09), r"$1\to1/16$": (C["Heun2"], "^", 0.09)}
xs = list(range(len(data.SWEEP_W1)))
labels = ["$-6.5625$", "$-0.5$", "$-0.125$", "$0$", "$0.125$", "$0.5$"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(style.TEXTWIDTH_SUPP, 2.15), gridspec_kw=dict(wspace=0.28))
for ax in (a1, a2):
    ax.axvspan(-0.5, 2.5, color="#F6E9E3", lw=0, zorder=0)
    ax.axvline(3, color=C["ref"], lw=0.6, zorder=1)
    ax.set_xticks(xs, labels); ax.set_xlim(-0.5, 5.5)
    ax.set_xlabel(r"First prediction weight $w_1$ (categorical axis)")
    ax.text(0.04, 0.03 if ax is a2 else 0.04, r"$w_1<0$", transform=ax.transAxes, color=C["Heun1"], fontsize=7.5)
for name, rows in data.SWEEP.items():
    col, mk, dx = cols[name]
    a1.plot([x + dx for x in xs], [r[1] for r in rows], marker=mk, color=col, lw=1.0, ms=4.2, mec="white",
            mew=0.4, label=name, zorder=3)
    a2.plot([x + dx for x in xs], [r[2] for r in rows], marker=mk, color=col, lw=1.0, ms=4.2, mec="white",
            mew=0.4, label=name, zorder=3)
rec = [r[0] for r in data.SWEEP[r"$2\to1/8$"]]
assert rec == [r[0] for r in data.SWEEP[r"$1\to1/16$"]]
for x, k in zip(xs, rec):
    y = 1.6 if k == 0 else 2.2e-4
    a1.text(x, y, f"{k}/{data.SWEEP_N}", ha="center", va="bottom", fontsize=7,
            color=C["Heun1"] if k == 0 else C["muted"])
a1.set_yscale("log"); a1.set_ylim(1e-5, 8)
a1.axhline(data.RECOVERY_THRESHOLD, color=C["ref"], lw=0.7, ls=(0, (4, 2)))
a1.text(5.45, data.RECOVERY_THRESHOLD * 1.25, r"recovery threshold $e_x=0.02$", ha="right", va="bottom",
        fontsize=7, color=C["muted"])
a1.set_ylabel(r"Mean source RMS $e_x$")
a1.set_title("Source error (labels: recovered / 12)", loc="left", fontweight="bold", pad=3)
a2.axhline(160, color=C["ref"], lw=0.7, ls=(0, (4, 2)))
a2.text(5.45, 162, "160-forward ceiling", ha="right", va="bottom", fontsize=7, color=C["muted"])
a2.set_ylim(0, 180); a2.set_ylabel(r"Mean iterative forwards $N_f$")
a2.set_title("Inverse work", loc="left", fontweight="bold", pad=3)
fig.subplots_adjust(bottom=0.3, top=0.9)
h, l = a1.get_legend_handles_labels()
fig.legend(h, ["Noise interval " + x for x in l], loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.01),
           columnspacing=2.5)
save(fig, "controlled")
