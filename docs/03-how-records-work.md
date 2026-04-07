# How Records Work

This is the guide to understanding the files that make up your research dataset. Read this when you're starting your real project and want to understand what's actually happening inside those files.

---

## The Mental Model

Here's the simplest way to think about it:

**Each file is a spreadsheet row. YAML fields are columns. The markdown body is your notes.**

If you had a spreadsheet tracking measles outbreaks, each row would be one outbreak. It would have columns like "date," "state," "confirmed_cases," and "verification_level." And maybe a "notes" column where you jot down extra context that doesn't fit neatly into a column.

That's exactly what each record file is. The structured fields at the top (the YAML) are your columns. The free-text section at the bottom (the markdown) is your notes. And when you run `/export`, the system reads all the files and assembles them into an actual spreadsheet.

The advantage over a spreadsheet: each record is its own file, so you can write as much or as little in the notes section as you want. A spreadsheet cell holding three paragraphs of context is awkward. A markdown file holding three paragraphs is natural.

---

## What Is YAML Frontmatter?

**YAML frontmatter** is the structured data section at the top of each file. It sits between two lines of three dashes (`---`). Here's what it looks like:

```yaml
---
record_id: OB-2024-OH-001
date: "2024-02-15"
year: 2024
state: "OH"
city: "Columbus"
confirmed_cases: 85
verification_level: CONFIRMED
sources:
  - url: "https://www.cdc.gov/mmwr/example"
    type: government
    name: "CDC MMWR"
notes: "Linked to under-vaccination in local school district."
---
```

The first `---` means "structured data starts here." The last `---` means "structured data ends here." Everything between them follows YAML rules. Everything after the second `---` is regular text (markdown) where you can write freely.

**YAML** stands for "YAML Ain't Markup Language" (programmers love recursive jokes). You don't need to remember that. What you need to know is the formatting rules:

- **Field names** are followed by a colon and a space: `state: "OH"`
- **Text values** should be in quotes: `city: "Columbus"`
- **Numbers** don't need quotes: `confirmed_cases: 85`
- **Dates** should be in quotes: `date: "2024-02-15"`
- **True/false values** don't need quotes: `vaccination_linked: true`
- **Lists** use dashes and indentation (more on this below)
- **Indentation matters.** Use spaces, not tabs. Two spaces per indent level.

If you're thinking "this sounds fussy" -- it is, a little. But Claude handles the formatting for you when it creates records. You mostly need to understand it enough to read records and make small edits.

---

## What Each Part of a Record Does

Let's walk through a complete record file, section by section.

### The filename

```
OB-2024-OH-001.md
```

The filename IS the record's identity. It follows the naming convention you defined in SCHEMA.md. In this example: OB (outbreak), 2024 (year), OH (state), 001 (sequence number). When you see this filename in a list, you immediately know what it represents.

### Identification fields

```yaml
record_id: OB-2024-OH-001
date: "2024-02-15"
year: 2024
```

- **record_id** matches the filename (without .md). This is the unique identifier -- no two records should share one.
- **date** is when the event happened, in YYYY-MM-DD format. The international date format avoids month/day confusion.
- **year** is a separate field for convenience. Filtering by year in a spreadsheet is easier when year has its own column.

### Location fields

```yaml
state: "OH"
county: "Franklin"
city: "Columbus"
location_detail: "Eastmoor Academy school district"
```

These place the record geographically. Your project might use different location fields (country instead of state, coordinates, etc.) -- whatever makes sense for your data.

### Classification fields

```yaml
record_type: "community"
confirmed_cases: 85
suspected_cases: 22
origin: "imported"
genotype: "D8"
```

These are the core data about the record -- the things that make it worth collecting. They're specific to your project. A measles project has case counts and genotypes. An ESD drowning project has fatality counts and electrical sources. A housing study has prices and square footage.

### Verification fields

```yaml
verification_level: CONFIRMED
discovery_source: "CDC MMWR search"
independent_source_count: 2
```

