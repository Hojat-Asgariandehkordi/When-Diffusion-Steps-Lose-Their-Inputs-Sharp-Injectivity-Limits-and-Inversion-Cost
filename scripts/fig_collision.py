"""Fig. 1 (one column): one saved Heun output, three compatible inputs (exact two-atom prior)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from scipy.optimize import brentq
import style, data
from common import tile, framed, save

style.apply()
C = style.COL
ARROW = "#3A3F44"          # arrows are neutral, never a data colour
rho = data.FIG1_RHO


def D(u, s):
    return np.tanh(u / s ** 2)


def step(u, q, kappa, w1, w2, a=1.0):
    p = q * u + (1 - q) * D(u, a)
    return rho * u + w1 * D(u, a) + w2 * D(p, kappa * a)


heun = dict(q=rho, kappa=rho, w1=(1 - rho) * (2 * rho - 1) / (2 * rho), w2=(1 - rho) / (2 * rho))
dpm = dict(q=np.sqrt(rho), kappa=np.sqrt(rho), w1=0.0, w2=1 - rho)
H = lambda u: step(u, **heun)
P = lambda u: step(u, **dpm)

grid = np.linspace(0.0, 2.1, 4001)
hv = H(grid) - data.FIG1_TARGET
idx = np.where(np.sign(hv[:-1]) != np.sign(hv[1:]))[0]
roots = [brentq(lambda t: H(t) - data.FIG1_TARGET, grid[i], grid[i + 1]) for i in idx]
assert len(roots) == 3, roots
labels = "ABC"

W, FH = style.COLWIDTH, 4.0
fig = plt.figure(figsize=(W, FH))
fx = lambda inch: inch / W
fy = lambda inch: inch / FH

# ---------------- (a) exact maps on one line
ax = fig.add_axes([fx(0.42), fy(2.38), fx(2.78), fy(1.45)])
ax.plot(grid, H(grid), color=C["Heun1"], lw=1.6, zorder=3)
ax.plot(grid, P(grid), color=C["DPM++2S"], lw=1.6, zorder=3)
ax.axhline(data.FIG1_TARGET, color=C["ref"], lw=0.7, ls=(0, (4, 2)), zorder=1)
for lab, u in zip(labels, roots):
    col = style.ABC[lab]
    ax.plot([u, u], [0, H(u)], color=col, lw=0.6, ls=":", zorder=2)
    for yv in (H(u), P(u)):
        ax.scatter([u], [yv], s=18, color=col, edgecolor="white", lw=0.5, zorder=5)
    ax.text(u + {"A": -0.055, "B": 0.0, "C": -0.06}[lab], H(u) + 0.07, lab, color=col, ha="center", va="bottom",
            fontsize=9, fontweight="bold")
ax.text(0.62, 1.47, "Heun1", color=C["Heun1"], fontsize=8.8, fontweight="bold", ha="left")
ax.text(1.02, 0.72, "DPM++2S", color=C["DPM++2S"], fontsize=8.8, fontweight="bold", ha="left")
ax.text(1.42, data.FIG1_TARGET + 0.03, "shared output 1.25", color=C["muted"], fontsize=8,
        ha="center", va="bottom", style="italic")
ax.set_xlim(0, 2.1); ax.set_ylim(0, 1.66)
ax.set_xticks([0, 0.5, 1, 1.5, 2]); ax.set_yticks([0, 0.5, 1, 1.5])
ax.set_xlabel(r"input coordinate $u$ on the line $c+uv$", labelpad=1)
ax.set_ylabel("output coordinate", labelpad=2)
fig.text(fx(0.02), fy(3.97), "(a)", fontsize=9, fontweight="bold", va="top")

# ---------------- (b) tiles
fig.text(fx(0.02), fy(1.92), "(b)", fontsize=9, fontweight="bold", va="top")
T = {k: tile("fig1", v, 32) for k, v in data.FIG1_TILES.items()}
ts = 0.47
xs = [1.06, 1.68, 2.30]
ytop, ymid, ybot = 1.3, 0.72, 0.14
for txt, y, col in [("sources", ytop, C["ink"]), ("Heun1\noutput", ymid, C["Heun1"]),
                    ("DPM++2S\noutputs", ybot, C["DPM++2S"])]:
    fig.text(fx(0.3), fy(y + ts / 2), txt, fontsize=8.4, fontweight="bold", color=col, va="center",
             ha="left", linespacing=1.0)
for lab, x, u in zip(labels, xs, roots):
    a1 = fig.add_axes([fx(x), fy(ytop), fx(ts), fy(ts)]); framed(a1, T[f"{lab}_src"], style.ABC[lab], 1.2)
    fig.text(fx(x + ts / 2), fy(ytop + ts + 0.03), rf"{lab}: $u={u:.3f}$", ha="center", va="bottom",
             fontsize=8, color=style.ABC[lab])
    a3 = fig.add_axes([fx(x), fy(ybot), fx(ts), fy(ts)]); framed(a3, T[f"{lab}_dpm"], C["DPM++2S"], 1.2)
    fig.text(fx(x + ts / 2), fy(ybot - 0.03), rf"$F={P(u):.3f}$", ha="center", va="top", fontsize=8,
             color=C["DPM++2S"])
am = fig.add_axes([fx(xs[1]), fy(ymid), fx(ts), fy(ts)]); framed(am, T["heun"], C["Heun1"], 1.6)
fig.text(fx(xs[2] + 0.02), fy(ymid + ts / 2), r"$H=1.250$" "\nfor A, B, C", ha="left", va="center",
         fontsize=8, color=C["Heun1"], linespacing=1.1)
for x in xs:
    src = (fx(x + ts / 2), fy(ytop - 0.01))
    dst = (fx(xs[1] + ts / 2 + (x - xs[1]) * 0.3), fy(ymid + ts + 0.01))
    fig.patches.append(FancyArrowPatch(src, dst, transform=fig.transFigure, arrowstyle="-|>",
                                       mutation_scale=6, color=ARROW, lw=0.7, shrinkA=0, shrinkB=0))
save(fig, "figure1")
print("roots", [round(r, 4) for r in roots], "dpm", [round(float(P(r)), 4) for r in roots])
