---
name: clean
description: Run a data quality check on the dataset and fix issues
user-invocable: true
---

# Clean: Data Quality Check

Scan all dataset records for missing fields, invalid values, stale data, inconsistencies, and potential duplicates. Fix mechanical issues automatically and flag judgment calls for the user.

## When to Use

Run `/clean` periodically -- especially after adding several records, before exporting, or before sharing the dataset. Think of it as a spell-check for your data.

## Workflow

### Step 1: Read the Schema

Read `dataset/SCHEMA.md` to understand:
- Which fields are required (look for `# required: true`)
- Which fields are enums with allowed values (look for `# type: enum` and `# values: [...]`)
- Which fields have staleness thresholds (look for `# stale_after_days: N`)
- Date formats expected
- Any other validation rules

If SCHEMA.md doesn't have structured annotations, use the field descriptions to apply reasonable checks (e.g., if a field is described as "state abbreviation," check that values are 2-letter codes).

### Step 2: Scan All Records

Read every `.md` file in `dataset/` (excluding SCHEMA.md and non-record files). For each record, check:

**Errors (must fix):**
- Missing required fields (field absent or empty)
- Enum field values not in the allowed list
- Malformed YAML (file won't parse)
- Malformed dates (not ISO 8601)

**Warnings (should fix):**
- Date fields older than `stale_after_days` threshold
- Empty `sources` list on a record that isn't UNVERIFIED
- `verification_level` is VERIFIED but `independent_source_count` < 2
- Inconsistent casing or formatting across records for the same field

**Info (nice to fix):**
- Fields that are empty but not required
- Records with no markdown body (summary section)
- research_notes mentioning "TODO", "needs follow-up", or "discrepancy"

### Step 3: Check for Duplicates

Compare records pairwise on key fields (typically: date, location, and primary identifying details). Flag pairs where:
- Dates match within +/- 30 days AND locations match
- Key identifying text is very similar
- research_notes already mention possible duplicates

Don't flag records that share a date but have clearly different details.

### Step 4: Present Results

Group findings by severity:

```
Data Quality Report
===================

ERRORS (3 issues -- must fix):
  - REC-2024-001.md: Missing required field 'date'
  - REC-2024-003.md: state value 'California' is not a valid 2-letter code (should be 'CA')
  - REC-2024-007.md: YAML parse error on line 15

WARNINGS (5 issues -- should fix):
  - REC-2023-002.md: cost_date_checked is 8 months old (stale)
  - REC-2024-005.md: verification_level is VERIFIED but only 1 source listed
  ...

INFO (2 notes):
  - REC-2024-004.md: research_notes says "needs follow-up on victim name"
  ...

POSSIBLE DUPLICATES (1 pair):
  - REC-2024-001.md and REC-2024-006.md: same date, same city, similar description
```

### Step 5: Offer Fixes

For each error and warning, determine if it's mechanical (Claude can fix it) or a judgment call (user must decide):

**Mechanical fixes (offer to do automatically):**
- Fix state abbreviations ("California" -> "CA")
- Fix date formatting ("7/4/2024" -> "2024-07-04")
- Add missing empty fields to records that predate a schema change

**Judgment calls (present to user):**
- "Should I upgrade this record from UNVERIFIED to CONFIRMED? It has 1 independent source."
- "These two records might be duplicates. Should I merge them or keep both?"
- "The cost data is 8 months old. Want me to search for updated pricing?"

Ask the user: "I can fix N mechanical issues automatically. Should I go ahead? The judgment calls I'll walk you through one at a time."

### Step 6: Apply Fixes

For each approved fix:
- Edit the record file
- Note what was changed in `research_notes` (e.g., "2026-04-07: Fixed state abbreviation from 'California' to 'CA' per /clean")

After all fixes:
- Report what was changed
- Suggest running `/export` to regenerate the spreadsheet

## Error Handling

- **No records:** "The dataset is empty. Use `/collect` to add your first record."
- **No SCHEMA.md:** "No schema found. I'll check for basic issues (malformed YAML, empty files) but can't validate field values without a schema. Consider creating dataset/SCHEMA.md."
- **Very large dataset (100+ records):** Report progress as you scan. Don't try to fix everything at once -- prioritize errors, then warnings.

## References

- Read `dataset/SCHEMA.md` for validation rules
- Read `CLAUDE.md` for project-specific conventions
