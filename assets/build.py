#!/usr/bin/env python3
"""Generate the profile's SVG assets. No dependencies. Run: python3 assets/build.py"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONT = "-apple-system, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Menlo, Consolas, monospace"
BG, BG2, LINE = "#0b1220", "#111a2e", "#1f2a44"
FG, MUTED, DIM = "#f1f5f9", "#94a3b8", "#64748b"
AMBER, BLUE, GREEN = "#f59e0b", "#60a5fa", "#34d399"


def defs():
    return f"""<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{BG2}"/>
  </linearGradient>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{AMBER}"/><stop offset="1" stop-color="{BLUE}"/>
  </linearGradient>
  <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">
    <circle cx="1" cy="1" r="1" fill="{LINE}"/>
  </pattern>
  <radialGradient id="glow" cx="0.85" cy="0.1" r="0.7">
    <stop offset="0" stop-color="{BLUE}" stop-opacity="0.18"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/>
  </radialGradient>
</defs>"""


def chip(x, y, label, color=AMBER, mono=False):
    w = int(len(label) * 7.4 + 24)
    fam = MONO if mono else FONT
    return (f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="13" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-opacity="0.45"/>'
            f'<text x="{x + w / 2}" y="{y + 17}" text-anchor="middle" font-family="{fam}" font-size="12" font-weight="600" fill="{color}">{label}</text>', w)


def hero():
    W, H = 1000, 260
    chips, x = [], 48
    for label, color in [("4.0 GPA · Dakota State University", GREEN), ("2 published evaluation tools", AMBER)]:
        s, w = chip(x, 192, label, color)
        chips.append(s)
        x += w + 12
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Elnatan Anbelu">
{defs()}
<rect width="{W}" height="{H}" rx="18" fill="url(#g)"/>
<rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>
<rect width="{W}" height="{H}" rx="18" fill="url(#glow)"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{LINE}"/>
<rect x="48" y="52" width="44" height="4" rx="2" fill="url(#accent)"/>
<text x="48" y="112" font-family="{FONT}" font-size="52" font-weight="800" fill="{FG}" letter-spacing="-1.5">Elnatan Anbelu</text>
<text x="48" y="150" font-family="{FONT}" font-size="19" fill="{MUTED}">Software / AI engineer in training. I build tools that measure how AI systems actually behave.</text>
{''.join(chips)}
<g font-family="{MONO}" font-size="13" fill="{DIM}">
  <text x="{W - 48}" y="66" text-anchor="end">github.com/ElnatanAnbelu</text>
  <text x="{W - 48}" y="88" text-anchor="end">Madison, SD · EN / አማርኛ</text>
</g>
</svg>"""


def card(name, pitch, stats, lang, lang_color, status="Published · MIT"):
    W, H = 590, 200
    stat_svg, x = [], 28
    for value, label in stats:
        stat_svg.append(f'<text x="{x}" y="146" font-family="{FONT}" font-size="26" font-weight="800" fill="{FG}" letter-spacing="-0.5">{value}</text>'
                        f'<text x="{x}" y="166" font-family="{FONT}" font-size="11.5" fill="{DIM}" letter-spacing="0.4">{label.upper()}</text>')
        x += 175
    pitch_lines = pitch.split("\n")
    pitch_svg = "".join(f'<text x="28" y="{80 + i * 20}" font-family="{FONT}" font-size="14" fill="{MUTED}">{l}</text>' for i, l in enumerate(pitch_lines))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{name}">
{defs()}
<rect width="{W}" height="{H}" rx="16" fill="url(#g)"/>
<rect width="{W}" height="{H}" rx="16" fill="url(#glow)"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="16" fill="none" stroke="{LINE}"/>
<rect x="0" y="0" width="4" height="{H}" rx="2" fill="url(#accent)"/>
<text x="28" y="46" font-family="{MONO}" font-size="19" font-weight="700" fill="{FG}">{name}</text>
<text x="{W - 28 - 84 - 14}" y="43" text-anchor="end" font-family="{FONT}" font-size="11.5" font-weight="600" fill="{DIM}">{status}</text>
{pitch_svg}
{''.join(stat_svg)}
<g transform="translate({W - 28 - 84}, 26)">
  <rect width="84" height="26" rx="13" fill="{lang_color}" fill-opacity="0.12" stroke="{lang_color}" stroke-opacity="0.45"/>
  <circle cx="16" cy="13" r="4" fill="{lang_color}"/>
  <text x="28" y="17" font-family="{FONT}" font-size="12" font-weight="600" fill="{lang_color}">{lang}</text>
</g>
</svg>"""


def divider(label):
    W, H = 900, 52
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">
{defs()}
<text x="0" y="32" font-family="{FONT}" font-size="26" font-weight="800" fill="{FG}" letter-spacing="-0.5">{label}</text>
<rect x="0" y="47" width="44" height="3" rx="1.5" fill="url(#accent)"/>
<rect x="52" y="48" width="{W - 52}" height="1" fill="{LINE}"/>
</svg>"""


def main():
    out = {
        "hero.svg": hero(),
        "card-mcp-scanner-benchmark.svg": card(
            "mcp-scanner-benchmark",
            "The referee for MCP security scanners. Every vulnerable case is paired with\na fixed twin, so a scanner that flags both is proven to have detected nothing.",
            [("32", "labeled cases"), ("9", "scanner adapters"), ("6", "issues caught pre-release")],
            "Python", BLUE),
        "card-agent-search-metric.svg": card(
            "agent-search-metric",
            "Do coding agents submit the best solution they already measured?\nRe-analysis of 269 published InferenceBench trajectories. Mostly, no.",
            [("269", "trajectories read"), ("45%", "shipped unmeasured"), ("20", "runs hand-validated")],
            "Python", BLUE),
        "card-own-brain.svg": card(
            "own-brain",
            "Training small language models from scratch on a laptop (PyTorch / MPS,\nmodded-nanogpt lineage), scored on a 100-task eval harness I built.",
            [("4", "model generations"), ("~1B", "tokens, current run"), ("100", "eval tasks")],
            "PyTorch", AMBER, status="In progress · private"),
        "card-addis-market.svg": card(
            "addis-market",
            "Ethiopian-first multi-vendor marketplace. Escrow payments backed by a\ndouble-entry ledger; I own the architecture and the security model.",
            [("291", "unit tests green"), ("12", "typechecked packages"), ("3", "blockers fixed")],
            "TypeScript", GREEN, status="Pre-launch · private"),
        "h-published.svg": divider("Published"),
        "h-building.svg": divider("Building"),
        "h-stack.svg": divider("Stack"),
        "h-how.svg": divider("How I work"),
    }
    for name, svg in out.items():
        (HERE / name).write_text(svg)
        print("wrote", name)


if __name__ == "__main__":
    main()
