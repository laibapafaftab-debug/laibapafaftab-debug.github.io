# Laiba.dev | Portfolio

Personal portfolio of **Laiba Aftab**, a web developer and Python automation builder based in Pakistan, working with clients worldwide.

**Live site:** https://laiba-portfoilo.netlify.app/

![Status](https://img.shields.io/badge/status-available%20for%20work-brightgreen)
![Built with](https://img.shields.io/badge/built%20with-HTML%20%7C%20CSS%20%7C%20JavaScript-blue)
![Hosted on](https://img.shields.io/badge/hosted%20on-Netlify-00C7B7)

---

## About

I design fast, mobile-friendly, conversion-focused websites and Python automation tools for small businesses, startups and independent professionals. This repository contains my portfolio site and the demo projects linked from it.

## Features

- Responsive layout for mobile, tablet and desktop
- Animated hero with a rotating role line, particle background and loading screen
- Scroll-reveal animations, scroll progress ring and scroll-to-top button
- Services, process, tech stack, pricing and case study sections
- Floating WhatsApp button and direct contact links
- Contact form powered by Formspree
- Google Analytics (gtag.js)
- Open Graph tags for link sharing
- Respects `prefers-reduced-motion`

## Demo projects

Each demo opens in a new tab from the **Recent projects** section.

| Project | Path | What it shows |
|---|---|---|
| Salon booking website | `/salon/` | Service menu with PKR prices, a live booking picker (service, day, time, details), and a confirmation with a shareable reference |
| Consulting firm site | `/consulting/` | A multi-view UK consultancy site with services, expandable case studies and a 3-step contact funnel |
| Python game | `/python-game/` | A demo video page for a Pygame project, with source link and run instructions |

> The salon and consulting sites are **demo concepts**. Bookings and enquiries on them are not sent to a real business, and sample figures on them are illustrative.

## Project structure

```
portfolio/
├── index.html              Main portfolio page
├── home.html               Home page
├── about.html              About page
├── services.html           Services page
├── education.html          Education page
├── skills.html             Skills page
├── favicon.svg
├── profile.jpg             Profile photo
├── coffee-heaven.jpg       Salon project thumbnail
├── social-campaigns.jpg    Consulting project thumbnail
├── portfilo.jpg            Python game thumbnail
├── salon/
│   └── index.html          Salon booking demo
├── consulting/
│   └── index.html          Consulting firm demo
├── python-game/
│   ├── index.html          Python game demo page
│   └── game-demo.mp4       Gameplay recording
└── README.md
```

## Tech stack

- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Python:** Python 3, Pygame (game project)
- **Fonts:** Space Grotesk, Inter, JetBrains Mono (Google Fonts)
- **Hosting:** Netlify
- **Forms:** Formspree
- **Analytics:** Google Analytics

## Run locally

No build step is needed.

```bash
git clone https://github.com/laibapafaftab-debug/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

Then open `index.html` in your browser, or serve the folder to test the demo links properly:

```bash
python -m http.server 8000
```

Visit `http://localhost:8000`.

## Deploy to Netlify

1. Put all files and folders in one project folder, as shown above.
2. Log in to Netlify and open the project, then go to **Deploys**.
3. Drag and drop the whole folder, or connect this GitHub repository for automatic deploys.
4. Check that `/salon/`, `/consulting/` and `/python-game/` all open.

## Customising the demos

Lines marked with `<!-- EDIT -->` in `python-game/index.html` are placeholders:

- Replace **My Python Game** with the real game name
- Save your screen recording as `game-demo.mp4` in the same folder
- Replace `YOUR-REPO-NAME` with the game's repository name
- Update the run command if the main file is not `main.py`

The salon and consulting demos keep their business names, prices and copy in plain HTML and a short script near the bottom of each file.

## Services I offer

- Business websites
- Landing pages
- E-commerce setup
- Website redesign
- Speed and performance fixes
- Python automation

Packages start at **$150** (Starter), **$350** (Business) and **from $600** (E-commerce). Typical turnaround is 10 to 21 days.

## Contact

- Website: https://laiba-aftab-portfolio.netlify.app
- Email: laibapafaftab@gmail.com
- WhatsApp: https://wa.me/923248957840
- LinkedIn: https://www.linkedin.com/in/laiba-aftab-211705420/
- GitHub: https://github.com/laibapafaftab-debug
- Instagram: https://www.instagram.com/thelaibaaftab/
- Fiverr: https://www.fiverr.com/s/1qr5Ra9

## License

© 2026 Laiba Aftab. All rights reserved. Please contact me before reusing the design or content.
