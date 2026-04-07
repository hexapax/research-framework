---
name: collect
description: Add a new record to the research dataset by walking through structured data collection
user-invocable: true
argument-hint: "[brief description of what you found]"
---

# Collect: Add a New Record

Walk the user through adding a new record to the dataset. Ask questions, check for duplicates, create the file, and set the verification level.

## When to Use

Run `/collect` when you've found something that should be in the dataset -- a new incident, case, entry, or data point from a source. You can also just say what you found in plain language and Claude will suggest running this skill.

## Workflow

### Step 1: Understand What Was Found

If the user provided an argument (e.g., `/collect measles outbreak in Ohio 2023`), use that as the starting point. Otherwise, ask:

1. "What did you find?" (brief description)
2. "Where did you find it?" (source URL, publication name, or description)
3. "When did this happen?" (date or approximate date)
4. "Where did this happen?" (location)

Don't ask all questions at once -- ask them conversationally, one or two at a time.

### Step 2: Check for Duplicates

Before creating a new file, search existing records for potential matches:

```bash
# Search by key terms the user mentioned
grep -rl "[key term]" dataset/*.md
```

Check for matches on:
- Date (allow +/- 1 year -- source dates are often wrong)
- Location (check city, state, and broader region)
- Key identifying details (names, specific descriptions)

**If a potential match is found:**
- Show the user the existing record's key fields
- Ask: "This looks like it might be the same thing. Is it?"
- If yes: offer to update the existing record instead of creating a new one
- If no: proceed with creating a new record
- If unclear: flag it as "POSSIBLE DUPLICATE" in the new record's `research_notes`

### Step 3: Determine the Next ID

Read SCHEMA.md to understand the file naming convention, then find the next available ID:

```bash
ls dataset/*.md | grep -v SCHEMA | sort | tail -1
```

### Step 4: Gather Remaining Fields

Read `dataset/SCHEMA.md` to get the full list of fields. For each required field, either:
- Extract it from what the user already told you
- Ask the user for it
- Mark it as unknown/empty if the user doesn't have it yet

Don't make the user answer 20 questions. Fill in what you can from the source, ask about the essentials, and leave the rest for later verification.

### Step 5: Assess Source Quality

Before setting the verification level, evaluate the source:
- Read the Source Rules in `CLAUDE.md` to check if this source is independent
- Ask if needed: "Is [source] independent from [subject of study], or does it derive from it?"

### Step 6: Create the File

Create the record file in `dataset/` following the naming convention from SCHEMA.md. The file must have:

1. YAML frontmatter between `---` markers with all fields from the schema
2. Markdown body with a summary section

Use the example record in SCHEMA.md as the template. Fill in known values, leave unknown values empty (not "Unknown" -- just empty or omitted).

Set `verification_level` based on what sources exist:
- VERIFIED: 2+ independent sources confirm key facts
- CONFIRMED: 1 independent source
- UNVERIFIED: Only the subject-of-study source, or no independent verification

### Step 7: Confirm and Remind

After creating the file:
1. Show the user what was created (filename and key fields)
2. Note what's still missing: "These fields are empty and could be filled in with more research: [list]"
3. Remind: "Run `/export` to update the CSV, or `/verify` to search for additional sources."

## Error Handling

- **SCHEMA.md not found:** Ask the user what fields they want to track. Create a minimal record with the basics (ID, date, location, description, source, verification_level). Suggest creating a SCHEMA.md.
- **User doesn't know the date:** Use `date_precision: unknown` or `year` and fill in what's known.
- **Duplicate detection is ambiguous:** Create the record but add a note in `research_notes`: "POSSIBLE DUPLICATE: see [other file]. Needs manual review."
- **Source URL is paywalled:** Note this in the source entry. The record can still be created -- the paywall is a limitation, not a blocker.

## References

- Read `CLAUDE.md` for project-specific source rules and conventions
- Read `dataset/SCHEMA.md` for field definitions, naming convention, and example record