- **verification_level** is how confident you are in this record. See the table below.
- **discovery_source** is where you first found this information.
- **independent_source_count** is how many separate, independent sources confirm the key facts.

These fields exist in every project, regardless of topic. They're the backbone of research integrity.

### Sources list

```yaml
sources:
  - url: "https://www.cdc.gov/mmwr/volumes/73/wr/mm7312a1.htm"
    type: government
    name: "CDC MMWR Weekly Report"
    date: "2024-03-22"
    date_accessed: "2024-09-15"
  - url: "https://www.dispatch.com/story/news/health/2024/03/01/measles.html"
    type: news
    name: "Columbus Dispatch"
    date: "2024-03-01"
    date_accessed: "2024-09-15"
```

This is a **list** of sources -- notice how each one starts with a dash and is indented. Every source has:
- **url** -- where you found it (so someone can check your work)
- **type** -- what kind of source (news, government, academic, etc.)
- **name** -- the publication or organization name
- **date** -- when the source was published
- **date_accessed** -- when you looked at it (because web pages can change)

You can have as many sources as you want. More independent sources = higher verification level.

### Notes fields

```yaml
notes: "Largest Ohio outbreak since 2014. Linked to under-vaccination in school district."
research_notes: "State health dept report pending. Follow up in 30 days. Searched MEDLINE 2024-09-15, no journal articles yet."
```

- **notes** is a brief human-readable summary. This shows up in the CSV export. Keep it to one or two sentences.
- **research_notes** is for internal tracking. Things like: what you've already searched for, what you're waiting on, known issues with the data, reminders to follow up. This is for you and Claude, not for the final audience.

### The markdown body

Everything after the second `---` is free-form markdown:

```markdown
# OB-2024-OH-001: Columbus Measles Outbreak -- Columbus, OH

## Summary

An outbreak of 85 confirmed measles cases in the Columbus, Ohio metro area
beginning in February 2024. The outbreak was linked to under-vaccination in
a local school district and involved the D8 genotype, consistent with
importation from abroad.

## Timeline

- 2024-02-15: First confirmed case reported to Franklin County Public Health
- 2024-02-28: School district notification issued
- 2024-03-01: CDC MMWR publishes initial report

## Known Issues

- Suspected case count (22) is from the March CDC report. State report expected
  to have updated numbers.
```

Write as much or as little as you want here. The YAML fields are for structured data you'll filter and analyze. The markdown body is for narrative context that helps you understand the record when you come back to it weeks later.

---

## How to Read a Record

When you open a record file, read it in this order:

1. **The heading** (first line after `---`): tells you what this record is at a glance
2. **verification_level**: how much should you trust this data?
3. **notes**: the one-sentence summary
4. **The key data fields**: the numbers and classifications that matter for your research
5. **sources**: where did this come from? Are the sources credible?
6. **research_notes**: any known issues, pending follow-ups, or search history
7. **The markdown body**: full narrative context

You don't need to read every field every time. Most of the time, the heading, verification level, and notes tell you what you need to know.

---

## How to Edit a Record

You'll edit records when you find new information, correct an error, or upgrade a verification level. Here are the rules:

### What to change freely

- **Field values** when you have better information (update the case count, fix a misspelled city)
- **Sources list** when you find a new source (add it to the list, bump independent_source_count)
- **verification_level** when a record now meets a higher standard
- **research_notes** any time (this is your working journal for the record)
- **The markdown body** any time (add context, timeline, analysis)

### What to be careful with

- **record_id** -- don't change this. It matches the filename. If the ID is wrong, rename the file too.
- **date** -- if you're correcting a date, note the old date in research_notes: "Date corrected from 2024-03-01 to 2024-02-15 based on state health dept report."
- **Field names** -- if you change a field name (say, renaming `cases` to `confirmed_cases`), you need to update SCHEMA.md and every other record file that uses the old name. Claude can help with this, but it's a bigger change than editing a value.

### What NOT to change

- **Don't delete records.** If a record turns out to be wrong, set its verification_level to something low and explain in research_notes why. The record's existence is part of your research trail.
- **Don't change source-data/ files.** Those are your original inputs and should stay as-is.

