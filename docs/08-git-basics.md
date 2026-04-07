# Saving and Tracking Your Work with Git

**Git** remembers every version of every file you've ever saved.

That's it. That's what git does. Everything else is details. This guide covers only what you need to know to save your work, back it up, and feel confident that nothing is ever truly lost.


## The Video Game Analogy

Think of git like save points in a video game.

Every time you save, the game remembers exactly where you were -- your position, your inventory, your progress. If you mess something up, you can load an earlier save and try again. The game doesn't delete your old saves when you make a new one. They're all still there.

Git works the same way for your files. Each save point (called a **commit**) captures a snapshot of your entire project at that moment. You can always go back and see what any file looked like at any previous save point.

The difference from a video game: git doesn't just save where you are. It also records a short description of what you did. "Added 5 new outbreak records." "Fixed the date on REC-2024-003." "Ran data quality check and cleaned up state abbreviations." Those descriptions make it easy to find the save point you want.


## Using /save

The `/save` skill is how you create a save point. Here's what happens when you type it:

1. **Claude checks what changed.** It looks at which files you've added, modified, or removed since your last save.

2. **Claude summarizes the changes.** In plain language: "Added 3 new records. Updated verification on 2 records. Regenerated the CSV export."

3. **Claude creates the save point.** Your changes are saved with a descriptive message. The save is stored locally on your computer.

4. **Claude reminds you to back up.** "To copy this save to the cloud, open GitHub Desktop and click Push."

That's the whole process. You describe what you did (or let Claude figure it out from the changes), and it's saved.


## GitHub Desktop: The Visual Way

**GitHub Desktop** is a free application that shows you your git history visually. It's the recommended way to browse your saves, back up to the cloud, and collaborate with others.

You don't need to use GitHub Desktop to save your work -- `/save` handles that. But GitHub Desktop is useful for:

- **Seeing your history.** The History tab shows every save point in chronological order. Click any one to see exactly what changed.
- **Backing up to the cloud.** Click "Push origin" to copy all your local saves to GitHub. If your computer dies, your work is safe.
- **Getting a collaborator's changes.** Click "Pull origin" to download their latest saves.

If you haven't installed GitHub Desktop yet, see the setup guide (01-setup-windows.md).


## Key Concepts

Here are the only terms you need to know right now:

**Commit** -- A save point with a label. Each commit captures the state of your project at one moment in time, plus a short description of what changed. Created by the `/save` skill.

**Push** -- Copy your save points to the cloud. Think of it as a backup. You do this in GitHub Desktop by clicking "Push origin." Your saves exist on your computer until you push them; after pushing, they also exist on GitHub's servers.

**Pull** -- Get your collaborator's save points from the cloud. If someone else pushed changes to the project, pulling brings their work to your computer. You do this in GitHub Desktop by clicking "Pull origin."

**Branch** -- A parallel universe for trying something without affecting your main work. You don't need to use branches yet. They exist, and they're useful when your project gets more complex, but they're an advanced topic for another day.

That's it. Four concepts. Commit, push, pull, and "branches exist but you don't need them yet."


## When to Save

There's no wrong time to save, but here are the moments when it matters most:

**After every productive session.** If you spent 30 minutes adding records or verifying data, save before you close your laptop.

**When you've added or changed records.** Each batch of changes deserves its own save point. "Added 4 new records from CDC data" is a good save. "Added records, changed the schema, rewrote the export script, and deleted three files" is too much in one save -- break it up next time.

**Before you try something risky.** About to reorganize your folder structure? Change a bunch of records at once? Modify the export script? Save first. That way, if the experiment goes wrong, you have a clean save point to return to.

**Before you close the project for the day.** Make it a habit. Save, then (optionally) push to GitHub for backup.


## The .gitignore File

Some files shouldn't be saved. API keys, temporary files, operating system junk, Python cache files -- these clutter up your history and can even be a security risk.

The **`.gitignore`** file tells git which files to ignore. The template project comes with a `.gitignore` that's already set up to exclude the common offenders:

- `.env` files (which might contain API keys)
- `__pycache__/` folders (Python temporary files)
- `.DS_Store` (macOS system files)
- `Thumbs.db` (Windows system files)
- `.mcp.json` (which can contain API keys for MCP tools)

You don't need to edit this file unless you have a specific reason to. The template handles the defaults for you.


## What to Do If Something Goes Wrong

The most important thing: **don't panic.** Git saved everything. That's literally what it's for.

**"I changed a file and now it's broken."** Open GitHub Desktop. Go to the Changes tab. Right-click the file and choose "Discard Changes." The file goes back to the way it was at your last save.

**"I need to see what a file looked like before."** Open GitHub Desktop. Go to the History tab. Click through your save points until you find the version you want. You can see exactly what every file looked like at that moment.

**"I deleted a file I shouldn't have."** If you saved (committed) before deleting, the file is in your history. You can find it in GitHub Desktop's History tab and recover it. If you didn't save before deleting, that's a good reminder to save more often.

**"I haven't pushed in a while and I'm nervous."** Open GitHub Desktop and click "Push origin." All your local saves get backed up to GitHub. Do this whenever you want peace of mind.

**"Something is really messed up and I don't know what happened."** Ask Claude. Describe what you see. Claude can look at the git history and help you figure out what changed and how to fix it. Git keeps a record of everything, so even complicated situations are usually recoverable.

The one thing that's hard to recover from: changes you never saved. If you spent an hour working and never ran `/save` or made a commit, git doesn't have a record of that work. That's why the habit matters: save early, save often.
