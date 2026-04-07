# CLAUDE.md -- [YOUR PROJECT TITLE]

<!--
==========================================================================
WHAT IS THIS FILE?

This file is the "brain" of your research project. When you open your
project in Claude Code, Claude reads this file first. Everything here
teaches Claude how YOUR project works -- what you're researching, what
rules to follow, where files go, and how to help you.

Think of it as a permanent set of instructions you'd give to a research
assistant on their first day: "Here's what we're studying, here's how we
organize our work, here's what to never do."

HOW TO CUSTOMIZE IT:
- Replace every [BRACKETED PLACEHOLDER] with your specifics
- Read the comment blocks above each section -- they explain WHY the
  section exists and WHAT to put in it
- Delete the comment blocks once you understand them (or keep them --
  Claude ignores HTML comments)
- Look at the examples from the ESD drowning project for inspiration

You don't need to fill in everything on day one. Start with Project
Overview and Source Rules, then add more as your project grows.
==========================================================================
-->

This file helps Claude Code (or any AI coding assistant) understand the structure, conventions, and rules of this research project so it can guide a researcher in adding to and maintaining the repository correctly.

## Project Overview

<!--
WHY THIS SECTION EXISTS:
Claude needs to know what you're studying to give you relevant help. A
researcher studying measles outbreaks needs different search strategies
than someone studying housing prices or historical battles.

WHAT TO PUT HERE:
- One sentence: what is this project about?
- What is the primary output? (Usually: "a structured dataset of [things]")
- What is the current state? (How many records? What time period?)

EXAMPLE (from the ESD drowning project):
  "This is an epidemiological research project studying Electric Shock
   Drowning (ESD) -- deaths and injuries caused by AC electricity leaking
   from dock/marina wiring into fresh water. The project independently
   verifies, corrects, and expands the ESDPA incident list using only
   primary public sources.

   Current state: 193 documented incidents in a consolidated dataset,
   spanning 1981-2025."
-->

This is a research project studying **[YOUR TOPIC]** -- [one sentence explaining what this means and why it matters].

**Current state:** [X] records in the dataset (`dataset/`), covering [time period or scope].

## Repository Structure

<!--
WHY THIS SECTION EXISTS:
Claude needs a map of your project so it knows where to find things and
where to put new files. Update this as your project grows.
-->

```
[your-project]/
  CLAUDE.md                    # This file -- project instructions for Claude
  DATA-GOVERNANCE.md           # Data source rules, privacy, ethics
  research-plan.md             # What you're researching, why, and how

  dataset/                     # THE PRIMARY OUTPUT
    SCHEMA.md                  # Data dictionary -- defines every field
    exports/                   # Generated CSV/XLSX files
    [RECORD-PREFIX]-*.md       # One file per record (YAML frontmatter + markdown)

  source-data/                 # Raw inputs (PDFs, original lists, datasets under study)
    methodology/               # How source data was obtained

  findings/                    # Research output organized by search strategy
    (subdirectories by Line of Attack or search campaign)

  verification/                # Independent verification of claims/records

  reference/                   # Supporting docs, search terms, external data

  scripts/                     # Python export/analysis scripts
```

## Critical Rules

### Source Rules

<!--
WHY THIS SECTION EXISTS:
This is the single most important section in this file. It prevents
CIRCULAR SOURCING -- the research equivalent of citing yourself as proof.

If you're studying a list or dataset created by Organization X, then
Organization X's data is your SUBJECT, not your evidence. You need
INDEPENDENT sources to verify what Organization X claims.

WHAT TO PUT HERE:
- Which sources are you STUDYING? (These cannot verify themselves.)
- Which sources count as INDEPENDENT verification?
- Are there any websites that just copy/repost the data you're studying?
  List them here so Claude never uses them as evidence.

EXAMPLE (from the ESD project):
  The ESDPA maintains a list of drowning incidents. Websites like
  MikeHolt.com repost that list. So the rule is: "NEVER use ESDPA.org,
  MikeHolt.com, or OnTimeService.com as independent verification sources.
  These are the SUBJECT OF STUDY, not independent sources."

If your research doesn't have a specific source exclusion (for example,
you're collecting original data from scratch), you can simplify this
section to focus on what counts as a reliable source for your domain.
-->

**Source exclusion -- NEVER use these as independent verification:**
- [Source you are studying, e.g., "OrganizationX.org"]
- [Websites that repost/mirror that source]
- [Any other sources that would create circular reasoning]

