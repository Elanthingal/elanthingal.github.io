#!/usr/bin/env python3
"""Generate the styled SVG assets used by the markdown pages.

GitHub strips CSS from markdown, but renders SVG images fully — including
@font-face fonts embedded as base64 data URIs. This script subsets are in
scripts/fonts/ (Space Grotesk 600, DM Mono 500) and every asset embeds them
so the pages carry the site typography.

Usage: python3 scripts/make_assets.py
"""

import base64
import json
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = pathlib.Path(__file__).resolve().parent / "fonts"
ASSETS = ROOT / "assets"

PAPER = "#f3f0e9"
PAPER_LIGHT = "#fbfaf6"
INK = "#12212b"
MUTED = "#66727a"
LINE = "#d8d5cd"
TEAL = "#0e7490"
TEAL_LIGHT = "#b9eee8"
ORANGE = "#ef633d"


def font_css() -> str:
    sg = base64.b64encode((FONTS / "sg.woff2").read_bytes()).decode()
    dmm = base64.b64encode((FONTS / "dmm.woff2").read_bytes()).decode()
    return f"""
    @font-face {{
      font-family: 'SG';
      src: url(data:font/woff2;base64,{sg}) format('woff2');
      font-weight: 600;
    }}
    @font-face {{
      font-family: 'DMM';
      src: url(data:font/woff2;base64,{dmm}) format('woff2');
      font-weight: 500;
    }}
    .h {{ font-family: 'SG', 'Avenir Next', sans-serif; font-weight: 600; letter-spacing: -1px; }}
    .m {{ font-family: 'DMM', Consolas, monospace; font-weight: 500; letter-spacing: 2px; }}
    """


def svg(name: str, width: int, height: int, body: str, title: str) -> None:
    content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{title}">
  <style>{font_css()}</style>
{body}
</svg>
"""
    (ASSETS / name).write_text(content)
    size = (ASSETS / name).stat().st_size
    print(f"  {name}: {size // 1024}KB")


def page_header(slug: str, eyebrow: str, heading: str, accent: str) -> None:
    body = f"""
  <rect width="1200" height="120" fill="{INK}"/>
  <circle cx="1150" cy="130" r="90" fill="none" stroke="{TEAL_LIGHT}" opacity=".22"/>
  <circle cx="1080" cy="105" r="45" fill="none" stroke="{TEAL_LIGHT}" opacity=".3"/>
  <rect x="0" y="0" width="6" height="120" fill="{accent}"/>
  <circle cx="46" cy="60" r="4" fill="{accent}"/>
  <text x="66" y="47" class="m" font-size="13" fill="{TEAL_LIGHT}">{eyebrow}</text>
  <text x="64" y="92" class="h" font-size="40" fill="{PAPER_LIGHT}">{heading}</text>
  <text x="1136" y="66" class="m" font-size="12" fill="{PAPER}" opacity=".45" text-anchor="end">EC / PORTFOLIO</text>
