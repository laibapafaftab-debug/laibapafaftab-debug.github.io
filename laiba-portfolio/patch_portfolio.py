"""
Run this file in the SAME folder as your portfolio index.html:

    python patch_portfolio.py

It makes a backup (index.backup.html) and then changes only these parts:
  1. Adds the infinite-scroll skills + projects strip (CSS + HTML)
  2. Replaces the fake stats box with honest facts
  3. Marks salon + consulting as "Concept project"
  4. Replaces the case study (no invented numbers)
  5. Removes the fake client reviews, keeps the 2 real industry feedback cards, adds "Open for my first projects"
  6. Changes the 6th service to WhatsApp chatbots & automation
Everything else in your file stays exactly as it is.
"""
import re, shutil, sys

SRC = "index.html"
try:
    html = open(SRC, encoding="utf-8").read()
except FileNotFoundError:
    sys.exit("index.html nahi mili. Ye file usi folder mein rakhein jahan index.html hai.")

import os
if not os.path.exists("index.backup.html"):
    shutil.copy(SRC, "index.backup.html")   # original is saved only once
errors = []

def swap(old, new, label):
    global html
    if html.count(old) != 1:
        errors.append(f"{label}: text {html.count(old)} baar mila (1 hona chahiye)")
        return
    html = html.replace(old, new)

def swap_block(start, end, new, label):
    global html
    s, e = html.find(start), html.find(end)
    if s == -1 or e == -1 or e < s:
        errors.append(f"{label}: marker nahi mila")
        return
    html = html[:s] + new + "\n\n  " + html[e:]

# ---------- 1. CSS for the infinite scroll strip ----------
CSS = """
    /* ---------- INFINITE SCROLL STRIP ---------- */
    .marquee-section { padding: 0 0 30px; }
    .marquee {
      overflow: hidden; margin-bottom: 14px;
      -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
      mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
    }
    .marquee-track { display: flex; width: max-content; animation: marqueeLeft 40s linear infinite; }
    .marquee.reverse .marquee-track { animation-name: marqueeRight; animation-duration: 46s; }
    .marquee:hover .marquee-track { animation-play-state: paused; }
    .marquee-group { display: flex; gap: 14px; padding-right: 14px; }
    .marquee-chip {
      font-family: 'JetBrains Mono', monospace; font-size: 14px; white-space: nowrap;
      padding: 12px 22px; border-radius: 999px;
      background: var(--surface); border: 1px solid var(--border-strong); color: var(--text-dim);
    }
    .marquee-chip.project { color: var(--gold); background: var(--gold-soft); border-color: rgba(212,162,76,0.3); }
    @keyframes marqueeLeft { from { transform: translateX(0); } to { transform: translateX(-50%); } }
    @keyframes marqueeRight { from { transform: translateX(-50%); } to { transform: translateX(0); } }
    @media (prefers-reduced-motion: reduce) {
      .marquee-track { animation: none !important; width: auto; flex-wrap: wrap; }
      .marquee-group[aria-hidden="true"] { display: none; }
      .marquee-group { flex-wrap: wrap; }
      .marquee { -webkit-mask-image: none; mask-image: none; }
    }
  </style>"""
swap("</style>", CSS, "CSS")

# ---------- 2. Stats box + infinite strip ----------
def chips(items, cls=""):
    return "\n".join(f'          <span class="marquee-chip{cls}">{i}</span>' for i in items)

skills = ["HTML5", "CSS3", "JavaScript", "Python", "Pygame", "OOP", "Responsive design",
          "Canva", "Graphic design", "Social media", "WhatsApp chatbots", "AI automation"]
projects = ["Salon booking site (concept)", "Consulting firm site (concept)", "Python game",
            "Booking form flow", "Mobile-first layout", "WhatsApp chat flow"]

def group(items, cls="", hidden=False):
    attr = ' aria-hidden="true"' if hidden else ""
    return f'        <div class="marquee-group"{attr}>\n{chips(items, cls)}\n        </div>'

STATS = f"""<!-- STATS TERMINAL -->
  <section class="stats-band" style="padding:0;">
    <div class="terminal" style="padding-top:0; padding-bottom:0;">
      <div class="terminal-window reveal" style="margin:60px 0;">
        <div class="terminal-bar">
          <div class="dots"><span></span><span></span><span></span></div>
          about_me.log
        </div>
        <div class="terminal-body">
          <div class="stat-line">
            <div class="prompt">$ stack --main</div>
            <div class="stat-num">HTML · CSS · JS</div>
            <div class="stat-label">plus Python and Pygame</div>
          </div>
          <div class="stat-line">
            <div class="prompt">$ projects --concept</div>
            <div class="stat-num">3</div>
            <div class="stat-label">practice builds you can open below</div>
          </div>
          <div class="stat-line">
            <div class="prompt">$ layout --approach</div>
            <div class="stat-num">Mobile-first</div>
            <div class="stat-label">every page designed for phones first</div>
          </div>
          <div class="stat-line">
            <div class="prompt">$ turnaround --typical</div>
            <div class="stat-num">10–21 days</div>
            <div class="stat-label">depends on the size of the project</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- INFINITE SCROLL: SKILLS + PROJECTS -->
  <section class="marquee-section" aria-label="Skills and projects">
    <div class="marquee">
      <div class="marquee-track">
{group(skills)}
{group(skills, hidden=True)}
      </div>
    </div>
    <div class="marquee reverse">
      <div class="marquee-track">
{group(projects, " project")}
{group(projects, " project", hidden=True)}
      </div>
    </div>
  </section>
"""
swap_block("<!-- STATS TERMINAL -->", "<!-- SERVICES -->", STATS, "Stats box")

