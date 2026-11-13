# Reproduce the revised documents

Extract release/paper_source_v3.zip into a fresh folder. Enter paper_source/ and run the following with TeX Live, BibTeX and latexmk.

    sha256sum -c SHA256SUMS.txt
    timeout 120 bash manuscript/build.sh build

The source contains both manuscripts, the figures, the unchanged generated numerical tables, and the official CVPR 2027 style. The code/evidence bundle and full state arrays are the hash-bound dependencies in release/RELEASE_MANIFEST.json. Follow their included REPRODUCE.md for the established offline experiment replay. The round-three check cold-built the revised documents and compared the figure and table bytes with the round-two release.

Check release checksums using `sha256sum -c SHA256SUMS.txt` in release/. Author review and portal actions are described in the author handoff from the bound round-two release.
