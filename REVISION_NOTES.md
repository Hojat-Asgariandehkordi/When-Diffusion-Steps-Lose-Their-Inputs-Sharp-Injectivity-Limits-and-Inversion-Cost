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

## Pass 4 (updated cvpr-paper-revision skill, 2026-11-13)
- Template: hyperref/cleveref now loaded after the preamble as in the kit's main.tex (`postamble.tex`); `\confName`/`\confYear` as in the kit. The supplement now uses the kit itself (two-column, `[review]{cvpr}`, `\maketitlesupplementary`); `geometry`/`float` removed; wide tables and figures use `table*`/`figure*`; long equations broken for the column. cvpr.sty/.bst copied byte for byte into supplement/ so Overleaf compiles it standalone.
- Contributions: "First, ... Second, ... Third, ... Finally, ..." with no bold labels.
- Sec. 3: Lemma 1 (posterior-mean Jacobian), Proposition 1 (nonnegative weights give a global inverse), Proposition 2 (a negative weight folds the map), Proposition 3 (transfer to approximate steps), each with a short proof; the theorem proof combines them.
- Sec. 5 restructured: 5.1 Datasets, 5.2 Experimental settings (plus an implementation-details paragraph collecting all constants), 5.3 Baselines (short names defined; methodological reasons for excluding reversible recurrences and null-text inversion), 5.4 Evaluation metrics (defines the "x points [l, u]" notation).
- Captions: no bold; shortened to content plus takeaway, with definitions moved to the text. Table 1 moved next to its first citation.
- "Choosing a step" merged into a four-paragraph Conclusion (answer, selection rule, limitations, future directions).
- LLM statement now also discloses Claude's role. BioRender was not used, so it is not cited.
- Checks: 0 overfull boxes in both documents; every number in the previous text still appears; Supplement letters A–I and supplement-to-main references verified.
- Page limit: the body runs about half a page onto p. 9 (CVPR limit: 8 pages excluding references). This is an expanded working draft.

## Pass 5 (central Figure 1, 2026-11-13)
- New Fig. 1 (figure*, full width): BioRender artwork (figure c1dd7dba802c2f9fcffffbb5, raw at scripts/assets/biorender/overview_raw.png, 2752x1536, pulled via Overleaf "From external URL") with labels typeset in Times by scripts/fig_overview_br.py from one LAYOUT table. Fixes to the art: placeholder bar charts in (d) erased; the missing connector carrying D_a(x) to the output mix drawn in the art's grey. Panels: (a) step F_a, (b) sign test, (c) schedules on 2 -> 1/8, (d) output-only recovery.
- Methodology (Sec. 3) now opens with a summary paragraph walking through Fig. 1(a)-(d); the intro cites Fig. 1 before the collision figure (now Fig. 2). Supplement references updated (main Fig. 2 collision, Fig. 4 sweep).
- Caption ends "Artwork created in BioRender; all labels typeset by the authors"; the LLM statement discloses BioRender. The named BioRender citation goes in at camera-ready.
- Fixed a stray theorem heading at a column break (needspace before Theorem 1).
- The body now ends on p. 9 (about 1 page over the 8-page limit); expanded working draft.

## Pass 6 (white space, bold, literature review; 2026-11-14)
- White space: removed the \clearpage before the LLM statement (it left a 3-in blank column on p. 9). A blank-run scan of every column now finds no gap above 0.55 in except the natural end of the references.
- Bold: all \paragraph run-in headings removed. Theory, solvers, intro and implementation paragraphs now open with plain sentences; results paragraphs use italic leads. Table 1 cohort labels are italic. Figures keep bold only for panel letters. Theorem/Lemma/Proposition headers stay bold (amsthm).
- Literature review: three connected paragraphs (inversion as a numerical problem; reversal by storing extra state; invertibility theory). Added verified citations: AIDI (ICCV 2023), Fixed-point inversion (arXiv 2023), ReNoise (ECCV 2024), edit-friendly DDPM inversion (CVPR 2024), invertible ResNets (ICML 2019), Neural ODEs (NeurIPS 2018), Tweedie's formula (Efron, JASA 2011). The positioning is explicit: these solvers search for a preimage of a step they did not design, while we characterize when that preimage is unique.
- Checks: 0 overfull boxes, no undefined references, all numbers from the previous version preserved.

## Pass 7 (Figure 5 to the supplement, 2026-11-14)
- Analysis: Fig. 5 (clean failures vs ceiling for AA, AA+L-BFGS, AA+Newton-GMRES) was cited only in the results paragraph that rules out an optimizer artifact. The conclusion's "under every optimizer and ceiling we tried" stays supported by the text and Supp. Fig. 1. Not essential in the main paper.
- Removed the main-paper float. The supplement already holds the fuller two-arm version (Supp. Sec. E, Fig. 1), which the text now cites.
- The paragraph was rewritten with a positive lead ("Robustness to the optimizer, budget and interval. The separation is a property of the step, not of the solver.") and keeps every number. The only number that left the main text is the figure's 75% axis tick.
- Body now ends higher on p. 9 (about 0.4 column saved). scripts/fig_controls_main.py is kept for reference but no longer used.