# ---------- 3. Project cards ----------
swap('<span class="project-tag">Local business</span>',
     '<span class="project-tag">Concept project</span>', "Salon tag")
swap('<span class="project-tag">International client</span>',
     '<span class="project-tag">Concept project</span>', "Consulting tag")
swap("<p>Service listing, booking form, and gallery for a beauty salon in Lahore.</p>",
     "<p>Concept project for a fictional beauty salon in Lahore: service list, 4-step booking form and a mobile-first layout.</p>",
     "Salon text")
swap("<p>Multi-page site with case studies and a contact funnel for a UK-based consultancy.</p>",
     "<p>Concept project for a fictional UK consultancy: clear service pages, case-study layout and a contact funnel.</p>",
     "Consulting text")
swap('<p class="section-sub">A few examples of the kind of work I do.</p>',
     '<p class="section-sub">Concept projects that show the kind of work I do.</p>', "Work subtitle")

# ---------- 4. Case study ----------
CASE = """<!-- CASE STUDY -->
  <section>
    <div class="eyebrow">Concept project</div>
    <h2 class="section-title reveal" style="margin-bottom:44px;">Designing a booking flow for phones</h2>
    <div class="case-study">
      <div>
        <div class="eyebrow" style="margin-bottom:10px;">Fictional salon — Lahore</div>
        <h3>A booking page built around one goal: make booking effortless</h3>
        <p>This is a practice project, not a client case. I built it to show how I plan a service business website so a customer can book from a phone in under a minute.</p>
        <ul class="case-list">
          <li>Mobile-first layout, checked on different screen sizes</li>
          <li>Simple 4-step booking form with a WhatsApp share option</li>
          <li>Clear service list with prices shown up front</li>
          <li>Plain, readable text and large tap targets</li>
        </ul>
        <a href="salon/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">Open the live demo</a>
      </div>
      <div class="case-metrics">
        <div class="metric reveal" style="transition-delay:0.00s"><div class="num">4 steps</div><div class="label">Service, day, time, details</div></div>
        <div class="metric reveal" style="transition-delay:0.08s"><div class="num">Mobile-first</div><div class="label">Designed for phones, then larger screens</div></div>
        <div class="metric reveal" style="transition-delay:0.16s"><div class="num">WhatsApp</div><div class="label">Booking reference can be shared</div></div>
        <div class="metric reveal" style="transition-delay:0.24s"><div class="num">PKR</div><div class="label">Fixed prices shown up front</div></div>
      </div>
    </div>
  </section>"""
swap_block("<!-- CASE STUDY -->", "<!-- Testimonials / Industry Validation Section -->", CASE, "Case study")

# ---------- 5. Testimonials -> honest section ----------
OPEN = """<!-- FEEDBACK FROM INDUSTRY CONNECTIONS -->
  <section>
    <div class="eyebrow">Feedback</div>
    <h2 class="section-title reveal" style="margin-bottom:44px;">Feedback from industry connections</h2>
    <div class="testi-grid">
      <div class="testi-card reveal" style="transition-delay:0.00s">
        <p class="quote">"I checked out the site — really nice work. I like how clear the site is about what you offer and how you connect the technical work back to actual business results. The process and pricing sections are especially easy to understand."</p>
        <div class="testi-who">
          <div class="testi-avatar">DW</div>
          <div><div class="name">Danielle Wilcott</div><div class="role">Industry feedback</div></div>
        </div>
      </div>
      <div class="testi-card reveal" style="transition-delay:0.08s">
        <p class="quote">"A simple, well-integrated system that saves time and reduces manual work can make a big difference. Businesses struggle with integrating different tools and setting up reliable workflows."</p>
        <div class="testi-who">
          <div class="testi-avatar">KK</div>
          <div><div class="name">Khalil Khan</div><div class="role">Industry insight: workflow automation</div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- OPEN FOR FIRST PROJECTS -->
  <section>
    <div class="eyebrow">Now booking</div>
    <h2 class="section-title reveal">Open for my first projects</h2>
    <p class="section-sub">I'm taking on a small number of new projects. Message me and I'll reply with a clear quote and timeline.</p>
    <a href="#contact" class="btn btn-primary">Tell me about your project</a>
  </section>"""
swap_block("<!-- Testimonials / Industry Validation Section -->", "<!-- PRICING -->", OPEN, "Testimonials")

# ---------- 6. Service card + footer link ----------
swap("<h3>Python automation</h3>", "<h3>WhatsApp chatbots &amp; automation</h3>", "Service title")
swap("<p>Scripts, tools and small applications that take repetitive work off your plate — built around how your business actually runs.</p>",
     "<p>WhatsApp chatbots, Python scripts and AI workflows that answer customers 24/7 and take repetitive work off your plate.</p>",
     "Service text")
swap('<li><a href="#services">Python Automation</a></li>',
     '<li><a href="#services">Chatbots &amp; Automation</a></li>', "Footer link")

if errors:
    print("KUCH CHEEZEIN NAHI BADLI. Ye masle mile:")
    for e in errors:
        print(" -", e)
    print("index.html ko touch nahi kiya gaya (backup bhi bana hua hai).")
    sys.exit(1)

open(SRC, "w", encoding="utf-8").write(html)
print("Ho gaya! index.html update ho gayi. Purani file: index.backup.html")
