# Getting Started

Welcome! This guide takes you from zero to your first research dataset in about 75 minutes.

You don't need to know how to code. You don't need to understand git, YAML, or Python. You just need to follow the steps, and the system handles the rest.

---

## What You'll Need

1. **A computer** (Windows, Mac, or Linux)
2. **An internet connection**
3. **About 75 minutes** for your first session

## Step 1: Install Claude Code Desktop (10 minutes)

Claude Code Desktop is the AI assistant that powers this framework. It reads your files, searches the web, and follows the research workflows you'll be using.

1. Go to [claude.ai/download](https://claude.ai/download)
2. Download the version for your operating system
3. Install it and sign in with your Anthropic account (you'll need a Claude Pro or Max subscription)
4. Open Claude Code Desktop -- you should see a terminal-like interface

**Don't worry about the terminal.** You'll be typing plain English, not commands. The few slash commands you'll use (like `/collect`) are just shortcuts.

## Step 2: Install GitHub Desktop (5 minutes)

GitHub Desktop tracks every change you make to your research. Think of it as "save points in a video game" -- you can always see what you changed and when.

1. Go to [desktop.github.com](https://desktop.github.com/)
2. Download and install
3. Sign in with a GitHub account (create one at [github.com](https://github.com) if you don't have one)

You won't need to use GitHub Desktop during the tutorial, but it'll be ready for when you start your real project.

## Step 3: Install Python (5 minutes)

Python runs the export scripts that turn your research files into spreadsheets.

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest version for your operating system
3. **Important (Windows):** During installation, check the box that says **"Add Python to PATH"**
4. Finish the installation

## Step 4: Get This Repository (5 minutes)

Open GitHub Desktop and clone this repository:

1. File > Clone Repository
2. Choose the URL tab
3. Paste: `https://github.com/hexapax/research-framework`
4. Choose where to save it on your computer
5. Click "Clone"

Or, if you already have the files, just note where they are on your computer.

## Step 5: Run the Tutorial (50 minutes)

The tutorial is a **vacation planner** that teaches you the research workflow. You'll search for vacation destinations, structure the results into files, verify claims across sources, and export everything to a spreadsheet and an interactive webpage.

It sounds simple -- and it is -- but the skills transfer directly to real research. The system doesn't care if your records are vacation destinations or measles outbreaks.

### Open the tutorial in Claude Code Desktop

1. In Claude Code Desktop, open the `tutorial/` folder from this repository
2. Read `tutorial/TUTORIAL-GUIDE.md` for step-by-step instructions

The guide walks you through:
- Reading a sample record to understand the format
- Using `/collect` to add new destinations
- Using `/verify` to check claims against sources  
- Using `/clean` to find data quality issues
- Using `/export` to generate a CSV spreadsheet
- Opening the interactive review page in your browser
- Using `/save` to commit your work

### What you'll learn

By the end of the tutorial, you'll know how to:
- Add structured records to a dataset
- Verify claims using independent sources
- Spot and fix data quality issues
- Export your work to formats you can share
- Save your progress with version control

## Step 6: Start Your Real Project (15 minutes)

Once you've finished the tutorial:

1. Copy the `template/` folder to a new location on your computer
2. Rename it to your project (e.g., `measles-research/`)
3. Open it in Claude Code Desktop
4. Open `CLAUDE.md` and fill in the blanks:
   - What are you researching?
   - What are your source rules?
   - What counts as a record?
5. Open `dataset/SCHEMA.md` and define your fields
6. Start researching! Use `/collect` to add your first real record.

## What's Next

You don't need to read all the docs right away. Here's when to read what:

| When | Read |
|------|------|
| **Starting your project** | `docs/03-how-records-work.md` |
| **After 10+ records** | `docs/05-verification.md` |
| **Want to share your data** | `docs/07-exporting.md`, `docs/09-publishing.md` |
| **Want more powerful search** | `docs/10-mcp-tools.md` |
| **Keep repeating the same steps** | `docs/12-creating-skills.md` |

## Getting Help

- Type your question to Claude in Claude Code Desktop -- it knows your project through CLAUDE.md
- Check the `docs/` folder for reference guides
- Open an issue on this repository if something is broken or confusing

---

*This framework was built for researchers who are great at research and want AI to handle the filing. You bring the questions; the system keeps the answers organized.*
