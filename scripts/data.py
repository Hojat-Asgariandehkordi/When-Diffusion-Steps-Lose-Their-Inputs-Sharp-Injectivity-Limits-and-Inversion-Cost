"""Every number plotted in the figures, with its source.

Sources
-------
T  = manuscript/generated/*.tex (authors' verified analysis output; exact)
R  = RECOVERED from the original vector figure (figures/original/*.pdf) by reading
     drawing coordinates with PyMuPDF. Axis mapping was validated on points that
     also appear in T (agreement to <=1e-4). Flagged for author confirmation.
A  = recomputed analytically from the paper's own definitions.
"""

# ---------------------------------------------------------------- tradeoff (Fig. 3)
# (mean iterative forwards N_f, mean forward RMS e_flow, 95% seed-bootstrap CI, clean recovered)
TRADEOFF = {
    "FFHQ64 VP": dict(
        cap=160, n=64, note="frozen 64",
        rows={  # N_f, e_flow: T ffhq_rows_labeled.tex; CI: R tradeoff.pdf
            "Heun1": (159.7, 0.1015, (0.0994, 0.1036), "5/64"),
            "DPM++2S": (78.2, 0.0490, (0.0462, 0.0520), "64/64"),
            "Heun2": (158.3, 0.0239, (0.0230, 0.0248), "64/64"),
        }),
    "CIFAR-10 VP": dict(
        cap=320, n=64, note="reused 64",
        rows={  # N_f, e_flow: T primary_rows_labeled.tex; CI: T fidelity_cpu_rows.tex
            "Heun1": (250.6, 0.1095, (0.1035, 0.1160), "18/64"),
            "DPM++2S": (69.2, 0.0683, (0.0636, 0.0728), "64/64"),
            "Heun2": (163.1, 0.0368, (0.0316, 0.0431), "64/64"),
        }),
    "CIFAR-10 VE": dict(
        cap=160, n=32, note="frozen 32",
        rows={  # N_f, e_flow: T ve_rows_labeled.tex; CI: R tradeoff.pdf
            "Heun1": (147.0, 0.1068, (0.1014, 0.1126), "10/32"),
            "DPM++2S": (68.2, 0.0653, (0.0602, 0.0703), "32/32"),
            "Heun2": (146.8, 0.0310, (0.0283, 0.0343), "31/32"),
        }),
}
CALLS_PER_MAP = {"Heun1": 2, "DPM++2S": 2, "Heun2": 4}

# ---------------------------------------------------------------- controlled sweep (Supp. Fig.)
# T sweep_rows.tex: w1 -> (recovered/12, mean e_x, mean N_f)
SWEEP_W1 = [-6.5625, -0.5, -0.125, 0.0, 0.125, 0.5]
SWEEP = {
    r"$2\to1/8$": [(0, 0.681, 160.0), (12, 2.98e-5, 88.7), (12, 2.34e-5, 75.3),
                   (12, 2.32e-5, 73.8), (12, 2.34e-5, 71.0), (12, 2.14e-5, 71.7)],
    r"$1\to1/16$": [(0, 0.283, 160.0), (12, 6.68e-5, 91.5), (12, 2.48e-5, 75.5),
                    (12, 2.45e-5, 73.8), (12, 2.41e-5, 73.5), (12, 2.29e-5, 75.3)],
}
SWEEP_N = 12
RECOVERY_THRESHOLD = 0.02

# ---------------------------------------------------------------- inverse controls (Supp. Fig.)
# Failure counts out of 64 on the reused primary CIFAR-VP seeds.
# Ceiling 320: T controls_clean.tex / controls_noisy.tex.
# Ceilings 80 and 160: R controls.pdf (marker centres map to integers to within 0.02 count).
CEILINGS = [80, 160, 320]
CONTROLS = {
    "clean": {
        "Anderson":          {"Euler2": [0, 0, 0], "Heun1": [47, 46, 46], "Midpoint1": [12, 10, 9],  "DPM++2S": [0, 0, 0], "Heun2": [2, 1, 0]},
        "AA + L-BFGS":       {"Euler2": [0, 0, 0], "Heun1": [47, 47, 47], "Midpoint1": [12, 12, 12], "DPM++2S": [0, 0, 0], "Heun2": [2, 2, 2]},
        "AA + Newton–GMRES": {"Euler2": [0, 0, 0], "Heun1": [47, 47, 46], "Midpoint1": [12, 12, 10], "DPM++2S": [0, 0, 0], "Heun2": [2, 1, 1]},
    },
    "noisy": {
        "Anderson":          {"Euler2": [1, 0, 0], "Heun1": [48, 47, 47], "Midpoint1": [12, 11, 11], "DPM++2S": [0, 0, 0], "Heun2": [3, 0, 0]},
        "AA + L-BFGS":       {"Euler2": [1, 1, 1], "Heun1": [48, 47, 47], "Midpoint1": [12, 12, 12], "DPM++2S": [0, 0, 0], "Heun2": [3, 3, 3]},
        "AA + Newton–GMRES": {"Euler2": [1, 1, 0], "Heun1": [48, 47, 47], "Midpoint1": [12, 12, 11], "DPM++2S": [0, 0, 0], "Heun2": [3, 2, 1]},
    },
}
CONTROLS_N = 64

# ---------------------------------------------------------------- Fig. 1 (collision)
# A: the two-atom prior (delta_{-1}+delta_{+1})/2 on the line c+uv with ||v||=1, so
# D_s(u)=tanh(u/s^2) (Sec. 2). Normalized noise 1 -> 1/4 (rho=1/4).
# Fitting a general two-atom line model to the printed A/B/C values recovers atoms
# at u=-1,+1 and ||v||=1 (residual <3e-4, i.e. display rounding), confirming this.
FIG1_RHO = 0.25
FIG1_TARGET = 1.25
# Tiles: R, embedded rasters of figure1.pdf (display-mapped, [-1.8,1.8]); 32x32 native.
FIG1_TILES = {"A_src": 0, "A_dpm": 1, "B_src": 2, "B_dpm": 3, "C_src": 4, "C_dpm": 5, "heun": 6}

# ---------------------------------------------------------------- recovery gallery (Supp. Fig.)
# R: embedded rasters and printed e_x values from recovery_gallery.pdf.
GALLERY = {
    "CIFAR-10 VP  ·  AA320": dict(native=32, tiles=[[0, 1, 2, 3], [7, 5, 7, 7]],
                                 ex=[["0.128", "2.37e-05", "2.24e-05"], ["0.312", "2.19e-05", "2.1e-05"]]),
    "FFHQ64 VP  ·  AA160": dict(native=64, tiles=[[8, 9, 10, 11], [12, 13, 14, 15]],
                               ex=[["0.105", "2.57e-05", "2.49e-05"], ["0.925", "3.26e-05", "0.00019"]]),
}
GALLERY_COLS = ["Source", "Heun1", "DPM++2S", "Heun2"]
