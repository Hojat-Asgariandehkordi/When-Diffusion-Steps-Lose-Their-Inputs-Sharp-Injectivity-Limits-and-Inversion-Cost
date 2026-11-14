"""Supplement: saved clean-target inverse states (tiles recovered from the original figure)."""
import matplotlib.pyplot as plt
import style, data
from common import tile, framed, save

style.apply()
C = style.COL
colcol = {"Source": C["ink"], "Heun1": C["Heun1"], "DPM++2S": C["DPM++2S"], "Heun2": C["Heun2"]}
fig = plt.figure(figsize=(style.TEXTWIDTH_SUPP, 2.2))
TS = 0.66
W, H = 6.5, 2.2
x0s = [0.55, 3.62]
for (title, g), x0 in zip(data.GALLERY.items(), x0s):
    fig.text(x0 / W, 0.975, title, fontsize=9, va="top")
    for r in range(2):
        y = H - 0.42 - r * (TS + 0.3) - TS
        if x0 == x0s[0]:
            fig.text(0.02, (y + TS / 2) / H, f"Index {r + 1}", va="center", fontsize=8)
        for c, name in enumerate(data.GALLERY_COLS):
            x = x0 + c * (TS + 0.06)
            ax = fig.add_axes([x / W, y / H, TS / W, TS / H])
            framed(ax, tile("gallery", g["tiles"][r][c], g["native"]), colcol[name], lw=1.0 if c else 1.3)
            if r == 0:
                ax.set_title(name, fontsize=8, color=colcol[name], pad=2.5)
            if c:
                v = g["ex"][r][c - 1]
                fail = float(v) > data.RECOVERY_THRESHOLD
                if float(v) < 1e-3:
                    m, e = f"{float(v):.2e}".split("e-")
                    m = v.split("e-")[0] if "e-" in v else m.rstrip("0").rstrip(".")
                    txt = rf"${m}\times10^{{-{int(e)}}}$"
                else:
                    txt = v
                ax.text(0.5, -0.05, txt, transform=ax.transAxes, ha="center", va="top", fontsize=7.5,
                        color=C["Heun1"] if fail else C["muted"])
save(fig, "recovery_gallery")