"""
    svg(f"header-{slug}.svg", 1200, 120, body, heading)


def card_height(title_lines: list, sub_lines: list, link: bool) -> int:
    """Height needed so text never collides: content flows down, link gets its own band."""
    h = 108 + 36 * len(title_lines) + 6 + 22 * len(sub_lines)
    if link:
        h += 44
    return h + 18


def card(x: int, w: int, h: int, bg: str, ring: str, index: str, index_fill: str,
         title_lines: list, title_fill: str, sub_lines: list, sub_fill: str,
         link_label: str = "", link_fill: str = "") -> str:
    parts = [f'  <g>',
             f'    <rect x="{x}" y="8" width="{w}" height="{h}" fill="{bg}"/>',
             f'    <circle cx="{x + w - 20}" cy="{h - 4}" r="64" fill="none" stroke="{ring}" opacity=".18"/>',
             f'    <text x="{x + 28}" y="52" class="m" font-size="13" fill="{index_fill}">{index}</text>']
    y = 108
    for line in title_lines:
        parts.append(f'    <text x="{x + 28}" y="{y}" class="h" font-size="30" fill="{title_fill}">{line}</text>')
        y += 36
    y += 6
    for line in sub_lines:
        parts.append(f'    <text x="{x + 28}" y="{y}" class="m" font-size="13" fill="{sub_fill}" opacity=".8" letter-spacing="0.5">{line}</text>')
        y += 22
    if link_label:
        parts.append(f'    <text x="{x + 28}" y="{h - 22}" class="m" font-size="12" fill="{link_fill}">{link_label}</text>')
    parts.append('  </g>')
    return "\n".join(parts)


def pillars() -> None:
    h = 174
    body = "\n".join([
        card(8, 284, h, PAPER_LIGHT, INK, "01 / QUALITY", ORANGE,
             ["Test strategy"], INK, ["Release confidence and", "trustworthy signals"], MUTED),
        card(306, 284, h, INK, TEAL_LIGHT, "02 / CLOUD", TEAL_LIGHT,
             ["Event-driven AWS"], PAPER_LIGHT, ["Explicit ownership and", "least-privilege design"], PAPER),
        card(604, 284, h, TEAL, TEAL_LIGHT, "03 / AI SYSTEMS", TEAL_LIGHT,
             ["Bounded agents"], PAPER_LIGHT, ["Scoped tools, evidence,", "deterministic gates"], PAPER),
        card(902, 284, h, ORANGE, INK, "04 / OPERATIONS", INK,
             ["Safe recovery"], INK, ["Observable paths and", "obvious next actions"], "#3d2317"),
    ])
    svg("pillars.svg", 1200, h + 16, body,
        "Four disciplines: quality, cloud, AI systems, operations")


def workbench() -> None:
    h = card_height(["x", "x"], ["x", "x", "x"], link=True)
    left = card(8, 586, h, INK, TEAL_LIGHT, "NOW BUILDING", TEAL_LIGHT,
                ["Measurable AI quality"], PAPER_LIGHT,
                ["Deterministic benchmarks for agents,", "quality gates for generated code,",
                 "self-hosted automation with operator controls"], PAPER,
                "OPEN AI SYSTEMS →", ORANGE)
    right = card(608, 584, h, PAPER_LIGHT, TEAL, "HOW I WORK", ORANGE,
                 ["Understand · Design ·", "Validate · Operate"], INK,
                 ["The path after the happy path:", "timeouts, permissions, retries,",
                  "diagnostics, rollback, next action"], MUTED,
                 "READ THE PRINCIPLES →", TEAL)
    svg("workbench.svg", 1200, h + 16, left + "\n" + right,
        "The workbench: now building measurable AI quality; how I work: understand, design, validate, operate")


def featured() -> None:
    h = card_height(["x", "x"], ["x", "x"], link=True)
    specs = [
        ("featured-ai.svg", INK, TEAL_LIGHT, "01 / AI SYSTEMS", TEAL_LIGHT,
         ["Agents with", "boundaries"], PAPER_LIGHT,
         ["Skills, SOPs, scoped tools,", "evidence-based evaluation"], PAPER,
         "AGENT DESIGN / BENCHMARKS", ORANGE),
        ("featured-cloud.svg", TEAL, TEAL_LIGHT, "02 / CLOUD SYSTEMS", TEAL_LIGHT,
         ["Infrastructure that", "explains itself"], PAPER_LIGHT,
         ["Clear ownership, least privilege,", "safe delivery, useful diagnostics"], PAPER,
         "AWS CDK / LAMBDA / SNS / IAM", "#ffd9cc"),
        ("featured-quality.svg", ORANGE, INK, "03 / QUALITY PLATFORMS", INK,
         ["Feedback that leads", "to a fix"], INK,
         ["Failure signals people can act on,", "across services, web, and devices"], "#3d2317",
         "API / UI / MOBILE / DEVTOOLS", INK),
    ]
    for name, bg, ring, index, index_fill, titles, tfill, subs, sfill, tag, tagfill in specs:
        body = card(8, 374, h, bg, ring, index, index_fill, titles, tfill, subs, sfill, tag, tagfill)
        svg(name, 390, h + 16, body, index)


def hero() -> None:
    body = f"""
  <rect width="1200" height="300" fill="{PAPER}"/>
  <rect width="1200" height="300" fill="url(#wash)"/>
  <defs>
    <radialGradient id="wash" cx="85%" cy="0%" r="70%">
      <stop offset="0%" stop-color="{TEAL_LIGHT}" stop-opacity=".55"/>
      <stop offset="100%" stop-color="{TEAL_LIGHT}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- orbit visual, echoing the site signal board -->
  <g transform="translate(985, 150)">
    <circle r="118" fill="none" stroke="{TEAL}" opacity=".3"/>
    <circle r="74" fill="none" stroke="{TEAL}" opacity=".45"/>
    <circle r="46" fill="{TEAL}"/>
    <text y="-2" text-anchor="middle" class="h" font-size="30" fill="{PAPER_LIGHT}">+</text>
    <text y="22" text-anchor="middle" class="m" font-size="10" fill="{TEAL_LIGHT}">TRUST</text>
    <circle cx="0" cy="-74" r="5" fill="{ORANGE}">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="16s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="-118" r="4" fill="{ORANGE}" opacity=".8">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="24s" repeatCount="indefinite"/>
    </circle>
  </g>

  <circle cx="52" cy="64" r="4.5" fill="{ORANGE}">
    <animate attributeName="opacity" values="1;.35;1" dur="2.6s" repeatCount="indefinite"/>
  </circle>
  <text x="72" y="69" class="m" font-size="14" fill="{TEAL}">QUALITY ENGINEERING · CLOUD · AI SYSTEMS</text>

  <text x="50" y="146" class="h" font-size="62" fill="{INK}">Make complex software</text>
  <text x="50" y="212" class="h" font-size="62" fill="{TEAL}">easier to trust.</text>

  <text x="52" y="262" class="m" font-size="14" fill="{MUTED}" letter-spacing="1">
    <tspan fill="{ORANGE}">—</tspan> Build feedback. Design for failure. Ship with confidence.</text>
