# Measles Research Quickstart

This guide helps you set up a research project for studying measles outbreaks using this framework. It shows you what to put in CLAUDE.md, how to define your schema, and what your first few records might look like.

---

## Customize Your CLAUDE.md

Here's what the key sections might look like for a measles research project:

### Project Overview

```markdown
## Project Overview

This project tracks measles outbreaks in the United States, focusing on the 
post-2019 resurgence. The goal is to build a verified dataset of outbreaks 
with case counts, vaccination coverage data, geographic spread, and public 
health response timelines.

**Current state:** [X] documented outbreaks in the dataset.
```

### Source Rules

```markdown
## Source Rules

### Independent Sources (use these for verification)
- CDC MMWR reports and situation updates
- State and local health department press releases
- Peer-reviewed journal articles (NEJM, Lancet, JAMA, etc.)
- News articles from local and national outlets
- WHO Disease Outbreak News

### Subject-of-Study Sources (do NOT use as independent verification)
- [If you're studying a specific dataset, e.g., a particular state's 
  surveillance system, list it here]

### Source Quality Hierarchy
1. **Primary:** CDC MMWR, state epi reports, published case series
2. **Secondary:** News articles, WHO situation reports
3. **Tertiary:** Blog posts, social media (leads only, must verify)
```

### Tool Usage Rules

```markdown
## Tool Usage Rules

- Use Perplexity for broad outbreak searches ("measles outbreaks US 2024")
- Use PubMed MCP (medical-mcp) for academic literature
- Use built-in web search for quick fact-checks (case counts, dates)
- Check CDC.gov directly for MMWR reports and surveillance data
- Do NOT use web search when the answer is in our own dataset files
```

## Define Your Schema

Here's a starter `dataset/SCHEMA.md` for measles outbreaks:

### File Naming

**Format:** `OB-YYYY-MM-DD-N.md`
- `OB` = Outbreak
- `YYYY-MM-DD` = Start date of the outbreak (or first reported case)
- `N` = Sequence number for same-date outbreaks
- Use `00` for unknown month or day

**Examples:**
- `OB-2024-11-15-1.md` -- Outbreak starting November 15, 2024
- `OB-2019-01-00-1.md` -- January 2019, day unknown

### Key Fields

```yaml
---
# IDENTIFICATION
# type: string
# required: true
# unique: true
outbreak_id: OB-YYYY-MM-DD-N

# type: date
# required: true
date_start: "YYYY-MM-DD"

# type: date
date_end: "YYYY-MM-DD"

# type: integer
# required: true
year: YYYY

# type: enum
# values: [exact, month, year, approximate]
# required: true
date_precision: exact

# LOCATION
# type: string
# required: true
state: XX

# type: string
county: ""

# type: string
city: ""

# CASE DATA
# type: integer
# required: true
total_cases: 0

# type: integer
hospitalized: 0

# type: integer
deaths: 0

# type: string
age_range: ""

# type: number
# stale_after_days: 90
vaccination_rate_area: null

# OUTBREAK DETAILS
# type: enum
# values: [imported, endemic, unknown]
origin: unknown

# type: string
genotype: ""

# type: string
index_case_description: ""

# type: enum
# values: [community, school, healthcare, religious, workplace, household, other, unknown]
setting: unknown

# RESPONSE
# type: string
public_health_response: ""

# type: string
containment_measures: ""

# VERIFICATION
# type: enum
# values: [VERIFIED, CONFIRMED, PROBABLE, SUSPECTED, UNVERIFIED]
# required: true
verification_level: UNVERIFIED

# type: integer
independent_source_count: 0

# SOURCES
sources: []

# NOTES
notes: ""
research_notes: ""
---
```

## Example Record

```yaml
---
outbreak_id: OB-2024-11-15-1
date_start: "2024-11-15"
date_end: "2025-01-20"
year: 2024
date_precision: exact

state: OH
county: Franklin
city: Columbus

total_cases: 85
hospitalized: 32
deaths: 0
age_range: "6 months - 12 years"
vaccination_rate_area: 89.2

origin: imported
genotype: D8
index_case_description: "Unvaccinated child, recent travel to Eastern Europe"
setting: community

public_health_response: "Mass vaccination clinics, school exclusion orders"
containment_measures: "Contact tracing identified 1,200+ exposures. Free MMR clinics at 8 locations."

verification_level: VERIFIED
independent_source_count: 5

sources:
  - url: "https://www.cdc.gov/mmwr/..."
    type: government
    outlet: "CDC MMWR"
    date: "2024-12-06"
  - url: "https://www.dispatch.com/..."
    type: news
    outlet: "Columbus Dispatch"
    date: "2024-11-20"
  - url: "https://odh.ohio.gov/..."
    type: government
    outlet: "Ohio Department of Health"
    date: "2024-11-18"

notes: "Largest Ohio measles outbreak since 2014. Concentrated in undervaccinated communities. Triggered statewide vaccination campaign."
research_notes: "CDC MMWR published detailed case series Dec 2024. ODH press releases provide weekly case counts. Vaccination rate from ODH immunization registry (2023-2024 school year data)."
---

# OB-2024-11-15-1: Columbus, OH Measles Outbreak (2024-2025)

## Summary

An outbreak of 85 confirmed measles cases in Columbus, Ohio, beginning in November 2024. The index case was an unvaccinated child who had recently traveled to Eastern Europe. The outbreak spread primarily through community contact in areas with below-average vaccination coverage, with 32 hospitalizations and no deaths.

## Timeline

- **Nov 15, 2024:** First confirmed case reported to Franklin County Public Health
- **Nov 20, 2024:** ODH declares outbreak, activates response team
- **Dec 1, 2024:** 30 cases confirmed, mass vaccination clinics open
- **Dec 6, 2024:** CDC MMWR publishes initial report
- **Jan 20, 2025:** Last case reported, outbreak declared over

## Key Details

- **Genotype D8** identified, consistent with Eastern European circulation
- **89.2% vaccination rate** in the affected area (below the 95% threshold for herd immunity)
- **37% of cases** in children under 5 years old
- **Contact tracing** identified over 1,200 potential exposures
```

## Recommended MCP Tools for Measles Research

| Tool | What it does | Install |
|------|-------------|---------|
| **Perplexity** | AI-powered web search with citations | See docs/10-mcp-tools.md |
| **medical-mcp** | PubMed, WHO, FDA search | `npm install` from GitHub |
| **paperplain-mcp** | 200M academic papers, no API key needed | `npm install` from GitHub |

## First Steps

1. Copy `template/` to a new folder called `measles-research/`
2. Replace the CLAUDE.md content with the sections above
3. Replace `dataset/SCHEMA.md` with the schema above
4. Run `/collect` and add your first outbreak
5. Run `/verify` to search for independent sources
6. Run `/export` to see your data in a spreadsheet

## Research Questions This Framework Can Help Answer

- How many measles outbreaks have occurred in the US since [year]?
- What is the average outbreak size by state?
- What proportion of outbreaks are imported vs. endemic?
- How do vaccination rates correlate with outbreak size?
- How quickly do public health agencies respond?
- Which genotypes are circulating and from where?

Each of these questions maps to fields in your schema. As your dataset grows, the answers emerge from the structured data.
