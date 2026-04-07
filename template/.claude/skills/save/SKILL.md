---
name: save
description: Save your work by committing changes to git
user-invocable: true
---

# Save: Commit Your Changes

Create a git commit capturing your current work. This is a local save point -- your work is preserved in history even if you change things later.

## When to Use

Run `/save` after a productive research session -- adding records, verifying data, fixing issues. It's like hitting "save" in a document, but with a description of what you did.

## Workflow

### Step 1: Check What Changed

```bash
git status
```

Review the output. Categorize changes:
- New files (added records)
- Modified files (updated records, exports)
- Deleted files (if any -- unusual in research projects)

If nothing has changed: "No changes to save. Your last save is still current."

### Step 2: Summarize Changes in Plain Language

Describe what changed in terms the user understands:
- "Added 3 new records (REC-2024-008, REC-2024-009, REC-2024-010)"
- "Updated verification for REC-2024-003 (now CONFIRMED with 1 new source)"
- "Regenerated CSV export"
- "Fixed 2 data quality issues found by /clean"

Show this summary to the user before committing.

### Step 3: Stage the Right Files

Stage specific files -- do NOT use `git add -A` or `git add .` which can catch secrets or temp files.

**Always stage:**
- New and modified record files in `dataset/`
- Updated exports in `dataset/exports/`
- Updated SCHEMA.md, CLAUDE.md, or other project files

**Never stage:**
- `.env` files
- `.mcp.json` (contains API keys)
- `__pycache__/` or `.pyc` files
- OS files (`.DS_Store`, `Thumbs.db`)

```bash
git add dataset/REC-2024-008.md dataset/REC-2024-009.md dataset/exports/dataset.csv
```

### Step 4: Compose a Commit Message

Write a clear, concise commit message that describes the research activity:

```
Add 3 measles outbreak records (Ohio 2020-2022)

- REC-2024-008: Franklin County, Jan 2020, 15 cases (CONFIRMED)
- REC-2024-009: Cuyahoga County, Mar 2021, 8 cases (UNVERIFIED)
- REC-2024-010: Hamilton County, Nov 2022, 23 cases (VERIFIED)
```

Keep the first line under 70 characters. Add detail in the body if there's more to say.

### Step 5: Commit

```bash
git commit -m "commit message here"
```

### Step 6: Tell the User What Happened

After committing:
- "Saved! Your work is committed locally."
- "To back up to the cloud, open GitHub Desktop and click 'Push origin'."
- "You can see your save history in GitHub Desktop under the History tab."

Do NOT push to remote automatically. That's the user's choice via GitHub Desktop.

## Error Handling

- **Git not initialized:** "This project isn't set up with git yet. Want me to initialize it? (This just means your changes will be tracked from now on.)"
- **Nothing to commit:** "No changes since your last save."
- **Merge conflicts:** "There are conflicting changes. This usually happens when you edited the same file in two places. Let me show you the conflicts so you can decide which version to keep."
- **Large files:** If any staged file is over 50MB, warn the user and suggest adding it to `.gitignore`.

## References

- The `.gitignore` file controls what's excluded from saves
- GitHub Desktop provides a visual way to browse save history and push to remote
