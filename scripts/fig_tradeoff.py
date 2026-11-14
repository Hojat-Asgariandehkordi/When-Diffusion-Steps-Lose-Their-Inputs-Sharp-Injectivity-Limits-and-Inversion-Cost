"""Fig. 2 (one column): inverse work vs forward fidelity, one row per cohort.
Forward RMS on a log axis so the 95% seed-bootstrap intervals are visible."""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
import style, data
from common import save

style.apply()
C = style.COL
ARROW = "#3A3F44"
fig, axes = plt.subplots(3, 1, figsize=(style.COLWIDTH, 3.55), sharex=True,
                         gridspec_kw=dict(hspace=0.32))
fig.subplots_adjust(left=0.15, right=0.98, top=0.9, bottom=0.11)
# label offsets in points (dx, dy) per cohort and map, chosen to clear markers and bars
OFF = {
    "FFHQ64 VP": {"Heun1": (-7, 0, "right"), "DPM++2S": (7, 0, "left"), "Heun2": (7, -1, "left")},
    "CIFAR-10 VP": {"Heun1": (-7, 0, "right"), "DPM++2S": (7, 0, "left"), "Heun2": (7, 0, "left")},
    "CIFAR-10 VE": {"Heun1": (-7, 0, "right"), "DPM++2S": (7, 0, "left"), "Heun2": (-7, 0, "right")},
}
for ax, (name, d) in zip(axes, data.TRADEOFF.items()):
    rows = d["rows"]
    ax.axvline(d["cap"], color=C["ref"], lw=0.8, ls=(0, (3, 2)), zorder=1)
    ax.text(d["cap"] + (4 if d["cap"] < 300 else -4), 0.205, f"ceiling {d['cap']}", color=C["muted"],
            fontsize=7.8, va="top", ha="left" if d["cap"] < 300 else "right")
    if name == "FFHQ64 VP":
        (x1, y1, *_), (x2, y2, *_) = rows["DPM++2S"], rows["Heun2"]
        ax.add_patch(FancyArrowPatch((x1 + 6, y1 * 0.94), (x2 - 6, y2 * 1.07), arrowstyle="-|>",
                                     mutation_scale=6, color=ARROW, lw=0.7, ls=(0, (2.5, 1.5)), zorder=2))
    for m, (nf, flow, (lo, hi), rec) in rows.items():
        ax.errorbar(nf, flow, yerr=[[flow - lo], [hi - flow]], fmt=style.MARK[m], color=C[m], ms=3.6,
                    mfc="white", mew=1.0, elinewidth=1.1, capsize=3.2, capthick=1.0, zorder=4)
        dx, dy, ha = OFF[name][m]
        ax.annotate(rec, (nf, flow), xytext=(dx, dy), textcoords="offset points", fontsize=8,
                    color=C[m], ha=ha, va="center")
    ax.set_yscale("log"); ax.set_ylim(0.018, 0.21)
    ax.set_yticks([0.02, 0.05, 0.1]); ax.set_yticklabels(["0.02", "0.05", "0.10"])
    ax.minorticks_off()
    ax.set_xlim(0, 335); ax.set_xticks([0, 80, 160, 240, 320])
    ax.set_title(f"{name}, {d['note']}", fontsize=8.6, loc="left", pad=2)
axes[1].set_ylabel(r"mean forward RMS $e_{\rm flow}$ (log)")
axes[-1].set_xlabel("mean iterative denoiser forwards per clean target", labelpad=1)
handles = [Line2D([], [], marker=style.MARK[m], color=C[m], ls="none", ms=4, mfc="white", mew=1.0,
                  label=f"{m} ({data.CALLS_PER_MAP[m]} calls)") for m in data.CALLS_PER_MAP]
fig.legend(handles=handles, loc="upper center", ncol=3, bbox_to_anchor=(0.56, 1.005), handletextpad=0.2,
           columnspacing=0.9, fontsize=8)
save(fig, "tradeoff")
