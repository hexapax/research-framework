# Keeping Your Data Clean

Your dataset is only as useful as its quality. A spreadsheet full of missing fields, inconsistent formatting, and stale numbers is hard to analyze and easy to misinterpret.

This guide covers the most common data quality problems, how the `/clean` skill helps you find and fix them, and how your SCHEMA.md file acts as a set of rules your data should follow.


## Common Data Quality Problems

These are the issues that creep into every research dataset. They're not signs of bad work -- they're the natural result of collecting data over time from different sources.

### Missing fields

A record has a blank where there should be a value. Maybe you added it in a hurry and planned to fill in the details later. Maybe the source didn't mention it.

**Example:** A measles outbreak record has the county and state, but the city field is blank. When you export to a spreadsheet, that row has an empty cell. If someone filters by city, this record disappears from the results.

**What to do:** Decide whether the field is truly unknown or just unfilled. If the information exists in your sources, fill it in. If it's genuinely unknown, that's fine -- but make sure your schema distinguishes "not yet entered" from "unknown."

### Stale data

A field that was accurate when you entered it but may not be accurate anymore.

**Example:** You recorded a hotel's nightly rate as $89 eight months ago. Prices change. If your analysis depends on current pricing, that number might be wrong now.

**What to do:** Your SCHEMA.md can flag fields with a staleness threshold (more on that below). The `/clean` skill checks these dates and warns you when values are getting old.

### Inconsistent formatting

The same information written different ways across records.

**Example:** One record says "California," another says "CA," a third says "ca." They all mean the same thing, but a computer treats them as three different values. Your filters break, your counts are wrong, and your spreadsheet has three separate categories instead of one.

**What to do:** Pick a format and stick to it. Define the allowed values in your SCHEMA.md. The `/clean` skill catches these inconsistencies and can fix the mechanical ones automatically.

### Duplicate records

Two records that describe the same thing.

**Example:** You collected a measles outbreak from a CDC report and later found the same outbreak mentioned in a state health department report. You created two records without realizing they're the same event.

**What to do:** The `/clean` skill compares records on key fields (dates, locations, descriptions) and flags pairs that look suspiciously similar. But it can't always tell for sure -- that's a judgment call you need to make.

### Mismatched verification

The verification level doesn't match the evidence.

**Example:** A record says VERIFIED, but there's only one source listed. Or a record has three independent sources but is still marked UNVERIFIED because nobody updated the level after adding the sources.

**What to do:** The `/clean` skill checks that verification levels are consistent with source counts and flags mismatches.


## Using /clean

The `/clean` skill is like a spell-checker for your data. Run it periodically to catch problems before they pile up.

### What it does

When you type `/clean`, Claude reads your SCHEMA.md to understand your data rules, then scans every record in the dataset and checks for:

1. **Errors** (must fix): Missing required fields, invalid values (like "Califronia" where a state code should be), malformed dates, broken YAML formatting.

2. **Warnings** (should fix): Stale dates past their freshness threshold, verification levels that don't match the source count, inconsistent formatting across records.

3. **Info** (nice to fix): Empty optional fields, records missing a summary section, research notes that say "TODO" or "needs follow-up."

4. **Possible duplicates**: Records with similar dates and locations that might be the same event.

### What it shows you

Claude presents a report grouped by severity:

```
Data Quality Report
===================

ERRORS (2 issues):
  - REC-2024-003.md: state value 'California' should be 'CA'
  - REC-2024-007.md: Missing required field 'date'

WARNINGS (3 issues):
  - REC-2023-002.md: cost field is 8 months old (stale)
  - REC-2024-005.md: VERIFIED but only 1 source listed
  - REC-2024-001.md: date format '7/4/2024' should be '2024-07-04'

POSSIBLE DUPLICATES (1 pair):
  - REC-2024-001.md and REC-2024-006.md: same date, same city
```

### What it fixes vs. what you decide

Some issues are mechanical -- Claude can fix them without your input. Changing "California" to "CA" or reformatting "7/4/2024" to "2024-07-04" has only one right answer.

