# Convert TeX Gyre Termes OTF -> TTF (Type 42-safe embedding).
import sys
from fontTools.ttLib import TTFont, newTable
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
def otf_to_ttf(src, dst, max_err=1.0):
    f = TTFont(src); gs = f.getGlyphSet(); order = f.getGlyphOrder()
    glyf = {}
    for n in order:
        pen = TTGlyphPen(gs); gs[n].draw(Cu2QuPen(pen, max_err, reverse_direction=True)); glyf[n] = pen.glyph()
    f["loca"] = newTable("loca"); g = f["glyf"] = newTable("glyf"); g.glyphOrder = order; g.glyphs = glyf
    del f["CFF "]
    if "VORG" in f: del f["VORG"]
    f["maxp"] = newTable("maxp"); m=f["maxp"]; m.tableVersion=0x00010000
    for a in ("maxZones","maxTwilightPoints","maxStorage","maxFunctionDefs","maxInstructionDefs","maxStackElements","maxSizeOfInstructions","maxComponentElements"): setattr(m,a,0)
    m.maxZones=1; f["head"].glyphDataFormat=0
    f["post"].formatType=2.0; f["post"].extraNames=[]; f["post"].mapping={}; f["post"].glyphOrder=order
    f.sfntVersion="\x00\x01\x00\x00"; f.save(dst)

import os, glob
SRC = "/usr/share/texmf/fonts/opentype/public/tex-gyre"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")


def ensure():
    """Convert TeX Gyre Termes (CFF OpenType) to TrueType so matplotlib embeds valid Type 42
    fonts. Converted files are local build products and are not committed (GUST font licence)."""
    os.makedirs(OUT, exist_ok=True)
    for st in ("regular", "bold", "italic", "bolditalic"):
        dst = os.path.join(OUT, f"texgyretermes-{st}.ttf")
        src = os.path.join(SRC, f"texgyretermes-{st}.otf")
        if not os.path.exists(dst) and os.path.exists(src):
            otf_to_ttf(src, dst)
    return sorted(glob.glob(os.path.join(OUT, "*.ttf")))


if __name__ == "__main__":
    print(ensure())
