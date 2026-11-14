"""DRAFT Fig. 1, version 2 (not used in the paper until approved).
Art: BioRender figure e1ee029660ff8494a945e2bd (step | folded-ribbon sign test | schedules + recovery).
Post-processing: add the missing third input to the folding ribbon, replace the glyphs above the
ribbons by drawn weight arrows, crop empty margins, typeset all labels in Times.
Coordinates are in 1024-px preview units; S rescales them to the art actually loaded."""
import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from PIL import Image
import style
from common import HERE, FIGDIR

style.apply()
RAW = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "assets", "biorender", "overview_v2_raw.png")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(FIGDIR, "overview_v2")
img = Image.open(RAW).convert("RGB")
S = img.width / 1024.0
art = np.asarray(img).astype(float) / 255
P = lambda v: int(round(v * S))
INK, GREY = "#222222", "#5F6670"
BLUE, RED, GREEN, OK = "#1F6FA8", "#B5441E", "#2F8F6E", "#2E8B57"
bg = np.median(art[P(20):P(60), P(20):P(380)].reshape(-1, 3), axis=0)


def erase(x0, y0, x1, y1):
    art[P(y0):P(y1), P(x0):P(x1)] = bg


# 1) folding ribbon gets the same three inputs as the blue ribbon (purple, grey, ochre)
src = art[P(172):P(267), P(430):P(463)].copy()           # the three blue-ribbon inputs
erase(426, 324, 466, 396)
h = P(392) - P(326)
tiles = np.asarray(Image.fromarray((src * 255).astype(np.uint8)).resize((src.shape[1] * h // src.shape[0], h),
                                                                       Image.LANCZOS)).astype(float) / 255
x0 = P(447) - tiles.shape[1] // 2
art[P(326):P(326) + h, x0:x0 + tiles.shape[1]] = tiles
# 2) remove the glyphs above both ribbons
erase(552, 150, 608, 184)
erase(552, 294, 608, 326)
# 3) redundant check marks in (c): four above the hops, one below the arc (labels go there)
erase(796, 110, 1004, 145)
erase(880, 243, 912, 268)

# crop empty margins
Y0, Y1 = 96, 470
art = art[P(Y0):P(Y1)]
Wpx, Hpx = art.shape[1], art.shape[0]
fig = plt.figure(figsize=(style.TEXTWIDTH_MAIN, style.TEXTWIDTH_MAIN * Hpx / Wpx))
ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(art, extent=(0, 1024, Y1, Y0), interpolation="lanczos")
ax.set_xlim(0, 1024); ax.set_ylim(Y1, Y0); ax.axis("off")

# drawn weight icons: two up arrows (blue), one up + one down (red)
def warrow(x, y0, y1, col):
    ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle="-|>", mutation_scale=7, color=col, lw=1.4))
warrow(574, 180, 160, BLUE); warrow(586, 180, 160, BLUE)
warrow(574, 322, 302, RED); warrow(586, 302, 322, RED)

T = lambda x, y, s, size=8, col=INK, ha="center", va="center": ax.text(x, y, s, fontsize=size, color=col,
                                                                        ha=ha, va=va, zorder=5)
# panel titles
T(12, 104, r"$\mathbf{(a)}$ One two-stage step $F_a$", 9, ha="left")
T(428, 104, r"$\mathbf{(b)}$ Sign test (Thm. 1)", 9, ha="left")
T(784, 104, r"$\mathbf{(c)}$ Schedules, $a=2\to b=1/8$", 9, ha="left")
T(784, 300, r"$\mathbf{(d)}$ Output-only recovery", 9, ha="left")
# (a)
T(50, 328, "input $x$", 7.6); T(50, 341, "noise $a$", 7.6, GREY)
T(113, 254, "$D_a$", 8.4); T(157, 307, "$p_a$", 7.6, GREY)
T(214, 328, "stage $p_a(x)$", 7.6)
T(277, 254, r"$D_{\kappa a}$", 8.4)
T(319, 307, "$w_1\\,w_2$", 7.6)
T(371, 337, "saved $y$", 7.6); T(371, 350, "noise $b$", 7.6, GREY)
T(207, 395, r"$F_a(x)=r\,x+w_1D_a(x)+w_2D_{\kappa a}(p_a(x))$", 8.4)
# (b)
T(470, 152, r"$w_1,w_2\geq0$", 7.8, BLUE, ha="left")
T(470, 304, r"a weight $<0$", 7.8, RED, ha="left")
T(590, 281, "one input per output", 7.4, BLUE)
T(620, 412, "three inputs, one output", 7.4, RED)
# (c)
T(895, 126, r"Heun: 4 substeps, each $\rho=1/2$", 7.4, GREEN)
T(790, 222, "$a$", 8); T(1004, 222, "$b$", 8)
T(895, 256, "DPM++2S: one step", 7.4, BLUE)
# (d)
T(817, 428, "saved $y$", 7.6)
T(893, 442, "inverse", 7.6)
T(971, 381, "recovered", 7.2, OK)
T(971, 461, "not recovered", 7.2, RED)
fig.savefig(OUT + ".pdf"); fig.savefig(OUT + ".png", dpi=220)
print("wrote", OUT)
