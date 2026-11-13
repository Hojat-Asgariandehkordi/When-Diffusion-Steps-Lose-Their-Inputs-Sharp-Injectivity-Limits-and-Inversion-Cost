"""Shared matplotlib style for all paper figures (Times text, STIX math, Type 42 fonts)."""
import matplotlib as mpl

TEXTWIDTH_MAIN = 6.875   # CVPR two-column \textwidth, inches
TEXTWIDTH_SUPP = 6.5     # supplement (1in margins)

COL = {
    "Heun1": "#B34016",
    "DPM++2S": "#09649A",
    "Heun2": "#007656",
    "Midpoint1": "#996827",
    "Euler2": "#525663",
    "Heun4": "#5B3E8F",
    "ink": "#222222",
    "muted": "#5A6570",
    "grid": "#E3E6E9",
    "ref": "#8A949D",
}
MARK = {"Heun1": "o", "DPM++2S": "s", "Heun2": "^", "Midpoint1": "v", "Euler2": "D"}
# Input states A, B, C in Fig. 1
ABC = {"A": "#7B3F9E", "B": "#1C7C74", "C": "#9A6A12"}


def apply():
    from matplotlib import font_manager
    import make_fonts
    for f in make_fonts.ensure():
        font_manager.fontManager.addfont(f)
    fm = font_manager.fontManager
    fm.ttflist = [e for e in fm.ttflist if not (e.name == "TeX Gyre Termes" and e.fname.endswith(".otf"))]
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": ["TeX Gyre Termes", "Times New Roman", "Nimbus Roman", "Times", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "font.size": 8,
        "axes.titlesize": 8.5,
        "axes.labelsize": 8,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "legend.fontsize": 7.5,
        "axes.edgecolor": "#9AA3AB",
        "axes.linewidth": 0.6,
        "axes.labelcolor": COL["ink"],
        "text.color": COL["ink"],
        "xtick.color": "#4A545E",
        "ytick.color": "#4A545E",
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 2.5,
        "ytick.major.size": 2.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": COL["grid"],
        "grid.linewidth": 0.5,
        "legend.frameon": False,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "figure.dpi": 150,
    })
