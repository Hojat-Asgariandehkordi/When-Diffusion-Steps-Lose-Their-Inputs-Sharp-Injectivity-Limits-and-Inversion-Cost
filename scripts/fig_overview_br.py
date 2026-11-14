"""Fig. 1: BioRender artwork (scripts/assets/biorender/overview_raw.png, 2752x1536, no lettering)
with scientific fixes and every label typeset in Times from one LAYOUT table.

Fixes to the raw art:
  * erase the two placeholder bar charts in panel (d) (they encode no data);
  * draw the missing connector that carries the first prediction D_a(x) to the output mix,
    since F_a(x) = r x + w1 D_a(x) + w2 D_{ka}(p_a(x)).
Coordinates are pixels of the raw art (origin top-left)."""
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import style
from common import HERE, save

style.apply()
RAW = os.path.join(HERE, "assets", "biorender", "overview_raw.png")
art = np.asarray(Image.open(RAW).convert("RGB")).astype(float) / 255
H, W = art.shape[:2]
INK, GREY = "#222222", "#5F6670"
BLUE, RED, GREEN, OK = "#1F6FA8", "#B5441E", "#2F8F6E", "#2E8B57"


def erase(x0, y0, x1, y1):
    """Fill a box with the median colour of its one-pixel border (panel background)."""
    border = np.concatenate([art[y0, x0:x1], art[y1, x0:x1], art[y0:y1, x0], art[y0:y1, x1]])
    art[y0:y1, x0:x1] = np.median(border, axis=0)


erase(2490, 890, 2680, 1045)    # placeholder bars, recovered row
erase(2490, 1215, 2680, 1370)   # placeholder bars, failed row

# ---- LAYOUT: (x, y, text, size, colour, ha, va, weight)
LAYOUT = [
    # panel titles
    (75, 92, "(a) One two-stage step $F_a$", 9, INK, "left", "center", "bold"),
    (1740, 92, "(b) Sign test (Thm. 1)", 9, INK, "left", "center", "bold"),
    (75, 838, r"(c) Schedules from $a=2$ to $b=1/8$ (Cor. 1)", 9, INK, "left", "center", "bold"),
    (1420, 838, "(d) Recovery with a learned denoiser (Sec. 6)", 9, INK, "left", "center", "bold"),
    # (a) step
    (190, 585, "input $x$ at noise $a$", 8, INK, "center", "top", "normal"),
    (485, 268, "$D_a$", 8.5, INK, "center", "center", "normal"),
    (890, 520, "stage $p_a(x)$", 8, INK, "center", "top", "normal"),
    (1184, 520, r"$D_{\kappa a}$", 8.5, INK, "center", "top", "normal"),
    (1362, 318, "$w_1\\,w_2$", 8, INK, "center", "bottom", "normal"),
    (1545, 545, "saved $y=F_a(x)$", 8, INK, "center", "top", "normal"),
    (1545, 593, "noise $b$", 8, GREY, "center", "top", "normal"),
    (865, 705, r"$F_a(x)=r\,x+w_1D_a(x)+w_2D_{\kappa a}(p_a(x))$", 8.5, INK, "center", "center", "normal"),
    # (b) sign test
    (1830, 322, r"$w_1,w_2\geq0$", 8, BLUE, "center", "top", "normal"),
    (2450, 66, "one input per output", 7.6, BLUE, "center", "center", "normal"),
    (1890, 700, "a negative weight", 8, RED, "center", "top", "normal"),
    (2522, 722, "three inputs, one output", 7.3, RED, "center", "center", "normal"),
    # (c) schedules
    (700, 885, r"Heun: $\lceil\log_2(a/b)\rceil=4$ substeps with $\rho_j=1/2$, 8 calls", 8, GREEN, "center", "center", "normal"),
    (125, 1215, "$a$", 8.5, INK, "center", "top", "normal"),
    (1285, 1215, "$b$", 8.5, INK, "center", "top", "normal"),
    (700, 1420, "DPM++2S: one step, 2 calls", 8, BLUE, "center", "center", "normal"),
    # (d) learned recovery
    (1565, 1270, "saved $y$ only", 8, INK, "center", "top", "normal"),
    (1942, 1270, "iterative", 8, INK, "center", "top", "normal"),
    (1942, 1318, "inverse", 8, INK, "center", "top", "normal"),
    (2490, 945, "recovered", 8, OK, "left", "center", "normal"),
    (2490, 995, r"$e_x\leq0.02$", 8, OK, "left", "center", "normal"),
    (2490, 1275, "not", 8, RED, "left", "center", "normal"),
    (2490, 1325, "recovered", 8, RED, "left", "center", "normal"),
]

fig = plt.figure(figsize=(style.TEXTWIDTH_MAIN, style.TEXTWIDTH_MAIN * H / W))
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(art, extent=(0, W, H, 0), interpolation="lanczos")
ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")

# missing connector: first prediction D_a(x) -> output mix (drawn in the art's own grey)
lw = 1.1
ax.plot([640, 640, 1340, 1340], [400, 640, 640, 445], color=GREY, lw=lw, solid_capstyle="round", zorder=3)
ax.annotate("", xy=(1340, 438), xytext=(1340, 470),
            arrowprops=dict(arrowstyle="-|>", color=GREY, lw=lw, mutation_scale=7), zorder=4)
ax.plot([640], [390], marker="o", ms=2.6, color=GREY, zorder=4)

for x, y, t, size, col, ha, va, wt in LAYOUT:
    ax.text(x, y, t, fontsize=size, color=col, ha=ha, va=va, fontweight=wt, zorder=5)
save(fig, "overview")
