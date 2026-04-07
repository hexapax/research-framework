---
name: next
description: Suggest what to work on next based on dataset gaps and priorities
user-invocable: true
---

# Next: What Should I Work On?

Scan the dataset for gaps, stale data, and unfinished work. Rank suggestions by expected value and let the user pick what to do.

## When to Use

Run `/next` when you sit down for a research session and aren't sure where to start. It gives you a prioritized to-do list based on the current state of your dataset.

## Workflow

### Step 1: Scan the Dataset

Read all record files in `dataset/` and categorize them:

```bash
# Count by verification level
grep -l 'verification_level: UNVERIFIED' dataset/*.md | wc -l
grep -l 'verification_level: CONFIRMED' dataset/*.md | wc -l
grep -l 'verification_level: VERIFIED' dataset/*.md | wc -l
```

Also scan for:
- Records with `research_notes` mentioning "needs follow-up", "TODO", "discrepancy", "possible duplicate"
- Records with stale date fields (check `stale_after_days` from SCHEMA.md)
- Recently added records (check git log or file modification dates) that haven't been verified
- Empty or near-empty records (minimal fields filled in)

### Step 2: Rank by Priority

Present the top 3-5 suggestions, ordered by expected value:

**Priority 1: Records with known issues**
- Records flagged with discrepancies or TODOs in research_notes
- These have specific, actionable next steps

**Priority 2: Unverified records likely to have findable sources**
- Records with specific names, dates, and locations (easier to verify)
- Records from recent time periods (more likely to have online sources)

**Priority 3: Stale data**
- Records where key fields (cost, dates, counts) are past their staleness threshold
- Quick to update, keeps the dataset current

**Priority 4: Broad gaps**
- Time periods with few records
- Geographic areas with few records
- Categories or types underrepresented in the dataset

### Step 3: Present Suggestions

```
Here's what I'd suggest working on:

1. FIX DISCREPANCY: REC-2024-003 -- research_notes says travel time 
   may be wrong. Quick win: check Google Maps and update.
   -> Run /verify REC-2024-003

2. VERIFY: REC-2024-008 -- Added last session, still UNVERIFIED. 
   Has a specific name and date, good chance of finding sources.
   -> Run /verify REC-2024-008

3. STALE DATA: REC-2023-001 -- cost data is 9 months old. 
   Check current pricing.
   -> Run /verify REC-2023-001

4. GAP: No records from 2021. This may be a real gap or just 
   unsearched. 
   -> Run /search [topic] 2021

Which one do you want to tackle? (Or tell me something else.)
```

### Step 4: Hand Off

When the user picks a suggestion, invoke the appropriate skill:
- Discrepancy or verification -> `/verify [record]`
- Gap filling -> `/search [terms]`
- Stale data -> `/verify [record]` with focus on refreshing specific fields
- Data quality -> `/clean`

## Error Handling

- **Empty dataset:** "Your dataset is empty! The best next step is `/collect` -- let's add your first record."
- **Everything is verified:** "Nice work -- all records are verified. You could: search for new records to add (/search), generate an export (/export), or take a break."
- **Very large dataset:** Focus on the top 5 suggestions. Don't overwhelm with 50 items.

## References

- Read `dataset/SCHEMA.md` for staleness thresholds and required fields
- Read `CLAUDE.md` for project-specific priorities and known gaps
- Check `research_notes` fields across records for actionable items