"""
    svg("profile-hero.svg", 1200, 300, body,
        "Elanthingal Chandrasekaran — make complex software easier to trust. Quality engineering, cloud, AI systems.")


def section_heading(slug: str, number: str, label: str) -> None:
    """Full-width section heading bar used in the md pages instead of ## text."""
    body = f"""
  <rect width="1200" height="64" fill="{PAPER_LIGHT}"/>
  <rect width="1200" height="64" fill="none" stroke="{LINE}"/>
  <rect x="0" y="0" width="5" height="64" fill="{ORANGE}"/>
  <text x="30" y="40" class="m" font-size="13" fill="{ORANGE}">{number}</text>
  <text x="78" y="43" class="h" font-size="26" fill="{INK}">{label}</text>
  <circle cx="1160" cy="32" r="4" fill="{TEAL}" opacity=".55"/>
"""
    svg(f"h-{slug}.svg", 1200, 64, body, label)


def heartbeat() -> None:
    """Full-history contribution 'heartbeat': weekly totals from account
    creation to today, drawn as an ECG-style trace. Re-run this script to
    refresh the data snapshot."""
    url = "https://github-contributions-api.jogruber.de/v4/Elanthingal"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.load(resp)
    days = sorted(data["contributions"], key=lambda d: d["date"])
    total = sum(d["count"] for d in days)

    # weekly buckets
    weeks, bucket, bucket_year = [], 0, days[0]["date"][:4]
    for i, d in enumerate(days):
        bucket += d["count"]
        if i % 7 == 6 or i == len(days) - 1:
            weeks.append((d["date"][:4], bucket))
            bucket = 0
    peak = max(c for _, c in weeks) or 1

    w, h = 1200, 300
    left, right, top, bottom = 20, 20, 74, 60
    plot_w, plot_h = w - left - right, h - top - bottom
    n = len(weeks)
    pts = []
    for i, (_, c) in enumerate(weeks):
        x = left + plot_w * i / max(n - 1, 1)
        y = top + plot_h * (1 - c / peak)
        pts.append(f"{x:.1f},{y:.1f}")
    baseline = top + plot_h
    line = " ".join(pts)
    area = f"{left:.1f},{baseline:.1f} {line} {left + plot_w:.1f},{baseline:.1f}"

    # year tick marks at each January boundary
    ticks = []
    seen = set()
    for i, (year, _) in enumerate(weeks):
        if year not in seen:
            seen.add(year)
            x = left + plot_w * i / max(n - 1, 1)
            ticks.append(
                f'  <line x1="{x:.0f}" y1="{baseline}" x2="{x:.0f}" y2="{baseline + 8}" stroke="{LINE}"/>\n'
                f'  <text x="{x:.0f}" y="{baseline + 28}" text-anchor="middle" class="m" font-size="11" fill="{MUTED}">{year}</text>')

    body = f"""
  <rect width="{w}" height="{h}" fill="{INK}"/>
  <circle cx="1140" cy="40" r="70" fill="none" stroke="{TEAL_LIGHT}" opacity=".14"/>
  <circle cx="46" cy="40" r="4" fill="{ORANGE}"/>
  <text x="66" y="45" class="m" font-size="13" fill="{TEAL_LIGHT}">COMMIT HEARTBEAT / {days[0]['date'][:4]} — PRESENT</text>
  <text x="{w - 30}" y="45" text-anchor="end" class="h" font-size="22" fill="{PAPER_LIGHT}">{total:,} contributions</text>
  <polygon points="{area}" fill="{TEAL}" opacity=".28"/>
  <polyline points="{line}" fill="none" stroke="{TEAL_LIGHT}" stroke-width="1.6" stroke-linejoin="round"/>
  <line x1="{left}" y1="{baseline}" x2="{left + plot_w}" y2="{baseline}" stroke="rgba(185,238,232,.3)"/>
{"".join(ticks)}
"""
    # ticks render on dark bg — restyle their fills
    body = body.replace(f'stroke="{LINE}"', 'stroke="rgba(185,238,232,.35)"')
    body = body.replace(f'fill="{MUTED}"', 'fill="rgba(243,240,233,.55)"')
    svg("heartbeat.svg", w, h, body,
        f"Commit heartbeat: {total:,} GitHub contributions from {days[0]['date'][:4]} to present, shown as weekly activity")


