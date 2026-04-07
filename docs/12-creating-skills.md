# Creating Your Own Workflows

Here's the rule: **if you've done the same thing 3 times, it's a skill.**

A skill is a set of instructions that Claude follows when you type a command. No code. No programming. Just plain English describing the steps -- the same way you'd explain the task to a research assistant.

You've been using skills since your first session. `/collect`, `/verify`, `/search`, `/export`, `/clean` -- these are all skills that someone wrote for you. Now you're going to write your own.

---

## What a Skill Actually Is

A skill is a text file. That's it. A text file with a name and a set of instructions.

When you type `/my-skill` in Claude Code, Claude reads that text file and follows the instructions. The instructions tell Claude what to ask you, what files to read, what checks to run, and what to produce.

Here's the mental model: **a skill is a checklist you'd give a research assistant.** "When I ask you to add a new outbreak record, here's what I need you to do, step by step."

The difference between asking Claude to do something in conversation vs. using a skill is permanence. Conversations disappear. Skills stay. The tenth time you run a skill, it works exactly like the first time.

---

## The 4-Step Process

### Step 1: Notice the pattern

You'll know it's time to make a skill when you catch yourself saying:

- "Do the same thing we did yesterday when I added that record"
- "Check the data quality like we did last week"
- "Generate that summary page again"
- "Search for outbreaks the same way you did before"

Three times is the threshold. Once is a task. Twice is a coincidence. Three times is a workflow.

### Step 2: Record it once

Do the task with Claude one more time, but at the end, say:

"Turn what we just did into a skill."

Claude will look at the conversation, extract the steps, and draft a SKILL.md file for you. It knows the format. It knows where skills live. It will create the file and explain what it wrote.

You can also describe the skill from scratch: "I want a skill called /weekly-summary that looks at the git history for the past week and tells me what records were added, modified, and verified."

### Step 3: Refine it

The first draft is rarely perfect. Test the skill by running it:

```
/weekly-summary
```

Watch what happens. Then adjust:

- "It didn't check for deleted records -- add that."
- "I want it to show the verification level changes, not just which files changed."
- "It should skip the exports/ directory -- those are generated files, not research changes."

Each correction makes the skill better. Two or three rounds of testing usually produces something solid.

### Step 4: Use it

Now you have a command that does in one step what used to take five. Use it. Every time you catch yourself about to do the manual version, use the skill instead.

---

## Anatomy of a SKILL.md File

Here's a complete example of a skill, with annotations explaining each part.

```yaml
---
name: weekly-summary
description: Summarize research activity from the past week
user-invocable: true
argument-hint: "[number of weeks back, default 1]"
---
```

**The frontmatter** (between the `---` lines) tells Claude Code about the skill:
- `name` -- what you type after the slash: `/weekly-summary`
- `description` -- a one-line explanation that shows up in the skill list
- `user-invocable: true` -- means you can run it directly (some skills are only called by other skills)
- `argument-hint` -- optional hint shown to the user about what arguments the skill accepts

```markdown
# Weekly Summary

Generate a summary of all research activity from the past week.

## When to Use

Run `/weekly-summary` at the start of each week to see what happened 
in the last one. Useful for progress reports, advisor meetings, or 
just remembering where you left off.

## Workflow

### Step 1: Determine the Time Range

If the user provided a number (e.g., `/weekly-summary 2`), look back 
that many weeks. Otherwise, default to 1 week.

Calculate the date range: from 7 days ago to today.

### Step 2: Check Git History

Run:

git log --since="7 days ago" --name-status --pretty=format:"%h %s"

Categorize each changed file:
- New record files in dataset/ -> "Records added"
- Modified record files in dataset/ -> "Records updated"
- Files in dataset/exports/ -> skip (generated files)
- Other files -> "Other changes"

### Step 3: Analyze the Changes

For each new record: note the record ID and key details (date, 
location, verification level).

For each modified record: check what changed. Look at the git diff. 
Summarize the change in plain language:
- "Verification upgraded from UNVERIFIED to CONFIRMED"
- "Added 2 new sources"
- "Corrected date from 2023-03-15 to 2023-03-17"

### Step 4: Compile Statistics

Report:
- Total records added this week
- Total records updated this week
- Records by verification level (current totals, not just changes)
- Date range of the dataset

### Step 5: Present the Summary

Format the summary clearly:

    This Week's Research Activity (March 30 - April 6, 2026)
    =========================================================

    ADDED (3 new records):
      - REC-2024-015: Columbus, OH -- 8 cases, Mar 2024 (CONFIRMED)
      - REC-2024-016: Toledo, OH -- 3 cases, Jun 2024 (UNVERIFIED)
      - REC-2025-001: Cincinnati, OH -- 12 cases, Jan 2025 (VERIFIED)

    UPDATED (2 records):
      - REC-2024-003: Upgraded to VERIFIED (added CDC source)
      - REC-2024-009: Corrected case count from 15 to 18

    DATASET TOTALS:
      48 records total (23 verified, 15 confirmed, 10 unverified)
      Date range: 2018-01-15 to 2025-01-22

## Error Handling

- **Git not initialized:** "Can't check history without git. Here's 
  a count of current records instead: [list dataset files]"
- **No changes this week:** "No research activity in the past week. 
  Run /next for suggestions on what to work on."
- **Very busy week (20+ changes):** Summarize by category rather 
  than listing every file. Offer: "Want the full details?"
```

**The body** is where the real instructions live. Notice:

- **When to Use** -- helps Claude (and you) know when this skill is appropriate
- **Workflow** -- numbered steps that Claude follows in order
- **Error Handling** -- what to do when things go wrong
- The instructions reference project files (`dataset/`, git history) and other skills (`/next`)