These are the **subject of study**, not independent sources. Using them as verification creates circular sourcing. All verification must come from independent primary sources.

**What counts as an independent source for this project:**

| Source Type | Independent? | Good For |
|------------|-------------|----------|
| [e.g., Peer-reviewed journal articles] | Yes | [e.g., Confirmed data, methodology] |
| [e.g., Government reports (CDC, WHO)] | Yes | [e.g., Official statistics, case counts] |
| [e.g., News articles with original reporting] | Yes | [e.g., Local details, timelines] |
| [e.g., The organization's own website] | No | [e.g., Their claims -- the thing we're checking] |

### Data Governance

<!--
WHY THIS SECTION EXISTS:
Quick reference for the rules in DATA-GOVERNANCE.md. Claude checks this
before adding any data to make sure it belongs in this repository.
-->

- Read `DATA-GOVERNANCE.md` before adding any data
- All data must come from **[publicly available sources / your access basis]**
- [If applicable: Data from restricted sources goes in a separate private repo]
- [Any special handling rules, e.g., "This dataset contains names of individuals -- treat with appropriate care"]

## How to Add a Record

<!--
WHY THIS SECTION EXISTS:
This is the step-by-step procedure Claude follows when you say "I found
something new" or when the /collect skill runs. It ensures every record
is created consistently.

WHAT TO CUSTOMIZE:
- The file naming pattern (what prefix do your records use?)
- The duplicate-checking strategy (what fields identify a duplicate?)
- The minimal template (copy from SCHEMA.md and simplify)
- The verification level definitions

EXAMPLE (from the ESD project):
  Files are named ESD-YYYY-MM-DD-N.md (date-based).
  Duplicates are checked by victim name, date, and location.
  Five verification levels from VERIFIED to UNVERIFIED.
-->

### Step 1: Check for duplicates

Before creating a new entry, verify the record doesn't already exist:

```bash
# Search by [primary identifier, e.g., name, location, date]
grep -rl "[search term]" dataset/

# Search by [secondary identifier]
grep -rl "[search term]" dataset/
```

### Step 2: Create the dataset file

**File naming:** `dataset/[RECORD-PREFIX]-[IDENTIFIER].md`

<!--
Choose a naming convention that works for your data:
  - Date-based:  ESD-YYYY-MM-DD-N.md  (good for events/incidents)
  - Sequence:    DEST-NNN.md           (good for catalogs/inventories)
  - Code-based:  OB-[STATE]-YYYY-NNN.md (good for location+time data)
Replace [RECORD-PREFIX] and [IDENTIFIER] with your convention.
-->

Follow the schema in `dataset/SCHEMA.md` exactly. Every file must have:

1. **YAML frontmatter** between `---` markers with all required fields
2. **Markdown body** with a summary section

Minimal template:

```yaml
---
record_id: "[RECORD-PREFIX]-[IDENTIFIER]"
date: "YYYY-MM-DD"
# [Add your required fields here -- see SCHEMA.md]

verification_level: UNVERIFIED
sources: []
notes: ""
research_notes: ""
---

# [RECORD-PREFIX]-[IDENTIFIER]: [Brief description]

## Summary

[1-3 sentence description of this record]
```

### Step 3: Set the verification level

<!--
Define what each level means for YOUR project. The levels below are a
sensible default for most research. Adjust the criteria column to match
your domain. You can add or remove levels as needed.
-->

| Level | When to use |
|-------|------------|
| VERIFIED | Multiple independent sources confirm the key facts |
| CONFIRMED | One independent source confirms the record |
| PROBABLE | Strong circumstantial evidence but not directly confirmed |
| SUSPECTED | Circumstantial evidence only; needs further investigation |
| UNVERIFIED | No independent sources found yet |

### Step 4: Regenerate exports

After adding or modifying records:

```bash
python3 scripts/export_dataset.py
```

This regenerates the CSV file in `dataset/exports/`.

### Step 5: Save your work

Stage only the specific files you changed:

```bash
git add dataset/[your-new-file].md
git add dataset/exports/
git commit -m "Add [record ID]: [brief description]"
```

Or use the `/save` skill to let Claude handle this for you.

## How to Verify a Record

<!--
WHY THIS SECTION EXISTS:
Verification is what separates a curated research dataset from a copy-
paste list. This section teaches Claude how to help you check claims
against independent sources.