def tagline() -> None:
    body = f"""
  <text x="600" y="52" text-anchor="middle" class="h" font-size="40" fill="{INK}">Engineering systems that are <tspan fill="{TEAL}">easier to trust.</tspan></text>
  <text x="600" y="96" text-anchor="middle" class="m" font-size="14.5" fill="{MUTED}">I am a Senior SDET building quality platforms, cloud automation, and</text>
  <text x="600" y="120" text-anchor="middle" class="m" font-size="14.5" fill="{MUTED}">measurable AI workflows that turn complex failure into useful feedback.</text>
"""
    svg("tagline.svg", 1200, 140, body,
        "Engineering systems that are easier to trust. I am a Senior SDET building quality platforms, cloud automation, and measurable AI workflows.")


def motto() -> None:
    body = f"""
  <rect x="530" y="14" width="140" height="2" fill="{ORANGE}"/>
  <text x="600" y="58" text-anchor="middle" class="h" font-size="24" fill="{INK}">Build feedback. Design for failure. Ship with confidence.</text>
  <text x="600" y="92" text-anchor="middle" class="m" font-size="12.5" fill="{MUTED}">Thanks for stopping by. Follow along or reach out if you are building something difficult.</text>
"""
    svg("motto.svg", 1200, 112, body,
        "Build feedback. Design for failure. Ship with confidence.")


