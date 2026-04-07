---
name: verify
description: Verify an existing dataset record against independent sources
user-invocable: true
argument-hint: "[record ID or filename]"
---

# Verify: Check a Record Against Independent Sources

Search for independent sources that confirm or contradict the claims in an existing record. Update the record's verification level and source list.

## When to Use

Run `/verify` after you have records in the dataset that need independent confirmation. This is the core research quality step -- it's what separates a list from a verified dataset.

## Workflow

### Step 1: Select a Record

If the user provided an argument (e.g., `/verify DEST-002`), find that record. Otherwise, list unverified records and let the user pick:

```bash
grep -l 'verification_level: UNVERIFIED' dataset/*.md
```

Show a numbered list with the record ID and a one-line summary for each. Ask the user which one to verify. If there are many, suggest starting with the one most likely to have findable sources.

### Step 2: Read the Record

Read the full record file. Note:
- What claims need verification (dates, locations, counts, descriptions)
- What sources already exist
- What's in the `research_notes` field (may mention known discrepancies)
- What the current `verification_level` is

### Step 3: Read the Source Rules

Read `CLAUDE.md` to understand which sources are independent and which are not. The key question: "Is this source derived from the subject of study, or is it independent?"

For example, in the ESD research project, the ESDPA website is the subject of study, not an independent source. A news article about the same incident IS independent.

### Step 4: Search for Independent Sources

Using available search tools (built-in web search, or MCP tools like Perplexity if configured), search for independent confirmation:

1. Search by key identifying details (names, dates, locations)
2. Search for the event/incident/case in news archives
3. Search for academic or government sources
4. Search for related records (obituaries, court records, reports)

For each search:
- Note what you searched for
- Note what you found (or that you found nothing)
- Assess whether the source is independent per the project's source rules

### Step 5: Evaluate Each Source Found

For each potential source, determine:
- **Is it independent?** Does it derive from the subject of study, or is it original reporting/data?
- **Does it confirm or contradict?** Does it agree with the record's claims, disagree, or add new information?
- **What is the source quality?** Primary source (government data, court record) vs. secondary (news article) vs. tertiary (blog post, forum)

### Step 6: Update the Record

Update the record file with:
- New sources added to the `sources` list (URL, name, date accessed, type)
- Updated `independent_source_count`
- Any corrections to existing fields (with the old value noted in `research_notes`)
- Updated `verification_level` if warranted:
  - Upgrade from UNVERIFIED to CONFIRMED if 1 independent source found
  - Upgrade from CONFIRMED to VERIFIED if 2+ independent sources agree on key facts
  - Do NOT downgrade without discussing with the user first
- Updated `research_notes` documenting what was searched and what was found

### Step 7: Report Results

Summarize for the user:
- "Found N new independent sources for [record]"
- What was confirmed, what was contradicted, what's still unknown
- Whether the verification level changed
- Any discrepancies that need the user's judgment

If nothing was found:
- "Searched for [terms] using [tools]. No independent sources found."
- Note the search attempt in `research_notes` so future sessions don't repeat the same searches
- Suggest alternative search strategies if applicable

## Error Handling

- **No unverified records:** "All records are verified or confirmed. You can still run /verify on a specific record to search for additional sources."
- **Search tools unavailable:** "Web search is not available in this session. You can verify manually by checking [suggested sources] and updating the record."
- **Source is ambiguous:** If it's unclear whether a source is independent, flag it in `research_notes` and ask the user: "Is [source] independent from [subject of study]?"
- **Conflicting information found:** Do NOT silently pick one version. Document both in `research_notes` and ask the user which to use as the primary value.

## References

- Read `CLAUDE.md` for source independence rules specific to this project
- Read `dataset/SCHEMA.md` for verification level definitions
