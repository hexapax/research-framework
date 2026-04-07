# How the ESD Research Project Uses These Patterns

This document shows how a real, completed research project used the same framework you're learning. The [ESD Research Project](https://github.com/hexapax/esd-research) studied Electric Shock Drowning -- deaths caused by electrical current leaking from dock wiring into fresh water. It documented 193 incidents over 44 years.

The patterns below map directly to what you're doing in your own project. The subject matter is different, but the workflow is identical.

---

## The Research Problem

The most widely cited list of ESD incidents (the ESDPA list) had 175 entries. But nobody had ever independently verified it. The research question: **How accurate is this list, and what's missing from it?**

This is a common research pattern: you have a dataset that everyone cites, but nobody has checked the primary sources.

## How CLAUDE.md Defined the Rules

The ESD project's CLAUDE.md had one critical rule that shaped every research decision:

> **NEVER use these as independent verification sources:**
> - ESDPA.org (the subject of study)
> - MikeHolt.com (reposts the ESDPA list)
> - OnTimeService.com
> - Any website that reproduces the ESDPA list verbatim

**Why this matters:** If Source B got its data from Source A, and you use Source B to "verify" Source A, you've proven nothing. You've just found a copy. The CLAUDE.md encoded this rule so every research session followed it automatically.

**In your project:** Your CLAUDE.md should identify what you're studying vs. what counts as independent evidence. If you're studying CDC case reports, then a news article that quotes the CDC report is not an independent verification -- it's a derivative.

## How Records Were Structured

Each incident was a markdown file with YAML frontmatter:

```yaml
---
incident_id: ESD-2012-07-04-1
date: "2012-07-04"
state: MO
body_of_water: Lake of the Ozarks
incident_type: fatal
fatality_count: 2
verification_level: VERIFIED
independent_source_count: 7
sources:
  - url: "https://www.lakeexpo.com/..."
    type: news
    outlet: "Lake Expo"
---

# ESD-2012-07-04-1: Anderson Children -- Lake of the Ozarks, MO

## Summary
Two children, ages 8 and 13, were electrocuted while swimming near a private dock...
```

**193 files like this.** Each one is a complete, self-contained research record with structured data for analysis and narrative for context.

## How Verification Worked

The project verified each ESDPA entry by searching for independent sources:

| Verification Result | Count | Percentage |
|-------------------|-------|-----------|
| Independently verified | 106 | 61% |
| No independent sources found | 69 | 39% |

**Key finding:** 73% of ESDPA entries had at least one data quality issue -- wrong dates, wrong locations, misclassifications.

The verification process was systematic:
1. Search for the victim's name + location + year
2. Search for obituaries
3. Search for court records
4. Search for local TV coverage on YouTube
5. Cross-reference against the structured dataset

This is exactly what the `/verify` skill does in your project.

## Lines of Attack (Search Strategies)

Instead of searching randomly, the project defined 14 systematic search strategies called "Lines of Attack":

| LOA | Strategy | Result |
|-----|----------|--------|
| LOA1 | News archive search | 13 new verified incidents |
| LOA2 | Misclassified drownings | 25 suspected cases |
| LOA3 | Legal record mining | Settlement and verdict data |
| LOA4 | Government records (OSHA, CPSC, CDC) | 5 new incidents |
| LOA5 | Academic literature | Critical methodology findings |
| LOA6 | Community/forum sources | 52 leads |
| LOA7 | Structured databases (BARD, NCHS) | 42 statistical candidates |
| LOA8 | Obituary mining | 4 victim IDs confirmed |
| LOA11 | YouTube video archives | 17 probable new incidents |

**In your project:** Your `research-plan.md` is where you define your own Lines of Attack. Each search strategy gets its own subdirectory in `findings/`. This prevents "searching randomly" and ensures comprehensive coverage.

## How the Export System Worked

The project had three export sizes:
- **Small** (18 columns): ID, date, name, location, counts, notes, source URL
- **Medium** (30 columns): adds verification, ESDPA status, electrical details, legal outcomes
- **Large** (42 columns): everything including all source URLs and research notes

Each XLSX had two sheets: **Incidents** (one row per event) and **Victims** (one row per person).

The export script read all 193 YAML files and produced CSV and XLSX automatically.

## What Worked Best

1. **CLAUDE.md as project memory.** Every new Claude session started by reading the rules, the schema, and the conventions. No re-explaining.

2. **Structured YAML for analysis, markdown for notes.** The YAML fields could be exported to Excel for quantitative analysis. The markdown body captured the nuance, uncertainty, and context that spreadsheet cells can't hold.

3. **Verification levels as workflow state.** An UNVERIFIED record isn't a failure -- it's a to-do item. The `/next` skill uses verification level to suggest what to work on.

4. **Source independence as a hard rule.** Encoding "these sources don't count" in CLAUDE.md prevented the most common research error: circular sourcing.

5. **Git as an audit trail.** Every change to every record is in the git history. If a reviewer asks "when did you add this source?" the answer is in the commit log.

## What You Can Learn From This

The ESD project started with a list and ended with a verified dataset that found the original list was 39% unverifiable and 73% inaccurate. The same framework -- file-per-record, independent verification, systematic search strategies, structured exports -- applies to any domain where you're building a dataset from scattered primary sources.

Your project might be smaller or larger. The principles scale.
