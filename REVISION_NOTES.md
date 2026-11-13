# Revision notes — Paper 6

Scope of this pass: figures only. No body text, captions, tables or numbers were edited.

| Figure | File | What changed | Data source |
|---|---|---|---|
| Fig. 1 collision | figures/figure1.pdf | Rebuilt in Times; curves recomputed analytically from the two-atom prior D_s(u)=tanh(u/s^2), rho=1/4; roots and DPM++2S outputs match the printed values (0.081/0.590/1.857; 0.255/0.881/1.214); clearer tile layout and ratio bar | exact (A); tiles recovered from original PDF rasters |
| Fig. 2 trade-off | figures/tradeoff.pdf | Times; direct labels; legend/axis spacing | tables (T); FFHQ and VE CIs **recovered from vector PDF** (R) |
| Supp. controls | figures/controls.pdf | Times; markers dodged so overlapping maps are visible; CIs recomputed (Clopper-Pearson) | 320 ceiling from tables (T); 80/160 **recovered** (R), integer counts |
| Supp. controlled sweep | figures/controlled.pdf | Times; negative-w1 region shaded; recovery labels | sweep_rows.tex (T) |
| Supp. gallery | figures/recovery_gallery.pdf | Times; failures in red; e_x in scientific notation | tiles and e_x recovered from original PDF |

Originals are kept in figures/original/. All plotted numbers live in scripts/data.py with sources.
Rebuild: `scripts/make_all.sh`, then `manuscript/build.sh build`.

Open items for the authors
- Confirm recovered values: FFHQ/VE bootstrap CIs in Fig. 2; 80/160-ceiling failure counts in the controls figure.
- BioRender schematic overview: pending (connector unavailable during this pass).

## Pass 2 (finalization prompt, scientific content frozen)
- New overview **Fig. 1** (`scripts/fig_overview.py`, vector, editable): problem -> sign test -> consequence. The collision figure is now Fig. 2. Every number comes from Thm. 1, Cor. 1 and Tab. 3.
- Structure: the contributions became connected sentences (same claims); the Related Work mini-headings were removed; the closing summary became a short **Conclusion** section; one theory paragraph and one results paragraph were split or merged; the residual-vs-source-error material got its own run-in heading.
- Figure fixes from the independent review: green is reserved for Heun2 (Heun4 is purple, source B is slate, "protected" is blue); Heun1 N_f was added in Fig. 1c; Fig. 3 bootstrap bars are visible; label collisions fixed.
- Supplement: its "Fig. 1" reference now reads "Fig. 2" (renumbering only).
- Unchanged: theorems, numbers, tables, the abstract, and the experiments/results prose.
- Independent review (before the fixes): 6/10, confidence 3. The remaining objections are scientific (the experiments do not test multiplicity directly; small images and a single interval; incremental over Verbii/Hong) and need new evidence or content changes.
