# Starting Your Own Research Project

This guide walks you through creating your own research project from the framework template. By the end, you'll have a working project folder customized for your research, ready to collect your first record.

If you haven't completed the tutorial yet (the vacation planner in `GETTING-STARTED.md`), do that first. It takes about an hour and teaches you how the system works before you invest time setting up your real project.

---

## Step 1: Copy the Template

The `template/` directory in this repository is your starting point. It has all the folders, configuration files, and skills pre-built. You're going to copy it and make it your own.

### Using File Explorer (easiest)

1. Open File Explorer and navigate to where you cloned this repository
2. Find the `template/` folder
3. Copy it (right-click > Copy, or Ctrl+C)
4. Paste it wherever you keep your projects (your Documents folder, Desktop, or a dedicated research folder)
5. Rename the copied folder to your project name -- for example, `measles-research`

### Using GitHub Desktop (if you want version control from the start)

1. Open GitHub Desktop
2. Click **File > New Repository**
3. Name it (e.g., `measles-research`)
4. Choose where to save it
5. Click **Create Repository**
6. Open the new folder in File Explorer
7. Copy everything from `template/` into your new repository folder
8. Back in GitHub Desktop, you'll see all the new files. Commit them with a message like "Initial project setup from research framework template"

Either approach works. The GitHub Desktop route gives you version history from the very start, which is nice but not required on day one.

---

## Step 2: Open Your Project in Claude Code Desktop

1. Open Claude Code Desktop
2. Open your new project folder (e.g., `measles-research/`)
3. Claude will automatically read your `CLAUDE.md` file and understand your project

At this point, Claude knows the structure of your project but not the specifics of your research. That's what the next step is for.

---

## Step 3: Customize CLAUDE.md

`CLAUDE.md` is the most important file in your project. It's the set of instructions that teaches Claude how to help you. Every time you start a session, Claude reads this file first.

Open `CLAUDE.md` in your project. You'll see sections with `[BRACKETED PLACEHOLDERS]` and comment blocks (the text between `<!--` and `-->`) explaining what goes where. You don't need to fill in everything right now -- start with the three sections below.

### Section 1: Project Overview

Find the section that starts with `## Project Overview`. Replace the placeholder text with a description of your research.

**Before (template):**
```
This is a research project studying **[YOUR TOPIC]** -- [one sentence explaining
what this means and why it matters].

**Current state:** [X] records in the dataset, covering [time period or scope].
```

**After (measles example):**
```
This is a research project studying **measles outbreaks in the United States
since 2000** -- tracking confirmed outbreaks, their size, geographic spread,
and connection to vaccination coverage gaps.

**Current state:** 0 records in the dataset. Starting fresh.
```

The description doesn't need to be long or formal. One or two sentences that tell Claude what you're looking at and why.

### Section 2: Source Rules

Find the section that starts with `### Source Rules`. This is the most important section for research integrity. It tells Claude which sources it can use as evidence and which it can't.

The key concept: if you're studying data that came from a specific organization, that organization's data is your **subject**, not your **evidence**. You need independent sources to verify it.

**Before (template):**
```
**Source exclusion -- NEVER use these as independent verification:**
- [Source you are studying, e.g., "OrganizationX.org"]
- [Websites that repost/mirror that source]
```

**After (measles example):**
```
**Source exclusion -- NEVER use these as independent verification:**
- Anti-vaccine blogs and social media posts (unreliable data, not primary sources)
- Wikipedia outbreak lists (secondary compilations, not primary reporting)

**What counts as an independent source for this project:**

| Source Type | Independent? | Good For |
|------------|-------------|----------|
| CDC MMWR reports | Yes | Official outbreak declarations, case counts |
| State health department press releases | Yes | Local outbreak details, timelines |
| Peer-reviewed journal articles | Yes | Analysis, confirmed case counts |
| Local news articles with original reporting | Yes | Community impact, timeline details |
| WHO disease outbreak news | Yes | International context, travel-linked cases |
| Anti-vaccine websites | No | Unreliable, often misrepresent data |
```

Not every project has a source exclusion rule. If you're collecting original data from scratch (not verifying someone else's list), you can simplify this section to focus on what counts as a reliable source for your topic.

### Section 3: What NOT to Do

Find `## What NOT to Do`. Add your project-specific guardrails. Think about what mistakes would be costly or hard to undo.

**Measles example:**
```
- Do not use anti-vaccine sources as verification of outbreak data
- Do not modify files in source-data/ -- those are original data extractions
- Do not delete dataset entries -- if a record is wrong, update its verification_level
- Do not include personally identifiable patient information beyond what's in public reports
- Do not combine suspected and confirmed cases in the same count fields
```

### The rest of CLAUDE.md

The other sections (Repository Structure, How to Add a Record, How to Verify, Common Tasks, Tool Usage Rules) are already filled in with sensible defaults. You can leave them as-is for now. As you work on your project, you'll naturally want to adjust them -- and that's fine. This file is meant to grow with your project.

**Tip:** You can ask Claude to help you customize CLAUDE.md. Try: "Help me fill in the source rules section of CLAUDE.md for a project studying measles outbreaks."

---

