# Research Plan

<!--
This document captures WHAT you're researching, WHY it matters, and HOW
you plan to do it. It serves two purposes:

1. It's your roadmap -- what to work on next and what's been done.
2. It teaches Claude your research strategy so it can help effectively.

Update this as your project evolves. Mark lines of attack as complete,
add new ones as you discover them, and revise your timeline as reality
diverges from the plan (it always does).
-->

**Project:** [YOUR PROJECT TITLE]
**Researcher:** [Your name]
**Started:** [Date]
**Last updated:** [Date]

---

## Research Question

<!--
State the core question you're trying to answer. Be specific enough that
you could tell someone whether you answered it when you're done.

Good: "How many measles outbreaks occurred in the US between 2010 and
      2025, and what percentage were linked to vaccine exemption clusters?"
Vague: "Study measles outbreaks."
-->

[Your research question here. 1-3 sentences.]

---

## Background

<!--
Brief context for someone new to the topic. Why does this question
matter? What has been done before? What gap does your research fill?
-->

[2-5 sentences of context. What's the state of knowledge? Why is this
research needed? What existing data or work are you building on?]

---

## Methodology

### Overview

<!--
Describe your overall approach in plain language. This section should
make sense to someone who isn't an expert in your field.
-->

[Brief description of your approach. e.g., "Systematic collection and
independent verification of [records] from public sources, structured
into a queryable dataset with defined verification levels."]

### Lines of Attack

<!--
"Lines of Attack" (LOAs) are your search strategies -- the different
ways you plan to find records and evidence. Each LOA targets a specific
type of source. Having multiple LOAs gives your dataset breadth and
helps find things that any single approach would miss.

EXAMPLE (from the ESD project, which used 14 LOAs):
  LOA1:  News archive search (newspapers.com, Google News)
  LOA2:  Misclassified drowning investigation (CDC WONDER, coroner data)
  LOA3:  Legal records (PACER, FindLaw, state courts)
  LOA4:  Government records (OSHA, CPSC, USCG)
  LOA5:  Academic literature (PubMed, Google Scholar)
  LOA6:  Community sources (Reddit, boating forums, GoFundMe)
  LOA11: YouTube video search (local TV news archives)

You probably won't have 14 lines of attack. Three to five is a good
start. You can always add more as you discover new source types.

Mark each LOA's status so you (and Claude) know what's been done:
  NOT STARTED | IN PROGRESS | COMPLETE | BLOCKED
-->

| LOA | Name | Source Type | Status |
|-----|------|------------|--------|
| LOA1 | [e.g., Academic literature] | [e.g., PubMed, Google Scholar] | NOT STARTED |
| LOA2 | [e.g., Government reports] | [e.g., CDC, WHO, state health depts] | NOT STARTED |
| LOA3 | [e.g., News archive search] | [e.g., Google News, news databases] | NOT STARTED |
| LOA4 | [e.g., Institutional data] | [e.g., Hospital networks, registries] | NOT STARTED |
| [Add more as needed] | | | |

### LOA Details

#### LOA1: [Name]

**What:** [What are you searching for?]
**Where:** [Specific databases, websites, or archives]
**Search terms:** [Key search queries you plan to use]
**Expected yield:** [Rough estimate of what you expect to find]
**Status:** NOT STARTED

<!--
Copy this block for each LOA. Fill in details as you execute each one.
After completing a LOA, add a results summary:

**Results:** Found X records. Y were new, Z were duplicates of existing
entries. Key findings: [brief summary].
-->

#### LOA2: [Name]

**What:** [What are you searching for?]
**Where:** [Specific databases, websites, or archives]
**Search terms:** [Key search queries you plan to use]
**Expected yield:** [Rough estimate]
**Status:** NOT STARTED

---

## Source Strategy

<!--
This section defines HOW you evaluate sources. It complements the source
rules in CLAUDE.md (which define WHAT sources to use and avoid) by
explaining your quality criteria.
-->

### Source Quality Criteria

| Criterion | High Quality | Acceptable | Low Quality |
|-----------|-------------|------------|-------------|
| Timeliness | [e.g., Published within 1 year of event] | [e.g., Within 5 years] | [e.g., Undated or very old] |
| Independence | [e.g., Original reporting] | [e.g., Cites original sources] | [e.g., Rehashes other coverage] |
| Specificity | [e.g., Names, dates, locations] | [e.g., Some details] | [e.g., Vague references] |
| Reliability | [e.g., Government, peer-reviewed] | [e.g., Established news outlet] | [e.g., Blog, social media] |

### Source Documentation Standard

For every source used, record:
- URL or citation
- Date accessed
- Source type (news, government, academic, etc.)
- What claims it supports

---

## Success Criteria

<!--
How will you know when you're done? Define concrete, measurable targets.
It's okay to revise these as you learn more about your topic.
-->

This research is successful if:

1. [e.g., The dataset contains at least X records covering Y time period]
2. [e.g., At least Z% of records are independently verified (CONFIRMED or higher)]
3. [e.g., Every [region/category/time period] in scope has been systematically searched]
4. [e.g., The dataset can be exported to a clean CSV suitable for statistical analysis]
5. [e.g., Known limitations are documented and honest]

---

## Timeline

<!--
Rough schedule. Research always takes longer than expected, so build in
buffer. Mark milestones as you hit them.

Status: PLANNED | IN PROGRESS | COMPLETE | DELAYED
-->

| Phase | Description | Target Date | Status |
|-------|------------|-------------|--------|
| Setup | Repository, schema, governance docs | [Date] | IN PROGRESS |
| LOA1 | [First line of attack] | [Date] | PLANNED |
| LOA2 | [Second line of attack] | [Date] | PLANNED |
| [Add more phases] | | | |
| Export | Clean dataset export and quality review | [Date] | PLANNED |
| Analysis | [Statistical analysis, visualization, etc.] | [Date] | PLANNED |

---

## Open Questions

<!--
Things you haven't figured out yet. It's better to write down your
uncertainties than to pretend they don't exist. Review this list
periodically and move resolved questions to a "Resolved" section.
-->

- [e.g., "Should pool incidents be included or excluded from scope?"]
- [e.g., "What's the best way to handle records with uncertain dates?"]
- [e.g., "Is there a government dataset that would give us ground truth for validation?"]
