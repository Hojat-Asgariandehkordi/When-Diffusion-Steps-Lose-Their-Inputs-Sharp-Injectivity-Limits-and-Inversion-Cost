"""Fig. 1: one saved Heun output, three compatible inputs (exact two-atom prior)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from scipy.optimize import brentq
import style, data
from common import tile, framed, save

style.apply()
C = style.COL
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

FH = 2.9
fig = plt.figure(figsize=(style.TEXTWIDTH_MAIN, FH))
# ---------------- (a) curves
ax = fig.add_axes([0.065, 0.385, 0.36, 0.52])
ax.plot(grid, H(grid), color=C["Heun1"], lw=1.8, zorder=3)
ax.plot(grid, P(grid), color=C["DPM++2S"], lw=1.8, zorder=3)
ax.axhline(data.FIG1_TARGET, color=C["ref"], lw=0.7, ls=(0, (4, 2)), zorder=1)
for lab, u in zip(labels, roots):
    col = style.ABC[lab]
    ax.plot([u, u], [0, H(u)], color=col, lw=0.6, ls=":", zorder=2)
    ax.scatter([u], [H(u)], s=22, color=col, edgecolor="white", lw=0.6, zorder=5)
    ax.scatter([u], [P(u)], s=22, color=col, edgecolor="white", lw=0.6, zorder=5)
    ax.text(u - (0.045 if lab == "A" else 0), H(u) + 0.075, lab, color=col, ha="center", va="bottom", fontsize=8.5, fontweight="bold")
ax.text(0.33, 1.47, "Heun1", color=C["Heun1"], fontsize=8.5, fontweight="bold", ha="left")
ax.text(0.98, 0.70, "DPM++2S", color=C["DPM++2S"], fontsize=8.5, fontweight="bold", ha="left")
ax.text(1.2, data.FIG1_TARGET + 0.035, "shared Heun output 1.25", color=C["muted"], fontsize=7.5,
        ha="center", va="bottom", style="italic")
ax.set_xlim(0, 2.1); ax.set_ylim(0, 1.62)
ax.set_xticks([0, 0.5, 1, 1.5, 2]); ax.set_yticks([0, 0.5, 1, 1.5])
ax.set_xlabel(r"Input coordinate $u$ on the line $c+uv$", labelpad=1.5)
ax.set_ylabel("Output coordinate", labelpad=2)
fig.text(0.008, 0.985, r"(a) Exact maps on one image line, noise $1\to1/4$", fontsize=9, fontweight="bold", va="top")

# ---------------- ratio bar
bx = fig.add_axes([0.065, 0.0, 0.36, 0.165]); bx.axis("off")
bx.set_xlim(0, 1); bx.set_ylim(-0.55, 1)
bx.add_patch(Rectangle((0, 0.42), 0.5, 0.2, color=C["Heun1"], lw=0))
bx.add_patch(Rectangle((0.5, 0.42), 0.5, 0.2, color=C["DPM++2S"], lw=0))
bx.plot([0.5, 0.5], [0.3, 0.75], color=C["ink"], lw=0.8)
bx.text(0.5, 0.25, r"$1/2$", ha="center", va="top", fontsize=7.5)
bx.text(0.2, 0.25, "collision possible", ha="center", va="top", color=C["Heun1"], fontsize=7.5)
bx.text(0.79, 0.25, "universally protected", ha="center", va="top", color=C["DPM++2S"], fontsize=7.5)
bx.text(0.0, 0.8, r"Heun substep ratio $\rho=b/a$", ha="left", va="bottom", fontsize=7.5, fontweight="bold")
bx.text(0.0, -0.3, r"Minimum protected Heun length from $a$ to $b$: $\lceil\log_2(a/b)\rceil$ substeps.", ha="left", va="top", fontsize=7.5, color=C["muted"])

# ---------------- (b) tiles
fig.text(0.50, 0.985, "(b) From input states to saved outputs", fontsize=9, fontweight="bold", va="top")
T = {k: tile("fig1", v, 32) for k, v in data.FIG1_TILES.items()}
TS = 0.62  # tile size, inches
w, h = TS / style.TEXTWIDTH_MAIN, TS / FH
xs = [0.655, 0.77, 0.885]
ytop, ymid, ybot = 0.64, 0.355, 0.075
row_lab = [("Source\nstates", ytop), ("Heun1\noutput", ymid), ("DPM++2S\noutputs", ybot)]
for txt, y in row_lab:
    col = C["Heun1"] if "Heun" in txt else C["DPM++2S"] if "DPM" in txt else C["ink"]
    fig.text(0.535, y + h / 2, txt, fontsize=8, fontweight="bold", color=col, va="center", ha="left")
axes_src = []
for lab, x, u in zip(labels, xs, roots):
    a1 = fig.add_axes([x, ytop, w, h]); framed(a1, T[f"{lab}_src"], style.ABC[lab]); axes_src.append(a1)
    fig.text(x + w / 2, ytop + h + 0.012, rf"{lab}:  $u={u:.3f}$", ha="center", va="bottom",
             fontsize=7.5, color=style.ABC[lab], fontweight="bold")
    a3 = fig.add_axes([x, ybot, w, h]); framed(a3, T[f"{lab}_dpm"], C["DPM++2S"])
    a3.text(0.5, -0.06, rf"$F={P(u):.3f}$", transform=a3.transAxes, ha="center", va="top",
            fontsize=7.5, color=C["DPM++2S"])
am = fig.add_axes([xs[1], ymid, w, h]); framed(am, T["heun"], C["Heun1"], lw=1.8)
fig.text(xs[2] + w / 2, ymid + h / 2, r"one output" "\n" r"$H=1.250$", ha="center", va="center",
         fontsize=7.5, color=C["Heun1"])
# converging arrows (figure coords)
tgt = (xs[1] + w / 2, ymid + h)
for x in xs:
    src = (x + w / 2, ytop)
    end = (tgt[0] + (x - xs[1]) * 0.25, tgt[1] + 0.004)
    fig.patches.append(FancyArrowPatch(src, end, transform=fig.transFigure, arrowstyle="-|>",
                                       mutation_scale=7, color=C["Heun1"], lw=0.9,
                                       shrinkA=1, shrinkB=1))
save(fig, "figure1")
print("roots", [round(r, 4) for r in roots], "dpm", [round(P(r), 4) for r in roots])