def nav_chips() -> None:
    # DM Mono at 12px is ~7.3px per char; chip width = text + padding
    items = [
        ("home", "HOME"),
        ("experience", "EXPERIENCE"),
        ("projects", "PROJECTS"),
        ("ai", "AI SYSTEMS"),
        ("aws", "AWS WORK"),
        ("content", "CONTENT"),
        ("contact", "CONTACT"),
    ]
    for slug, label in items:
        w = int(len(label) * 8.6) + 36
        body = f"""
  <rect x="1" y="1" width="{w - 2}" height="30" fill="{PAPER_LIGHT}" stroke="{LINE}"/>
  <text x="{w / 2}" y="21" text-anchor="middle" class="m" font-size="12" fill="{MUTED}">{label}</text>
"""
        svg(f"nav-{slug}.svg", w, 32, body, label)


def link_chips() -> None:
    """Footer / call-to-action link chips: same shape as nav chips but in the
    accent orange so they read as links on GitHub (where raw text links render
    in default blue and cannot be CSS-styled)."""
    items = [
        ("back-home", "← BACK TO HOME"),
        ("connect-linkedin", "CONNECT ON LINKEDIN ↗"),
        ("open-site", "OPEN PORTFOLIO SITE ↗"),
        ("work-with-me", "WORK WITH ME ↗"),
        ("see-systems", "SEE THE SYSTEMS →"),
        ("youtube", "YOUTUBE CHANNEL ↗"),
        ("github", "GITHUB ↗"),
        ("x", "X / TWITTER ↗"),
        ("instagram", "INSTAGRAM ↗"),
        ("linkedin", "LINKEDIN ↗"),
    ]
    for slug, label in items:
        w = int(len(label) * 8.6) + 36
        body = f"""
  <rect x="1" y="1" width="{w - 2}" height="30" fill="{PAPER_LIGHT}" stroke="{LINE}"/>
  <text x="{w / 2}" y="21" text-anchor="middle" class="m" font-size="12" fill="{ORANGE}">{label}</text>
"""
        svg(f"link-{slug}.svg", w, 32, body, label)


if __name__ == "__main__":
    print("Generating SVG assets:")
    for slug, num, label in [
        ("workbench", "01", "The Workbench"),
        ("featured", "02", "Featured Systems"),
        ("toolbox", "03", "Toolbox"),
        ("agent-design", "01", "Agent Design"),
        ("architecture", "02", "Engineering Architecture"),
        ("benchmarks", "03", "Deterministic Benchmarks"),
        ("eval-patterns", "04", "Practical Evaluation Patterns"),
        ("trustworthy", "05", "Making LLM Evaluation Trustworthy"),
        ("why", "06", "Why This Matters"),
        ("iac", "01", "Infrastructure as Code"),
        ("compute", "02", "Compute and Events"),
        ("network", "03", "Networking and Security"),
        ("approach", "04", "Engineering Approach"),
        ("arch-shape", "05", "Architecture Shape"),
        ("quality-eng", "01", "Quality Engineering"),
        ("strengths", "02", "Engineering Strengths"),
        ("principles", "03", "Working Principles"),
        ("glance", "04", "At a Glance"),
        ("cloud-systems", "01", "Cloud Analysis and Automation"),
        ("quality-platforms", "02", "Quality Engineering Platforms"),
        ("ai-benchmarks", "03", "AI Agents and Benchmarks"),
        ("self-hosted", "04", "Self-Hosted Automation"),
        ("evaluate", "05", "How I Evaluate a System"),
        ("activity", "04", "Commit Activity"),
        ("youtube", "01", "YouTube"),
        ("social", "02", "Social Profiles"),
    ]:
        section_heading(slug, num, label)
    heartbeat()
    tagline()
    motto()
    nav_chips()
    link_chips()
    hero()
    pillars()
    workbench()
    featured()
    for slug, eyebrow, heading, accent in [
        ("experience", "PRINCIPLES AND STRENGTHS", "Experience", ORANGE),
        ("projects", "PROBLEM / ARCHITECTURE / OUTCOME", "Projects", TEAL),
        ("ai", "AGENTS AND EVALUATION", "AI Systems", TEAL),
        ("aws", "CLOUD PATTERNS", "AWS Work", ORANGE),
        ("content", "VIDEOS AND CHANNELS", "Content", TEAL),
        ("contact", "OPEN CHANNEL", "Contact", ORANGE),
    ]:
        page_header(slug, eyebrow, heading, accent)
