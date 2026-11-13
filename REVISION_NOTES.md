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

## Pass 3 (supervisor comments, 2026-11-13)
- Abstract rewritten for a broad reader around one message; numbers unchanged (64/64, 5/64).
- Intro: problem -> limitation -> idea -> toy example (two-image line, Fig. 1) -> contributions (a)-(d) as connected sentences.
- Related work: two connected paragraphs; added verified classics (DDPM, DDIM, score SDE, null-text inversion). Old Table 2 moved to Supplement I.
- Math: Sec. 3 defines prior, noise, posterior mean, stage, weights and invertibility before use; covariance identity, Jacobian bound, chain-rule Jacobian, similarity, finite-difference argument, co-Lipschitz constant c_*, scalar derivative and fold argument, Lipschitz transfer (from Supp. A).
- Sec. 4: Table 1 removed; Heun/midpoint/DPM++2S weights derived in text (Eqs. 13-16); experiment interval numbers from Supp. B.
- Figures, all one column at 8-9 pt Times: Fig. 1 (a)+(b) stacked, ratio bar moved to text; Fig. 2 trade-off with log axis so CIs show; Fig. 3 fixed-stage sweep with follow-up panels (forward RMS, directional gain), neutral colours, no text on data; Fig. 4 clean failures vs ceiling (from supplement). Arrows are neutral grey.
- Table 3 one column. Results reorganized around three questions; sweep equation (19) added. Conclusion with limitations and future directions.
- Main: 9 pages (8 of content + LLM statement/refs). Supplement: 15 pages. No overfull boxes; only Times/STIX in figures.
