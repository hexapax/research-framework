# Setting Up Your Research Workstation

You need four tools installed before you can start researching. A fifth one is optional but nice. None of them require any technical knowledge to install, and you only need to do this once.

This guide walks you through each one. If you already have something installed, skip to the verification step to make sure it's working.

---

## 1. Claude Code Desktop

**What it is:** An AI assistant that lives on your computer. It can read your files, search the web, and follow step-by-step research workflows. This is the tool you'll spend most of your time in.

**Why you need it:** Claude Code Desktop is the engine behind this entire framework. When you type `/collect` or `/search`, Claude is the one doing the work. It reads your project's instructions (CLAUDE.md), understands your data schema, and helps you build a structured research dataset through conversation.

**You'll need:** A Claude Pro or Max subscription from Anthropic ($20/month or $100/month). The Pro plan is fine to start with.

### Installation steps

1. Open your web browser and go to [claude.ai/download](https://claude.ai/download)
2. Click the **Windows** download button
3. Open the downloaded file and follow the installer prompts -- the defaults are fine
4. When it finishes, open Claude Code Desktop from your Start menu
5. Sign in with your Anthropic account (the same one you use for claude.ai)
6. You'll see a window with a text input area at the bottom -- this is where you'll type

**Don't be intimidated by the interface.** It looks like a terminal, but you're just typing plain English. The only special things you'll type are slash commands like `/collect`, and those are just shortcuts.

### How to verify it worked

Type `hello` and press Enter. Claude should respond with a greeting. If it does, you're good.

If you see an error about signing in, double-check that you have an active Claude Pro or Max subscription at [claude.ai/settings](https://claude.ai/settings).

---

## 2. Git

**What it is:** A tool that tracks every change you make to your files. Think of it as unlimited "undo" that remembers everything, forever.

**Why you need it:** Git runs quietly in the background. You won't interact with it directly -- Claude and GitHub Desktop (the next tool) handle that for you. But it needs to be installed for those tools to work.

### Installation steps

1. Go to [git-scm.com/downloads](https://git-scm.com/downloads)
2. Click **Windows** and download the installer
3. Run the installer
4. **Click "Next" on every screen.** The default settings are exactly right. You don't need to understand any of the options it asks about -- just keep clicking Next until it finishes.
5. Click "Finish" when it's done

That's it. You won't open Git directly. It just needs to exist on your computer.

### How to verify it worked

1. Press the Windows key, type `cmd`, and press Enter to open Command Prompt
2. Type `git --version` and press Enter
3. You should see something like `git version 2.47.1.windows.1` (the exact number doesn't matter)
4. Close the Command Prompt window

If you see "git is not recognized," try restarting your computer and checking again. The installer sometimes needs a restart to take effect.

---

## 3. GitHub Desktop

**What it is:** A visual app for managing your research project's history. It shows you what changed, when, and lets you back up your work to the cloud.

**Why you need it:** While Claude handles the day-to-day file tracking (through the `/save` skill), GitHub Desktop gives you a visual way to browse your project's history, push your work to an online backup, and share your project with collaborators. Think of it as the "save points" screen in a video game -- you can see every save, what changed, and go back if needed.

### Installation steps

1. Go to [desktop.github.com](https://desktop.github.com/)
2. Click **Download for Windows**
3. Run the installer -- it will open automatically when done
4. Click **Sign in to GitHub.com**
   - If you already have a GitHub account, sign in
   - If you don't, click "Create an account" and follow the steps (it's free)
5. On the "Configure Git" screen, your name and email should be pre-filled. Click **Finish**.

### How to verify it worked

You should see the GitHub Desktop main screen with options to create a new repository, add an existing one, or clone from the internet. If you see that, you're set. You'll come back to this tool later when you start your project.

---

## 4. Python

**What it is:** A programming language that runs the scripts that turn your research files into spreadsheets. You won't write Python code -- Claude and the framework handle that -- but Python needs to be installed so those scripts can run.

**Why you need it:** When you run `/export`, a Python script reads all your research files and combines them into a CSV or Excel file you can open in a spreadsheet. No Python, no spreadsheets.

### Installation steps

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click the big yellow **Download Python** button (it will be the latest version)
3. Run the downloaded installer
4. **THIS IS THE CRITICAL STEP:** On the very first screen of the installer, look at the bottom. There's a checkbox that says **"Add Python to PATH."** **Check that box.** If you miss this, Python will be installed but nothing will be able to find it.
5. Click **Install Now** (not "Customize installation" -- the defaults are fine)
6. Wait for it to finish and click **Close**

### How to verify it worked

1. Press the Windows key, type `cmd`, and press Enter to open Command Prompt
2. Type `python --version` and press Enter
3. You should see something like `Python 3.12.4` (the exact number doesn't matter, as long as it starts with 3)
4. Close the Command Prompt window

**If you see "python is not recognized":**
- You probably missed the "Add to PATH" checkbox. The easiest fix is to uninstall Python (Settings > Apps > Python > Uninstall) and reinstall it, making sure to check that box this time.
- If you'd rather not reinstall, restart your computer first -- sometimes that's all it takes.

**If it says Python 2.something:** You have an old version. Install the latest from python.org alongside it. On some systems you may need to type `python3 --version` instead.

---

## 5. VS Code (OPTIONAL)

**What it is:** A text editor made by Microsoft. It's good for reading and browsing your research files, but it's not required.

**Why you might want it:** Claude Code Desktop is where you'll do your research, but sometimes you want to browse through your files, read a record side by side with another one, or look at your schema without interrupting a conversation with Claude. VS Code makes that easy. It also has a nice YAML syntax highlighter that color-codes your record files, which makes them easier to read.

**Why it's optional:** Everything VS Code does, you can also do through Claude ("show me the contents of DEST-003.md") or through File Explorer. VS Code is just more comfortable for file browsing.

### Installation steps

1. Go to [code.visualstudio.com](https://code.visualstudio.com/)
2. Click the big blue **Download for Windows** button
3. Run the installer
4. On the "Select Additional Tasks" screen, check **"Add to PATH"** and **"Register Code as an editor for supported file types"** (both are helpful but not required)
5. Click "Next" through the remaining screens and then "Finish"

### How to verify it worked

Open VS Code from your Start menu. You should see a welcome screen. You can close it -- you'll use it later when you want to browse your project files.

**Nice to have:** If you install the "Front Matter CMS" extension (click the Extensions icon on the left sidebar, search for "Front Matter CMS"), it gives you a form-based view of YAML frontmatter. This means you can edit your record files through dropdown menus and text boxes instead of editing the YAML text directly. Completely optional, but some people find it more comfortable.

---

## You're done with setup

All the tools are installed. Here's what you have now:

| Tool | What it does for you |
|------|---------------------|
| **Claude Code Desktop** | Your AI research assistant -- where you'll spend your time |
| **Git** | Tracks every change (runs silently in the background) |
| **GitHub Desktop** | Visual history browser and cloud backup |
| **Python** | Powers the export scripts (runs behind the scenes) |
| **VS Code** (optional) | File browser with nice YAML highlighting |

**Next step:** Open `docs/02-your-first-project.md` or follow the tutorial in `GETTING-STARTED.md`.

---

## Troubleshooting

**"I installed something but the verification step failed."**
Restart your computer. Many Windows installers need a restart before their commands are available in the Command Prompt.

**"The Command Prompt says 'is not recognized' for everything."**
This usually means the tool wasn't added to your system PATH. For Python, reinstall with "Add to PATH" checked. For Git, the installer should handle this automatically -- try restarting first.

**"I'm on a Mac, not Windows."**
The same tools are available for Mac. Go to the same download pages and choose the Mac versions. The main difference: you don't need to worry about the "Add to PATH" checkbox for Python on Mac -- it handles that automatically.

**"Do I need to pay for anything?"**
Claude Code Desktop requires a Claude Pro ($20/month) or Max ($100/month) subscription. Everything else is free. Pro is enough to start with.

**"Claude Code Desktop looks like a hacker tool. Am I going to break something?"**
No. You're typing in plain English, and Claude does the technical work. The terminal-style interface is just how Claude Code works -- it's designed for typing, not for clicking buttons. You'll get comfortable with it quickly.