Other issues need your judgment. Should two similar-looking records be merged or kept separate? Should a record be upgraded from UNVERIFIED to CONFIRMED? Is the stale price still close enough to be useful?

Claude will offer to fix the mechanical issues automatically and walk you through the judgment calls one at a time.


## Validation Rules in SCHEMA.md

Your SCHEMA.md file is the rulebook for your data. It describes every field: what it means, what values are allowed, and whether it's required.

The framework uses a hybrid approach. Each field has a plain English description that humans can read, plus optional structured annotations that the `/clean` skill can parse automatically.

Here's what that looks like in practice:

```yaml
# type: enum
# values: [beach, mountain, city, nature, historical]
# required: true
destination_type: "beach | mountain | city | nature | historical"

# type: number
# min: 0
# max: 10000
# stale_after_days: 180
estimated_cost_per_night: 0

# type: string
# required: true
city: ""

# type: date
# required: true
date_checked: ""
```

The lines starting with `#` are the structured annotations. The line without `#` is the English description (or a default value). Both are useful:

- **The English description** is for you. It tells you what the field means and what to put there.
- **The structured annotations** are for the `/clean` skill. They let Claude check your data automatically instead of guessing.

### What the annotations mean

| Annotation | What it does | Example |
|-----------|-------------|---------|
| `# type: enum` | Only these specific values are allowed | `# values: [low, medium, high]` |
| `# type: number` | Must be a number, optionally within a range | `# min: 0` and `# max: 100` |
| `# type: string` | Free text | Most fields are this by default |
| `# type: date` | Must be a date in YYYY-MM-DD format | -- |
| `# required: true` | Field cannot be blank | -- |
| `# stale_after_days: N` | Warn if the field hasn't been updated in N days | `# stale_after_days: 180` (6 months) |

### You don't need annotations on day one

The annotations are optional. If your SCHEMA.md only has English descriptions, the `/clean` skill still works -- Claude uses judgment based on the descriptions. You'll get less precise checking, but it's better than nothing.

As you use `/clean` and notice the same issues coming up repeatedly, that's a natural time to add structured annotations. "I keep entering state names instead of abbreviations" means it's time to add `# type: enum` with a list of state codes.


## How to Add Your Own Validation Rules

Adding a rule is as simple as adding a comment line above a field in SCHEMA.md.

**Before (no rule):**
```yaml
case_count: 0
```

**After (with validation):**
```yaml
# type: number
# required: true
# min: 0
case_count: 0
```

Now `/clean` will flag any record where `case_count` is missing, not a number, or negative.

Want to restrict a field to specific values? Use an enum:

```yaml
# type: enum
# values: [confirmed, probable, suspected, unknown]
# required: true
case_classification: "confirmed | probable | suspected | unknown"
```

Now `/clean` will catch typos like "confimed" or non-standard entries like "likely."

**The REDCap inspiration:** Professional research databases like REDCap (used by thousands of clinical research teams worldwide) have formal data dictionaries that enforce validation rules on every field. Your SCHEMA.md is your version of that. It's simpler than REDCap's system, but the principle is the same: define the rules once, check them every time.


## When to Run /clean

There's no wrong time, but these are the most useful moments:

**After adding several records.** If you've collected 5 or 10 new records in a session, run `/clean` before you move on. It's easier to fix issues while the records are fresh in your mind.

**Before exporting.** If you're about to generate a CSV or XLSX to share with someone, clean first. You don't want to hand over a spreadsheet with "California" and "CA" as two separate categories.

**Before sharing your dataset.** Whether it's a collaborator, a professor, or a publication, a clean dataset makes a better impression and produces more reliable analysis.

**When you've been away for a while.** If you haven't touched the project in a few weeks, `/clean` is a good way to re-orient. The stale data warnings tell you what's gotten old, and the TODO notes in research_notes remind you where you left off.

You don't need to run it after every single record. Think of it like tidying your desk -- you don't need to organize after every piece of paper, but you shouldn't let it pile up either.