## Step 4: Customize Your Schema

`dataset/SCHEMA.md` defines the fields in your dataset -- think of it as designing the columns of a spreadsheet, but before you enter any data.

Open `dataset/SCHEMA.md`. The template has placeholder fields organized in categories. You're going to replace the placeholders with fields that matter for your research.

### How to think about fields

Ask yourself: **"What questions do I want to answer about my data?"** Each question usually becomes a field.

For measles research, your questions might be:
- When did the outbreak start? -> `date` (already in the template)
- Where was it? -> `state`, `county`, `city` (already in the template)
- How many people were affected? -> `confirmed_cases`, `suspected_cases`
- Was it linked to under-vaccination? -> `vaccination_linked` (yes/no)
- What setting? -> `setting` (school, daycare, community, healthcare, travel)
- What genotype? -> `genotype` (D8, B3, etc.)
- Was it imported or endemic? -> `origin` (imported, import-linked, endemic, unknown)

### Replacing the template fields

Find the `## YAML Frontmatter Fields` section. It has placeholder categories like `[Category 1: e.g., Location]`. Replace those with your real categories and fields.

**Measles example -- the Classification section might look like:**

```yaml
### Outbreak Details

# type: number
# min: 0
# required: true
confirmed_cases: 0                   # Lab-confirmed measles cases in this outbreak

# type: number
# min: 0
suspected_cases: 0                   # Suspected but not confirmed cases

# type: enum
# values: [school, daycare, community, healthcare, travel, workplace, unknown]
setting: "community"                 # Primary setting where transmission occurred

# type: enum
# values: [imported, import-linked, endemic, unknown]
origin: "unknown"                    # Whether the outbreak originated from international travel

# type: boolean
vaccination_linked: false            # Whether under-vaccination was identified as a factor

# type: string
genotype: ""                         # Measles virus genotype if identified (e.g., D8, B3)
```

### Update the file naming convention

The template uses `[PREFIX]-[IDENTIFIER].md`. Choose a convention for your project.

**Measles example:**
```
**Format:** `OB-YYYY-ST-NNN.md`

- OB = Outbreak
- YYYY = Year the outbreak started
- ST = Two-letter state code
- NNN = Sequence number (001, 002...) for multiple outbreaks in the same state/year

**Examples:**
- `OB-2024-OH-001.md` -- First tracked 2024 outbreak in Ohio
- `OB-2024-OH-002.md` -- Second tracked 2024 outbreak in Ohio
- `OB-2019-NY-001.md` -- 2019 New York outbreak
```

### Update the example record

At the bottom of SCHEMA.md, there's a `## Complete Example Record` section. Replace it with a realistic example for your project. This example is what Claude references every time it creates a new record, so it should be complete and accurate.

### Don't worry about getting it perfect

You can always add, rename, or remove fields later. The `/clean` skill will help you find inconsistencies when you change your schema. Start with the fields you're sure about, and add more as you learn what data is available.

---

## Step 5: Create Your First Record

Now you're ready to add real data. Open Claude Code Desktop with your project folder and type:

```
/collect
```

Claude will ask you what you found, where you found it, and when it happened. Answer in plain English -- Claude handles the file creation, the YAML formatting, and the naming convention.

For example:
```
You: /collect measles outbreak in Columbus Ohio 2024
Claude: I found your schema. Let me ask a few questions...
        What source did you find this in?
You: CDC MMWR report from March 2024
Claude: How many confirmed cases?
You: 85 confirmed, about 20 suspected
...
```

Claude creates the file, fills in what it knows, marks unknown fields as empty, and sets the verification level. It will remind you about next steps like running `/export` or `/verify`.

---

## Step 6: The "Your Project Is Ready" Checklist

Before you dive into full-time research, make sure these things are done:

- [ ] `template/` copied and renamed to your project name
- [ ] Project folder opens successfully in Claude Code Desktop
- [ ] `CLAUDE.md` has your Project Overview filled in (what are you studying?)
- [ ] `CLAUDE.md` has your Source Rules filled in (what sources are independent?)
- [ ] `CLAUDE.md` has your "What NOT to Do" customized
- [ ] `dataset/SCHEMA.md` has your fields defined
- [ ] `dataset/SCHEMA.md` has your file naming convention
- [ ] `dataset/SCHEMA.md` has a realistic example record
- [ ] You've created at least one record using `/collect`
- [ ] You've run `/export` and confirmed it produces a CSV

You don't need every field in SCHEMA.md to be finalized. You don't need source rules to cover every edge case. Start collecting data, and refine the setup as you learn what your project actually needs.

---

## What's Next

| After you... | Read this |
|-------------|-----------|
| Created your first few records | `docs/03-how-records-work.md` -- understand the file format deeply |
| Have 10+ records | `docs/05-verification.md` -- learn about source independence |
| Want to share your data | `docs/07-exporting.md` -- CSV, Excel, and HTML exports |
| Keep doing the same steps | `docs/12-creating-skills.md` -- turn patterns into slash commands |

---

*Your project is a living thing. The schema will evolve, the CLAUDE.md will get more detailed, and the dataset will grow. That's exactly how it's supposed to work.*
