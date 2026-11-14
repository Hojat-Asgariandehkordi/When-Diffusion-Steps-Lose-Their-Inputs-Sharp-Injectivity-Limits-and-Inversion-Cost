"""Format Table 1 rows from the verified generated rows (manuscript/generated/*_rows_labeled.tex).

No number is retyped: each row is parsed from the analysis output and rewritten for
siunitx S columns. Recovery shows counts only (N is in the cohort header). Bold marks the
best value per cohort among the compared step maps: most clean / noisy recoveries,
lowest forward RMS, lowest inverse work (ties are all bold)."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "manuscript", "generated"))
COHORTS = {"ffhq": "ffhq_rows_labeled", "primary": "primary_rows_labeled", "ve": "ve_rows_labeled"}
B = r"\bfseries "


def parse(name):
    rows = []
    for line in open(os.path.join(GEN, name + ".tex")):
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        cells = [c.strip() for c in line.rstrip("\\").split("&")]
        m, calls, clean, noisy, flow, nf = cells
        rows.append(dict(map=m, calls=calls, clean=int(clean.split("/")[0]), noisy=int(noisy.split("/")[0]),
                         n=int(clean.split("/")[1]), flow=flow, nf=nf))
    return rows


for key, name in COHORTS.items():
    rows = parse(name)
    best = dict(clean=max(r["clean"] for r in rows), noisy=max(r["noisy"] for r in rows),
                flow=min(float(r["flow"]) for r in rows), nf=min(float(r["nf"]) for r in rows))
    out = [f"% Formatted by scripts/make_table1.py from generated/{name}.tex; do not edit."]
    for r in rows:
        c = (B if r["clean"] == best["clean"] else "") + str(r["clean"])
        z = (B if r["noisy"] == best["noisy"] else "") + str(r["noisy"])
        f = (B if float(r["flow"]) == best["flow"] else "") + r["flow"]
        w = (B if float(r["nf"]) == best["nf"] else "") + r["nf"]
        out.append(f"{r['map']} & {r['calls']} & {c} & {z} & {f} & {w} \\\\")
    path = os.path.join(GEN, f"table1_{key}.tex")
    open(path, "w").write("\n".join(out) + "\n")
    print("wrote", path)