The key concept is SOURCE INDEPENDENCE: a source is independent if it
gathered its own information rather than copying from the source you're
already using.
-->

Verification means checking a record's claims against independent sources:

1. **Read the existing record** -- What does it claim? What sources does it cite?
2. **Search for independent sources** -- Find sources NOT derived from the ones already listed
3. **Compare claims** -- Do the independent sources agree with the record?
4. **Document discrepancies** -- If sources disagree, note it in `research_notes`. Do not hide disagreements -- they are valuable information.
5. **Update verification level** -- Upgrade if the record now meets a higher standard
6. **Update sources list** -- Add any new sources you found

## Tool Usage Rules

<!--
WHY THIS SECTION EXISTS:
If you have MCP tools installed (like Perplexity for web search, or
PubMed for academic papers), this section tells Claude WHEN to use each
tool. Without this, Claude might use expensive search tools for questions
it could answer from your own files, or use the wrong search tool for
your domain.

WHAT TO PUT HERE:
- Which tool to use for what kind of question
- When NOT to use external search (when the answer is in your own files)
- Any cost considerations

You can skip this section entirely if you're only using Claude's built-in
capabilities. Add it when you install your first MCP tool.
-->

- Use built-in web search for quick fact-checks and finding specific sources
- [If installed: Use Perplexity for broad research questions requiring multiple sources]
- [If installed: Use [domain-specific tool] for [specific searches]]
- Do NOT use web search when the answer is in our own dataset files -- always check existing records first
- Always check for duplicates in the dataset before searching externally

## Common Tasks

<!--
WHY THIS SECTION EXISTS:
These are cookbook recipes for things you do regularly. Claude uses these
as step-by-step guides. Add new tasks as you discover repeating patterns
in your research workflow.
-->

### "Search for a specific [record type]"
1. Search the existing dataset first: `grep -rl "[search term]" dataset/`
2. Search [primary external source] for [key identifiers]
3. Search [secondary external source] for corroboration
4. Cross-reference against existing dataset entries

### "Find new [records] in [a region/time period/category]"
1. Read `reference/` for search methodology and terms
2. Use [your search strategy] with [your keyword combinations]
3. Focus on [known gaps in your dataset]
4. Create dataset entries for confirmed findings

### "Analyze the dataset"
```bash
# Generate fresh exports
python3 scripts/export_dataset.py

# Quick stats
grep -c "verification_level: VERIFIED" dataset/*.md
grep -c "verification_level: UNVERIFIED" dataset/*.md
```

### "Update the exports"
```bash
python3 scripts/export_dataset.py
```

## What NOT to Do

<!--
WHY THIS SECTION EXISTS:
Guardrails prevent costly mistakes. Every "don't" here exists because
someone (or some AI) actually made this mistake in a real project.

The ESD project learned these the hard way:
- "Don't use ESDPA as a verification source" -- circular sourcing
- "Don't modify source-data files" -- preserving the original record
- "Don't delete entries" -- research integrity requires keeping the trail

WHAT TO PUT HERE:
Think about what would be the worst mistakes in your project. What would
compromise your data integrity? What would violate your source rules?
What would waste hours of work?
-->

- Do not use [your subject-of-study sources] as verification sources (see Source Rules above)
- Do not modify files in `source-data/` -- those are original extractions and should remain unchanged
- Do not delete dataset entries -- if a record is wrong, update its `verification_level` and add notes explaining why
- Do not commit large binary files (PDFs > 10MB, datasets > 50MB) -- use `.gitignore`
- [Add your own project-specific "don'ts" here]

## Key Files to Read Before Starting

1. `dataset/SCHEMA.md` -- The data dictionary. Understand the fields before adding records.
2. `DATA-GOVERNANCE.md` -- Privacy and source rules.
3. `research-plan.md` -- The research plan. What's done vs. what remains.

<!--
==========================================================================
GROWING THIS FILE

This file should grow with your project. After a few weeks of research,
you'll notice patterns -- things you keep explaining to Claude, mistakes
that keep happening, shortcuts that save time. Add them here.

Good additions over time:
- New "Common Tasks" recipes for things you do repeatedly
- New "What NOT to Do" entries when you discover a pitfall
- Updated record counts and project state in the Overview
- New source types in the Source Rules table
- Search terms and strategies that work well for your domain

If you find yourself giving Claude the same instruction three times in
different sessions, put it in this file so you never have to say it again.
==========================================================================
-->
