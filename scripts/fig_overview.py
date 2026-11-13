"""Overview figure: problem -> sign test -> consequence for schedules and learned models.
All quantities are taken from the paper (Thm. 1, Cor. 1, Tab. coeff, Tab. recovery)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import style, data
from common import tile, framed, save

style.apply()
C = style.COL
W, H = style.TEXTWIDTH_MAIN, 2.35
fig = plt.figure(figsize=(W, H))
L = fig.add_axes([0, 0, 1, 1]); L.set_xlim(0, W); L.set_ylim(0, H); L.axis("off")


def box(x, y, w, h, fc="#F7F8F9", ec="#C9CED3", r=0.06):
    L.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=0.7))


def arrow(p, q, col=C["ink"], lw=0.9, ms=7, ls="-", rad=0.0):
    L.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms, color=col, lw=lw, ls=ls,
                                connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))


def head(x, y, s):
    L.text(x, y, s, fontsize=8.5, fontweight="bold", va="top", ha="left")


# ------------------------------------------------------------------ (a) problem
box(0.02, 0.05, 2.08, 2.22)
head(0.1, 2.2, "(a) Output-only recovery")
T = {k: tile("fig1", v, 32) for k, v in data.FIG1_TILES.items()}
ts = 0.52
ax = fig.add_axes([0.16 / W, 1.08 / H, ts / W, ts / H]); framed(ax, T["B_src"], C["ink"], 1.0)
ax = fig.add_axes([1.42 / W, 1.08 / H, ts / W, ts / H]); framed(ax, T["B_dpm"], C["DPM++2S"], 1.2)
L.text(0.16 + ts / 2, 1.0, r"input $x$ at noise $a$", ha="center", va="top", fontsize=7.5)
L.text(1.42 + ts / 2, 1.0, r"saved $y=F_a(x)$ at $b$", ha="center", va="top", fontsize=7.5)
arrow((0.72, 1.40), (1.38, 1.40), C["ink"], lw=1.1)
L.text(1.05, 1.47, r"step $F_a$", ha="center", va="bottom", fontsize=7.5)
L.text(1.05, 1.28, "2 denoiser\ncalls", ha="center", va="top", fontsize=6.8, color=C["muted"], linespacing=1.0)
arrow((1.68, 1.04 - 0.30), (0.42, 1.04 - 0.30), C["Heun1"], lw=0.9, ls=(0, (3, 2)), rad=-0.25)
L.text(1.05, 0.42, r"inverse sees only $y$, $F_a$ and the schedule:" "\n" r"is $x$ the unique source of $y$?",
       ha="center", va="top", fontsize=7.3, color=C["Heun1"], linespacing=1.15)

# ------------------------------------------------------------------ (b) sign test
box(2.2, 0.05, 2.25, 2.22)
head(2.28, 2.2, "(b) Sign test on the two weights")
L.text(3.325, 1.88, r"$F_a(x)=r\,x+w_1D_a(x)+w_2D_{\kappa a}(p_a(x))$", ha="center", va="top", fontsize=7.8)
u = np.linspace(-0.05, 2.1, 400)
rho = data.FIG1_RHO
D = lambda v, s: np.tanh(v / s ** 2)
def stp(v, q, k, w1, w2):
    p = q * v + (1 - q) * D(v, 1.0); return rho * v + w1 * D(v, 1.0) + w2 * D(p, k)
hh = stp(u, rho, rho, (1 - rho) * (2 * rho - 1) / (2 * rho), (1 - rho) / (2 * rho))
pp = stp(u, .5, .5, 0, 1 - rho)
for i, (yy, col, ok, ttl) in enumerate([(pp, C["DPM++2S"], True, r"$w_1,w_2\geq0$"),
                                        (hh, C["Heun1"], False, r"$w_1<0$ or $w_2<0$")]):
    x0 = 2.32 + i * 1.07
    a = fig.add_axes([x0 / W, 0.52 / H, 0.9 / W, 0.95 / H])
    a.plot(u, yy, color=col, lw=1.5)
    a.set_xticks([]); a.set_yticks([]); a.grid(False)
    a.set_xlim(-0.05, 2.1); a.set_ylim(0, 1.5)
    if not ok:
        a.axhline(1.25, color=C["ref"], lw=0.6, ls=(0, (3, 2)))
        a.scatter([0.081, 0.5903, 1.8573], [1.25] * 3, s=9, color=[style.ABC[k] for k in "ABC"], zorder=4)
    a.set_title(ttl, fontsize=7.5, pad=2, color=col)
    a.set_xlabel("input", fontsize=6.8, labelpad=1); a.set_ylabel("output", fontsize=6.8, labelpad=1)
    L.text(x0 + 0.45, 0.38, "global inverse,\nfor every prior and scale" if ok else
           "a fixed two-atom prior gives\nthree inputs for one output",
           ha="center", va="top", fontsize=6.8, color=col, linespacing=1.05)

# ------------------------------------------------------------------ (c) consequence
box(4.55, 0.05, 2.3, 2.22)
head(4.63, 2.2, r"(c) Consequence on $2\to1/8$")
rows = [
    ("DPM++2S", r"$w_1=0$", "1 step, 2 calls", True),
    ("Heun4", r"all $\rho_j=1/2$", "4 steps, 8 calls", True),
    ("Heun1", r"$w_1=-6.56$", "1 step, can collide", False),
]
y = 1.86
for name, cond, cost, ok in rows:
    col = C["DPM++2S"] if name == "DPM++2S" else C["Heun4"] if ok else C["Heun1"]
    L.text(4.66, y, name, fontsize=7.5, fontweight="bold", color=col, va="top")
    L.text(5.22, y, cond, fontsize=7.3, va="top")
    L.text(5.84, y, cost, fontsize=6.9, va="top", color=C["ink"] if ok else C["Heun1"])
    y -= 0.21
L.plot([4.66, 6.78], [1.17, 1.17], color="#C9CED3", lw=0.6)
L.text(4.66, 1.1, "Learned FFHQ64 denoiser: 64 sources, ceiling 160", fontsize=6.9, va="top",
       color=C["muted"])
ff = data.TRADEOFF["FFHQ64 VP"]["rows"]
bx = fig.add_axes([5.5 / W, 0.3 / H, 1.26 / W, 0.6 / H])
names = ["DPM++2S", "Heun2", "Heun1"]
vals = [int(ff[n][3].split("/")[0]) for n in names]
bx.barh(range(3), vals, color=[C[n] for n in names], height=0.62)
bx.set_yticks(range(3), ["DPM++2S", r"Heun2 ($\rho_j<1/2$)", "Heun1"], fontsize=7); bx.invert_yaxis()
bx.set_xlim(0, 64); bx.set_xticks([0, 32, 64]); bx.tick_params(axis="x", labelsize=6.5, pad=1)
bx.grid(axis="y", visible=False)
for i, (n, v) in enumerate(zip(names, vals)):
    bx.text(v + 1 if v < 50 else v - 1, i, f"{v}/64  ({ff[n][0]:.1f})",
            va="center", ha="left" if v < 50 else "right", fontsize=6.6, color="white" if v > 50 else C[n])
bx.set_xlabel("clean sources recovered, of 64", fontsize=6.6, labelpad=1, color=C["muted"])
save(fig, "overview")
