---
name: search
description: Search for information to add to the research dataset
user-invocable: true
argument-hint: "[what to search for]"
---

# Search: Find Information for the Dataset

Run structured searches using available tools, present findings with source quality assessment, and offer to create records from promising results.

## When to Use

Run `/search` when you want to find new data points to add to the dataset. This is the discovery phase -- casting a wide net, then filtering for quality.

## Workflow

### Step 1: Understand the Search Goal

If the user provided an argument (e.g., `/search measles outbreaks Ohio 2020-2025`), use that. Otherwise ask: "What are you looking for?"

Clarify scope if needed:
- Time period
- Geographic area
- Type of record (incident, case, study, etc.)
- Any specific details (names, organizations, legislation)

### Step 2: Build Search Queries

Read `CLAUDE.md` for domain-specific search patterns and terms. Build 3-5 search queries that approach the topic from different angles:

- Specific terms: exact names, locations, dates
- Broader terms: category + region + time period
- Source-specific: site:cdc.gov, site:scholar.google.com, etc.
- Variant phrasings: different terms for the same concept

### Step 3: Execute Searches

Use available search tools in this order of preference:
1. **MCP search tools** (Perplexity, Brave, etc.) if configured -- most powerful
2. **Built-in web search** -- always available
3. **Specific site searches** via web fetch if targeting a known database

For each search:
- Run the query
- Note the tool used
- Record the number of results

Limit to 5-8 searches per session to avoid information overload.

### Step 4: Evaluate Results

For each promising result, assess:
- **Relevance:** Does this actually match what we're looking for?
- **Source quality:** Primary source (government, court, academic) vs. secondary (news) vs. tertiary (blog, forum)?
- **Independence:** Is this source independent per the project's CLAUDE.md source rules?
- **Novelty:** Is this already in the dataset? Check existing records.

### Step 5: Present Findings

Present results to the user as a numbered list:

```
Found 4 potentially relevant results:

1. [Title] -- [Source type]
   URL: [url]
   Key details: [1-2 sentence summary]
   Source quality: [primary/secondary/tertiary]
   Already in dataset: [yes/no/maybe]

2. ...
```

### Step 6: Offer Next Steps

For each promising result:
- "Want me to add this to the dataset? (I'll run /collect)"
- "Want me to verify an existing record with this source? (I'll run /verify)"
- "Want me to search deeper on this specific finding?"

If nothing relevant was found:
- Suggest alternative search terms
- Suggest broadening the time period or geographic scope
- Note what was searched so it's not repeated

## Error Handling

- **No search tools available:** "I don't have web search access in this session. Here are search queries you can run manually: [list]. Copy these into your browser or a search tool."
- **All results are from excluded sources:** "All results trace back to [subject of study source]. No independent sources found. Try searching for [alternative terms]."
- **Too many results:** Focus on the top 5-8 most relevant and highest quality. Note that more exist if the user wants to go deeper.
- **Rate limited or search errors:** Note the error, try alternative search tools, or suggest the user try again later.

## References

- Read `CLAUDE.md` for search terms, source rules, and domain-specific patterns
- Read `dataset/SCHEMA.md` to understand what fields to look for in search results
- Check existing records in `dataset/` to avoid duplicating what's already there
