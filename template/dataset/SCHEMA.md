# Dataset Schema

<!--
This is your DATA DICTIONARY -- it defines every field in your dataset
files. Anyone (human or AI) who reads this file should be able to create
a correctly structured record without asking you any questions.

The schema uses a hybrid format:
1. Human-readable descriptions (always present)
2. Optional machine-readable validation annotations (lines starting with
   # type:, # values:, # required:, etc.)

If the structured annotations are present, the /clean skill can use them
for automated validation. If they're absent, Claude uses judgment based
on the English descriptions. Start informal -- you can add annotations
later as you see their value.

VALIDATION ANNOTATIONS (all optional):
  # type: string | number | enum | date | boolean | list | map
  # values: [option1, option2, option3]    (for enum fields)
  # required: true                          (field must have a value)
  # min: 0                                  (for numbers)
  # max: 100                                (for numbers)
  # stale_after_days: 180                   (flag if older than N days)
  # format: ISO-8601                        (expected format hint)
  # unique: true                            (no two records should share this value)
-->

**Version:** 1.0
**Created:** [Date]
**Purpose:** [One sentence describing what each record in this dataset represents]

---

## File Naming Convention

<!--
Choose a naming convention that matches your data. Examples:

  Date-based:     ESD-YYYY-MM-DD-N.md     (events with known dates)
  Sequential:     DEST-NNN.md             (catalog entries)
  Code-based:     OB-ST-YYYY-NNN.md       (location + date + sequence)
  Name-based:     CASE-[lastname]-YYYY.md  (person-centered records)
-->

**Format:** `[PREFIX]-[IDENTIFIER].md`

- [Explain each component of the identifier]
- [Explain how to handle unknowns, e.g., "Use 00 for unknown month or day"]
- [Explain sequence numbers for same-identifier collisions]

**Examples:**
- `[PREFIX]-2024-03-15-1.md` -- [Description of what this example represents]
- `[PREFIX]-2024-03-15-2.md` -- [Second record on the same date]
- `[PREFIX]-2024-00-00-1.md` -- [Year known, month and day unknown]

---

## File Structure

Each file uses **YAML frontmatter** (between `---` markers) for structured data, followed by a **markdown body** for narrative notes. The YAML is designed to be machine-parseable for CSV/Excel export.

---

## YAML Frontmatter Fields

### Identification

<!--
Every record needs a unique ID and some way to place it in time.
The record_id should match the filename (without .md).
-->

```yaml
# type: string
# required: true
# unique: true
record_id: "[PREFIX]-[IDENTIFIER]"   # Primary ID (matches filename)

# type: date
# required: true
# format: ISO-8601
date: "YYYY-MM-DD"                   # When did this [event/observation] occur?

# type: number
# required: true
year: 2024                           # Separate year field for filtering
```

### [Category 1: e.g., Location]

<!--
Group related fields under descriptive headings. For each field, provide:
- The field name and a sample value
- A comment explaining what it is
- Validation annotations if you want automated checking
-->

```yaml
# type: string
# required: true
state: "XX"                          # [e.g., Two-letter state code]

# type: string
county: ""                           # [e.g., County name, if known]

# type: string
# required: true
city: ""                             # [e.g., City or nearest town]

# type: string
location_detail: ""                  # [e.g., Specific venue, address, or landmark]
```

### [Category 2: e.g., Classification]

```yaml
# type: enum
# values: [type_a, type_b, type_c, other, unknown]
# required: true
record_type: "type_a"                # [What kind of record is this?]

# type: enum
# values: [active, resolved, historical, unknown]
status: "active"                     # [Current status of this record]
```

### [Category 3: e.g., Key Measurements / Counts]

```yaml
# type: number
# min: 0
primary_count: 0                     # [e.g., Number of cases, fatalities, items]

# type: number
# min: 0
# max: 10000
# stale_after_days: 180
estimated_value: 0                   # [e.g., Cost, population, measurement]
```

### Verification and Provenance

<!--
These fields track where the record came from and how well-verified it
is. They are essential for research integrity. Keep these fields in every
schema -- customize the verification_level values to match your project.
-->

```yaml
# type: enum
# values: [VERIFIED, CONFIRMED, PROBABLE, SUSPECTED, UNVERIFIED]
# required: true
verification_level: "UNVERIFIED"     # See Verification Levels below

# type: string
# required: true
discovery_source: ""                 # Where was this record first found?
                                     # e.g., "LOA1", "news search", "colleague tip"

# type: number
# min: 0
independent_source_count: 0          # Number of independent sources confirming this record
```

### Sources

<!--
Every record should document where its information came from. This is
non-negotiable for research credibility. The sources list can contain
as many entries as needed.
-->

```yaml
sources:
  - url: "https://example.com/article"
    type: news                       # news | government | academic | review |
                                     # legal | video | organization | other
    name: "Source Name"              # Publication or organization name
    date: "YYYY-MM-DD"              # Publication date of the source
    date_accessed: "YYYY-MM-DD"     # When you accessed it
```

### Notes

```yaml
# type: string
notes: ""                            # Brief description for humans reading the export

# type: string
research_notes: ""                   # Internal notes: data quality concerns, follow-up
                                     # needed, search attempts that found nothing, etc.
```

---

## Verification Levels

<!--
Define what each level means for your project. Adjust the criteria to
match your domain. The five levels below work well for most projects,
but you can use fewer (the vacation planner uses three: VERIFIED,
CONFIRMED, UNVERIFIED) or add domain-specific levels.
-->

| Level | Definition | Criteria |
|-------|-----------|----------|
| **VERIFIED** | Independently confirmed | Multiple independent sources confirm key facts |
| **CONFIRMED** | At least one independent source | One non-subject source confirms the record |
| **PROBABLE** | Strong circumstantial evidence | Evidence strongly suggests accuracy but not directly confirmed |
| **SUSPECTED** | Circumstantial only | Some evidence, but needs investigation |
| **UNVERIFIED** | Not yet checked | No independent sources found or sought |

---

## Source Types

<!--
Define the types of sources relevant to your research. This helps with
filtering and understanding where your data comes from.
-->

| Type | Description | Independence |
|------|-------------|-------------|
| `news` | Published news articles with original reporting | Independent |
| `government` | Official government reports, datasets, filings | Independent |
| `academic` | Peer-reviewed journal articles, conference papers | Independent |
| `organization` | Reports from the organization under study | NOT independent (subject of study) |
| `review` | Review sites, aggregators | Independent |
| `legal` | Court records, legal filings | Independent |
| `video` | News broadcasts, documentary footage | Independent |
| `other` | Anything not fitting the above | Evaluate case-by-case |

---

## Generating Exports

The YAML frontmatter is designed for CSV/Excel export. Run:

```bash
python3 scripts/export_dataset.py
```

This produces a CSV file in `dataset/exports/` with one row per record. Simple list fields (like `highlights`) are joined with semicolons. Nested objects (like `sources`) are summarized (count + names).

---

## Complete Example Record

<!--
Provide one fully filled-out example so there's zero ambiguity about
what a real record looks like. Replace the sample data below with
something relevant to your project.
-->

```yaml
---
record_id: "[PREFIX]-2024-06-15-1"
date: "2024-06-15"
year: 2024

state: "OH"
county: "Franklin"
city: "Columbus"
location_detail: "Example location"

record_type: "type_a"
status: "resolved"

primary_count: 3
estimated_value: 150

verification_level: CONFIRMED
discovery_source: "LOA1"
independent_source_count: 2

sources:
  - url: "https://example.com/article-about-this"
    type: news
    name: "Columbus Dispatch"
    date: "2024-06-16"
    date_accessed: "2024-09-01"
  - url: "https://government.example.gov/report-123"
    type: government
    name: "State Health Department"
    date: "2024-07-01"
    date_accessed: "2024-09-01"

notes: "Brief human-readable summary of this record."
research_notes: "Found via Google News search. State report confirms details. No discrepancies."
---

# [PREFIX]-2024-06-15-1: [Brief description] -- Columbus, OH

## Summary

[1-3 sentence description of what this record documents.]

## Details

[Additional narrative context, observations, or analysis that doesn't
fit in structured YAML fields.]

## Known Issues

- [Any data quality concerns, unresolved discrepancies, or follow-up needed]
```

---

*This schema is part of the [YOUR PROJECT NAME] research project. Files conforming to this schema live in `dataset/`.*