### After every edit

Run `/export` to regenerate the spreadsheet. The CSV/Excel files in `dataset/exports/` are generated from your record files. If you edit a record but don't re-export, the spreadsheet will be out of date.

---

## How Records Become a Spreadsheet

When you run `/export`, here's what happens:

1. The export script scans every `.md` file in `dataset/` (except SCHEMA.md)
2. For each file, it reads the YAML frontmatter
3. It extracts each field and maps it to a spreadsheet column
4. Simple values (text, numbers, dates) go directly into cells
5. Lists (like sources) get summarized -- the export typically includes the count and source names joined with semicolons
6. Everything is written to a CSV file in `dataset/exports/`

The result is a standard spreadsheet where:
- Each row = one record file
- Each column = one YAML field
- You can open it in Excel, Google Sheets, or any data tool

You never need to keep the spreadsheet updated by hand. Edit the record files, run `/export`, and the spreadsheet reflects the current state of your data.

**If you need a custom export** (different columns, special formatting, or XLSX instead of CSV), ask Claude: "Can you modify the export script to also include an XLSX file?" Claude will update the Python script for you.

---

## Schema Design Basics

Your schema (the fields you track in SCHEMA.md) is the most consequential design decision in your project. Here's how to approach it.

### Start with your research questions

Every field should connect to a question you want to answer. If you're studying measles outbreaks:

| Question | Field |
|----------|-------|
| When did the outbreak happen? | `date` |
| Where was it? | `state`, `county`, `city` |
| How big was it? | `confirmed_cases`, `suspected_cases` |
| What caused it? | `origin`, `vaccination_linked` |
| What strain? | `genotype` |
| How confident are we? | `verification_level`, `sources` |

If you can't connect a field to a question you care about, you probably don't need it yet.

### Start small and grow

It's much easier to add a field later than to remove one. Begin with 8-12 fields that cover the basics: identification, time, place, key measurements, and verification. After you've collected 10-15 records, you'll have a much better sense of what other fields would be useful.

### Use consistent value types

For fields where the answer comes from a set list (like `setting: "school"` or `origin: "imported"`), define the allowed values in SCHEMA.md. This is called an **enumerated field** (or "enum"). It prevents typos and makes filtering reliable. "school" and "School" and "schools" would be three different values in a spreadsheet -- an enum list prevents that.

### Don't design for every possible case on day one

You'll encounter edge cases -- an outbreak that spans two states, a record with two different dates from two different sources, a case that doesn't fit any of your categories. That's normal. Handle the first few edge cases with the `notes` and `research_notes` fields. If you see the same edge case three or more times, it might deserve its own field.

### The fields every project needs

Regardless of what you're studying, every project benefits from these:

- **record_id** -- unique identifier
- **date** and **year** -- when it happened
- **Location fields** -- where it happened (at least one level: country, state, city)
- **verification_level** -- how well-confirmed is this record?
- **sources** -- where did the information come from?
- **notes** -- brief human-readable summary
- **research_notes** -- internal tracking, search history, follow-ups

These are already in the template. Your project-specific fields go alongside them.

---

## Quick Reference: YAML Formatting

| Data type | How to write it | Example |
|-----------|----------------|---------|
| Text | In quotes | `city: "Columbus"` |
| Number | No quotes | `confirmed_cases: 85` |
| Date | In quotes, YYYY-MM-DD | `date: "2024-02-15"` |
| True/false | No quotes | `vaccination_linked: true` |
| Empty value | Empty quotes or just blank | `genotype: ""` |
| List of values | Dashes with indentation | See sources example above |

**The number one formatting mistake:** getting the indentation wrong in lists. Each level of nesting uses two spaces. If something looks wrong after you edit a record, ask Claude: "Is the YAML in this file valid?" Claude will spot and fix formatting errors.

---

*Records are just files. Files are just text. But text with consistent structure becomes a database -- and a database is the foundation of publishable research.*
