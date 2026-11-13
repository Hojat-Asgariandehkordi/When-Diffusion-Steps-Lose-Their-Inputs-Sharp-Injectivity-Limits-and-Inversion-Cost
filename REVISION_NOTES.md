# Revision notes — Paper 6 (figures pass, text unchanged)

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
