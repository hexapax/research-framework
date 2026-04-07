# Vacation Planner Dataset Schema

This document defines the YAML frontmatter fields used in each destination file (`DEST-NNN.md`).

## File Naming

Files are named `DEST-NNN.md` where NNN is a zero-padded three-digit sequence number starting at 001.

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `destination_id` | string | Unique identifier in format `DEST-NNN` |
| `destination_name` | string | Common name of the destination (resort, park, area) |
| `city` | string | City or nearest town |
| `state_or_country` | string | US state abbreviation or country name |
| `type` | enum | One of: `beach`, `mountain`, `city`, `nature`, `historical` |
| `travel_time_hours` | float | Driving time from home base (Richmond, VA) in hours |
| `travel_time_source` | string | How travel time was determined (e.g., "Google Maps, checked 2026-03-15") |
| `estimated_cost_per_person_per_night` | int | Estimated lodging cost in USD per person per night |
| `cost_date_checked` | string | ISO date when the cost was last verified |
| `overall_rating` | float | Averaged rating on 1.0-5.0 scale from sources listed |
| `ratings_breakdown` | map | Individual ratings from each source (e.g., `tripadvisor: 4.5`) |
| `best_season` | string | Best time to visit (e.g., "May-September", "Year-round") |
| `seasonal_closures` | string | Any known closure periods, or "none" |
| `highlights` | list | Activities, attractions, and things to do |
| `verification_level` | enum | One of: `VERIFIED`, `CONFIRMED`, `UNVERIFIED` (see below) |
| `sources` | list | Research sources (see Source format below) |
| `notes` | string | General notes about the destination |
| `research_notes` | string | Internal notes about data quality, discrepancies, or follow-up needed |

## Verification Levels

| Level | Criteria |
|-------|----------|
| **VERIFIED** | Cost, travel time, ratings, and availability confirmed by 2+ independent sources. No unresolved discrepancies. |
| **CONFIRMED** | At least one independent source confirms key facts. Minor discrepancies may exist. |
| **UNVERIFIED** | Based on a single source or marketing material only. Key claims not independently checked. |

"Independent" means the source is not the destination's own marketing. A hotel's website listing its own price is a primary source for cost but not an independent review. TripAdvisor, Google Reviews, travel blogs with dated visit reports, and news articles count as independent.

## Source Format

Each entry in the `sources` list should have:

```yaml
sources:
  - name: "TripAdvisor"
    url: "https://www.tripadvisor.com/Hotel_Review-..."
    date_accessed: "2026-03-20"
    type: review_aggregator
  - name: "Hotel Website"
    url: "https://www.example-resort.com/rates"
    date_accessed: "2026-03-20"
    type: marketing
```

Source types:
- `review_aggregator` — TripAdvisor, Google Reviews, Yelp
- `travel_blog` — Independent travel blogs with visit dates
- `news` — News articles, travel section features
- `marketing` — The destination's own website or brochures
- `government` — NPS, state tourism boards, official park sites
- `booking` — Booking.com, Hotels.com, Expedia (price sources)
- `mapping` — Google Maps, Apple Maps (travel time sources)

## Ratings Breakdown

The `overall_rating` is the simple average of all individual ratings in `ratings_breakdown`. Ratings should be normalized to a 1.0-5.0 scale. If a source uses a 10-point scale, divide by 2. If a source uses percentage, multiply by 0.05.

```yaml
ratings_breakdown:
  tripadvisor: 4.5
  google: 4.2
  expedia: 4.0
overall_rating: 4.23  # average of the three
```

## Markdown Body

After the YAML frontmatter, the markdown body should include:

1. **H1 heading** with destination name and location
2. **Summary** section with 2-3 sentence overview
3. **What to Do** section listing specific activities
4. **Known Issues** section documenting any data discrepancies or concerns
