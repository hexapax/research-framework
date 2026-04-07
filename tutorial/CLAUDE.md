# CLAUDE.md -- Vacation Planner Research Project

This file helps Claude Code (or any AI coding assistant) understand how this vacation planner dataset works, so it can guide a researcher in adding, verifying, and maintaining destination entries.

## Project Overview

This is a file-based research project for planning vacations. Each destination is documented in a structured markdown file with YAML frontmatter (like a database record) and a markdown body (like a wiki article). The goal is to build a verified, trustworthy dataset of vacation options -- not just a list of places, but a curated set where costs, travel times, ratings, and seasonal availability have been independently checked.

**Current state:** 5 sample destinations in the dataset, stored as `DEST-NNN.md` files.

**Home base:** Richmond, VA (all travel times are measured from here).

## Repository Structure

```
vacation-planner/
  SCHEMA.md           # Data dictionary -- READ THIS FIRST
  CLAUDE.md           # This file
  DEST-001.md         # Outer Banks, NC (beach, CONFIRMED)
  DEST-002.md         # Canaan Valley, WV (mountain, UNVERIFIED -- travel time wrong)
  DEST-003.md         # Charleston, SC (historical, VERIFIED -- clean entry)
  DEST-004.md         # Shenandoah NP, VA (nature, CONFIRMED)
  DEST-005.md         # Wintergreen, VA (mountain, UNVERIFIED -- multiple issues)
  export_dataset.py   # Generates CSV export and prints summary stats
  review.html         # Interactive HTML review/comparison tool
  exports/
    destinations.csv  # Generated CSV (run export_dataset.py to refresh)
```

## Critical Rules

### Source Independence

The destination's own website is a **primary source** for factual data (prices, hours, amenities) but it is **not an independent review**. Marketing material tells you what a place wants you to believe; independent sources tell you what it is actually like.

| Source Type | Independent? | Good For |
|------------|-------------|----------|
| TripAdvisor, Google Reviews, Yelp | Yes | Ratings, visitor experience |
| Travel blogs (with visit dates) | Yes | Detailed descriptions, tips |
| News articles, travel magazine features | Yes | Context, awards, issues |
| Booking.com, Expedia | Partial | Pricing (yes), ratings (yes), descriptions (often from the hotel) |
| Hotel/resort's own website | No | Current pricing, amenities, hours |
| Tourism board marketing | No | General area info (verify specifics independently) |

### Data Freshness

Prices and availability go stale. Every entry has a `cost_date_checked` field. If it is more than 6 months old, the cost estimate should be treated as unreliable and the entry should not be upgraded to VERIFIED until pricing is rechecked.

### Verification Levels

| Level | When to Use |
|-------|------------|
| **VERIFIED** | Cost, travel time, ratings, and availability confirmed by 2+ independent sources. No unresolved discrepancies in `research_notes`. |
| **CONFIRMED** | At least one independent source confirms key facts. Minor or explained discrepancies are acceptable. |
| **UNVERIFIED** | Single source, or known unresolved discrepancies. Needs more research before recommending. |

## How to Add a New Destination

### Step 1: Check for duplicates

```bash
# Search by name
grep -rl "Resort Name" DEST-*.md

# Search by city
grep -rl "City Name" DEST-*.md
```

### Step 2: Determine the next ID

```bash
ls DEST-*.md | tail -1
# If the last file is DEST-005.md, the next ID is DEST-006
```

### Step 3: Create the file

Create `DEST-NNN.md` following the schema in `SCHEMA.md`. Every file must have:

1. YAML frontmatter between `---` markers with all required fields
2. Markdown body with Summary, What to Do, and Known Issues sections

Minimal template:

```yaml
---
destination_id: DEST-NNN
destination_name: "Name"
city: "City"
state_or_country: XX
type: beach
travel_time_hours: 0.0
travel_time_source: "Google Maps, checked YYYY-MM-DD"
estimated_cost_per_person_per_night: 0
cost_date_checked: "YYYY-MM-DD"
overall_rating: 0.0
ratings_breakdown: {}
best_season: ""
seasonal_closures: "none"
highlights: []
verification_level: UNVERIFIED
sources: []
notes: ""
research_notes: ""
---

# DEST-NNN: Name -- City, State

## Summary

[2-3 sentence description]

## What to Do

- [Activity 1]
- [Activity 2]

## Known Issues

- [Any data quality concerns]
```

### Step 4: Research and fill in

For each destination, gather:

1. **Travel time**: Check Google Maps from Richmond, VA. Record the date you checked.
2. **Cost**: Check Booking.com or Expedia for a representative stay. Record the date.
3. **Ratings**: Check at least TripAdvisor and Google. Record each rating separately in `ratings_breakdown`, then compute the average for `overall_rating`.
4. **Highlights**: What would you actually do there? Be specific.
5. **Seasonal closures**: Check the destination's own website for closure dates. Cross-reference with a review source if possible.
6. **Sources**: List every source you used with URL, name, access date, and type.

### Step 5: Set verification level

- If you found 2+ independent sources that agree on key facts: **VERIFIED**
- If you found 1 independent source: **CONFIRMED**
- If you only have the destination's own website or unresolved discrepancies: **UNVERIFIED**

### Step 6: Regenerate exports

```bash
python3 export_dataset.py
```

## How to Verify an Existing Destination

Verification means checking claims against independent sources. Common tasks:

1. **Check travel time**: Open Google Maps, enter "Richmond, VA to [destination]", record the drive time and the date. If it disagrees with the file, update `travel_time_hours` and `travel_time_source`, and note the old value in `research_notes`.

2. **Check pricing**: Search Booking.com or Expedia for a representative stay. If the price has changed, update `estimated_cost_per_person_per_night` and `cost_date_checked`. Note the old price in `research_notes`.

3. **Check ratings**: Look up TripAdvisor and Google Reviews. If ratings have shifted, update `ratings_breakdown` and recompute `overall_rating`.

4. **Check seasonal info**: Verify closure dates on the destination's official website and cross-reference with recent reviews mentioning closures.

5. **Document discrepancies**: If sources disagree, document the disagreement in `research_notes`. Do not hide discrepancies -- they are valuable information.

After verification, consider upgrading `verification_level` if the entry now meets a higher standard.

## Common Tasks

### "Find a beach destination under $100/night"
```bash
grep -l 'type: beach' DEST-*.md | xargs grep -l 'estimated_cost_per_person_per_night:'
```
Or use the `review.html` interactive tool with the cost slider and type filter.

### "Which entries need verification?"
```bash
grep -l 'verification_level: UNVERIFIED' DEST-*.md
```

### "Update the exports"
```bash
python3 export_dataset.py
```

### "Open the review tool"
Open `review.html` in a browser. It contains embedded data and works offline. After adding new destinations, update the JSON data in the HTML file to include the new entries.

## What Not to Do

- Do not use a destination's own marketing copy as the "summary" -- write your own based on independent sources
- Do not list a destination as VERIFIED if the cost data is more than 6 months old
- Do not delete entries -- if a destination turns out to be unsuitable, add notes explaining why and leave it in the dataset for reference
- Do not average ratings from incompatible scales without normalizing first (see SCHEMA.md for normalization rules)
