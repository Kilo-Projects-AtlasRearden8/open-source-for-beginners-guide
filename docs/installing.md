# Installing Open-Source Software

There are two main ways to get open-source software: download a ready-to-use
release, or install it from the source code. This guide covers both in plain
English.

## Option A: Download a release (easiest)

Many projects offer "releases" — pre-built versions you can download and run.

1. Go to the project's GitHub page.
2. Look for a **Releases** section on the right side, or click **Releases** in
   the top menu.
3. Find the latest release (usually at the top).
4. Download the file for your computer:
   - Windows: `.exe` or `.msi`
   - Mac: `.dmg` or `.pkg`
   - Linux: `.AppImage`, `.deb`, or source tarball
5. Open the file and follow the installer.

## Option B: Install from source code

If there is no release, you can install from the code yourself. The README
usually has exact instructions. Common patterns:

### If the project is a Python tool

1. Install Python from python.org if you do not have it.
2. Open a terminal (Command Prompt, PowerShell, or Terminal).
3. Run: `pip install <project-name>`
   Or, if the project gives a GitHub URL: `pip install git+https://github.com/owner/repo.git`

### If the project is a Node.js tool

1. Install Node.js from nodejs.org.
2. Open a terminal.
3. Run: `npm install -g <project-name>`

### If the project gives build instructions

Follow the README step by step. Common commands you might see:

- `git clone https://github.com/owner/repo.git` — downloads the code
- `cd repo` — enters the project folder
- `npm install` or `pip install -r requirements.txt` — installs dependencies
- `npm start` or `python main.py` — runs the program

## If you get stuck

- Read the README again. The answer is usually there.
- Search the project's **Issues** tab for your error message.
- Open a new issue if you cannot find an answer (see
  [reporting-issues.md](reporting-issues.md)).

## Credit

Written by **Asdale Dynamics, LLC**. Copyright (c) 2026 Asdale Dynamics, LLC.
Licensed under the MIT License.
