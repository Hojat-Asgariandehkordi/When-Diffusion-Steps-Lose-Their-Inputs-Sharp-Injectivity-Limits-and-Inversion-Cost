"""Fig. 3: inverse work vs forward fidelity for three cohorts."""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import style, data
from common import save

style.apply()
C = style.COL
fig, axes = plt.subplots(1, 3, figsize=(style.TEXTWIDTH_MAIN, 2.25), sharey=True,
                         gridspec_kw=dict(wspace=0.12))
offsets = {  # label placement (dx points, dy points, ha)
    "Heun1": (6, 2, "left"), "DPM++2S": (6, 3, "left"), "Heun2": (7, -5, "left")}
for ax, (name, d) in zip(axes, data.TRADEOFF.items()):
    rows = d["rows"]
    ax.axvline(d["cap"], color=C["ref"], lw=0.8, ls=(0, (3, 2)), zorder=1)
    ax.text(d["cap"] + 4, 0.131, f"AA ceiling {d['cap']}", color=C["muted"], fontsize=7, va="top", ha="left"
            if d["cap"] < 300 else "right", transform=ax.transData) if d["cap"] < 300 else \
        ax.text(d["cap"] - 4, 0.131, f"AA ceiling {d['cap']}", color=C["muted"], fontsize=7, va="top", ha="right")
    if name == "FFHQ64 VP":
        (x1, y1, *_), (x2, y2, *_) = rows["DPM++2S"], rows["Heun2"]
        ax.plot([x1, x2], [y1, y2], color="#9DB7C4", lw=1.0, zorder=2)
    for m, (nf, flow, (lo, hi), rec) in rows.items():
        ax.errorbar(nf, flow, yerr=[[flow - lo], [hi - flow]], fmt=style.MARK[m], color=C[m], ms=4.2,
                    mec="white", mew=0.5, elinewidth=0.9, capsize=3.0, capthick=0.9, zorder=4)
        dx, dy, ha = offsets[m]
        lab = rec
        if name == "FFHQ64 VP" and m != "Heun1":
            lab = f"{rec}\n{nf:.1f} / {flow:.4f}"
        ax.annotate(lab, (nf, flow), xytext=(dx, dy), textcoords="offset points", fontsize=7,
                    color=C[m], ha=ha, va="center", linespacing=1.05)
    ax.set_title(f"{name}  ({d['note']})", fontsize=8.5, fontweight="bold", loc="left", pad=3)
    ax.set_xlim(0, 335); ax.set_xticks([0, 80, 160, 240, 320])
    ax.set_ylim(0, 0.135); ax.set_yticks([0, 0.04, 0.08, 0.12])
axes[0].set_ylabel(r"Mean forward RMS $e_{\rm flow}$ vs. Heun128")
fig.subplots_adjust(bottom=0.28, top=0.9, left=0.07, right=0.99)
fig.text(0.53, 0.12, "Mean iterative denoiser forwards per clean target", ha="center", fontsize=8)
handles = [Line2D([], [], marker=style.MARK[m], color=C[m], ls="none", ms=5, mec="white", mew=0.5,
                  label=f"{m} ({data.CALLS_PER_MAP[m]} calls/map)") for m in data.CALLS_PER_MAP]
fig.legend(handles=handles, loc="lower center", ncol=3, bbox_to_anchor=(0.53, -0.04), handletextpad=0.3,
           columnspacing=2.0)
save(fig, "tradeoff")
