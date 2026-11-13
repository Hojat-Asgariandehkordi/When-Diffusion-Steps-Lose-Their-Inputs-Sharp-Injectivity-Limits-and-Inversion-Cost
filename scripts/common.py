import os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.normpath(os.path.join(HERE, "..", "figures"))


def tile(folder, idx, native):
    """Load an embedded raster recovered from the original PDF and undo its
    nearest-neighbour upsampling, returning the native-resolution RGB array."""
    a = np.asarray(Image.open(os.path.join(HERE, "assets", folder, f"t-{idx:03d}.png")).convert("RGB"))
    n = a.shape[0]
    centers = ((np.arange(native) + 0.5) * n / native).astype(int)
    return a[np.ix_(centers, centers)]


def framed(ax, img, color, lw=1.4):
    ax.imshow(img, interpolation="nearest")
    ax.set_xticks([]); ax.set_yticks([]); ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(True); s.set_color(color); s.set_linewidth(lw)


def save(fig, name):
    path = os.path.join(FIGDIR, name + ".pdf")
    fig.savefig(path)
    fig.savefig(os.path.join(HERE, "..", "build_previews", name + ".png"), dpi=200) if os.path.isdir(
        os.path.join(HERE, "..", "build_previews")) else None
    print("wrote", path)