That's the entire format. Plain English. Step by step. With error handling.

---

## Where Skills Live

Skills go in your project's `.claude/skills/` directory. Each skill gets its own folder:

```
.claude/
  skills/
    weekly-summary/
      SKILL.md
    check-urls/
      SKILL.md
    validate-costs/
      SKILL.md
```

When you ask Claude to create a skill, it puts the file in the right place automatically. You can also create the folder and file manually if you prefer.

---

## Worked Examples

Here are three skills that show different patterns. Use them as inspiration.

### /validate-costs

A skill for a project tracking outbreak response costs:

```yaml
---
name: validate-costs
description: Find records with outdated cost data and offer to update them
user-invocable: true
---
```

```markdown
# Validate Costs

Scan all records where cost data hasn't been checked in 6+ months. 
List them and offer to search for current figures.

## Workflow

### Step 1: Read the Schema

Read dataset/SCHEMA.md to find cost-related fields and any 
stale_after_days annotations.

### Step 2: Scan Records

For each record in dataset/, check:
- Does it have a cost field?
- When was the cost last verified? (Check research_notes for dates, 
  or fall back to the file's last git commit date)
- Is it older than 180 days?

### Step 3: Present Stale Records

List records with outdated costs, sorted by oldest first:

    Records with stale cost data (older than 6 months):

    1. REC-2023-005: Response cost $2.3M -- last checked 2025-08-12
    2. REC-2024-001: Response cost $890K -- last checked 2025-09-03

    Want me to search for updated figures? (I'll start with #1)

### Step 4: Update If Requested

If the user says yes, search for updated costs using available 
search tools. Update the record and note the change in 
research_notes with today's date.
```

### /weekly-summary

The full example shown in the Anatomy section above. Summarizes git activity into a human-readable progress report.

### /review

This skill already exists in your project -- it generates an interactive HTML page from your dataset. Here's how it works under the hood:

1. It reads every record file in `dataset/`
2. It reads `SCHEMA.md` to understand what fields exist and which are enums
3. It builds a self-contained HTML file with embedded JavaScript
4. The HTML includes a sortable table, filter dropdowns, a search box, and summary statistics
5. It writes the file to `dataset/review.html`

No external dependencies. No internet needed to view it. You can email the HTML file to someone and they can open it directly.

The skill instructions tell Claude how to build this from scratch each time, ensuring the page always reflects the current state of your data.

---

## Tips for Writing Good Skills

### Be specific

"Check the data" is vague. Claude will do something, but it might not be what you want.

"Read each record in dataset/. For each one, check that the date field is a valid ISO 8601 date (YYYY-MM-DD format). List any records where the date is missing, malformed, or in the future." That's specific. Claude will do exactly that.

### Include what to do when things go wrong

Every skill should have an error handling section. Think about:

- What if the dataset is empty?
- What if a file has malformed YAML?
- What if a required field is missing from the schema?
- What if the user says "no" to a suggestion?

A skill without error handling works great until something unexpected happens. Then it gets confused.

### Reference your project rules

Skills don't live in isolation. They should know about your project:

"Read CLAUDE.md for the source exclusion rules before evaluating sources."

"Follow the naming convention defined in SCHEMA.md for new files."

"Check DATA-GOVERNANCE.md before including any names in the output."

These references keep the skill consistent with the rest of your project.

### Test with edge cases

After creating a skill, test it against unusual situations:

- Run it on an empty dataset
- Run it on a record with missing fields
- Run it on a record with malformed YAML
- Run it with an argument it doesn't expect

Each failure teaches you something to add to the error handling section.

---

## Advanced Features (Brief Overview)

Once you're comfortable creating basic skills, there are more powerful features available. You don't need these now, but knowing they exist helps when your needs grow.

### Skills that take arguments

Your skill can accept input from the user. The `$ARGUMENTS` variable captures whatever the user types after the skill name:

```
/my-skill Ohio 2024
```

In the skill, `$ARGUMENTS` would be `Ohio 2024`. Your instructions can tell Claude how to parse this: "The first argument is a state name, the second is a year."

### Skills that inject live data

You can embed shell commands in your skill that run when the skill is invoked. Wrap them in `` !`command` `` syntax:

```markdown
Current record count: !`ls dataset/*.md | grep -v SCHEMA | wc -l`
```

This runs the command and inserts the result before Claude processes the skill. Useful for skills that need to know the current state of the project.

### Skills that run in subagents

Adding `context: fork` to your skill's frontmatter tells Claude to run the skill in a separate context. This is useful for long-running tasks that shouldn't interfere with your main conversation.

### Publishing skills for others

If you create a skill that would be useful to other researchers, it can be packaged and shared. The skill file itself is all that's needed -- it's just a text file someone drops into their `.claude/skills/` directory.

---

## You Can Do This

Look at what you've done. You started with a blank project. You collected records, verified them against independent sources, cleaned up data quality issues, exported spreadsheets, and built interactive review pages. All by typing plain English commands.

Creating a skill is the same thing. You're describing a process in plain English. The only difference is you're saving it to a file so you can use it again.

The skills you create are the ones that matter most -- they're tailored to your research, your data, your workflow. Nobody else can write them for you, because nobody else knows your work like you do.

Start with one. Pick the task you've done three times. Turn it into a skill. Refine it. Use it.

Then make another one.

---

## Next Steps

- Looking for the basics? Go back to [Your First Project](02-your-first-project.md).
- Want to share your dataset with the world? See [Publishing and Sharing Your Research](09-publishing.md).
- Want to add more powerful tools? See [Adding Search and Research Tools](10-mcp-tools.md).
