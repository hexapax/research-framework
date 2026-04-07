#!/usr/bin/env python3
"""
Export vacation destination dataset from YAML frontmatter to CSV.

Reads all DEST-*.md files in this directory, parses their YAML frontmatter,
and writes a flat CSV to exports/destinations.csv. Also prints summary
statistics to stdout.

Usage:
    python3 export_dataset.py
"""

import csv
import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file.

    Returns the parsed YAML as a dict, or None if parsing fails.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?\n)---", content, re.DOTALL)
    if not match:
        print(f"  WARNING: No YAML frontmatter found in {filepath}", file=sys.stderr)
        return None

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        print(f"  WARNING: YAML parse error in {filepath}: {e}", file=sys.stderr)
        return None

    return data


def flatten_for_csv(record):
    """Flatten a parsed YAML record into a flat dict suitable for CSV export.

    Complex fields (lists, nested dicts) are converted to strings.
    """
    flat = {}

    # Scalar fields -- copy directly
    scalar_fields = [
        "destination_id",
        "destination_name",
        "city",
        "state_or_country",
        "type",
        "travel_time_hours",
        "travel_time_source",
        "estimated_cost_per_person_per_night",
        "cost_date_checked",
        "overall_rating",
        "best_season",
        "seasonal_closures",
        "verification_level",
        "notes",
        "research_notes",
    ]
    for field in scalar_fields:
        flat[field] = record.get(field, "")

    # Highlights -- join as semicolon-separated string
    highlights = record.get("highlights", [])
    flat["highlights"] = "; ".join(highlights) if highlights else ""

    # Ratings breakdown -- expand to individual columns
    ratings = record.get("ratings_breakdown", {})
    if ratings:
        for source_name, rating_value in ratings.items():
            flat[f"rating_{source_name}"] = rating_value
    flat["ratings_source_count"] = len(ratings) if ratings else 0

    # Sources -- count and list names
    sources = record.get("sources", [])
    flat["source_count"] = len(sources)
    flat["source_names"] = "; ".join(
        s.get("name", "unknown") for s in sources
    )

    return flat


def collect_all_csv_columns(records):
    """Determine the full set of CSV columns across all records.

    Because ratings_breakdown keys vary, we need to scan all records first.
    """
    all_keys = set()
    for rec in records:
        all_keys.update(rec.keys())

    # Define a stable column order: fixed columns first, then dynamic rating columns
    fixed_order = [
        "destination_id",
        "destination_name",
        "city",
        "state_or_country",
        "type",
        "travel_time_hours",
        "travel_time_source",
        "estimated_cost_per_person_per_night",
        "cost_date_checked",
        "overall_rating",
        "ratings_source_count",
        "best_season",
        "seasonal_closures",
        "highlights",
        "verification_level",
        "source_count",
        "source_names",
        "notes",
        "research_notes",
    ]

    # Add any rating_* columns in sorted order
    rating_cols = sorted(k for k in all_keys if k.startswith("rating_"))
    for col in rating_cols:
        if col not in fixed_order:
            # Insert rating columns after ratings_source_count
            idx = fixed_order.index("ratings_source_count") + 1
            fixed_order.insert(idx, col)

    return fixed_order


def print_summary(records_raw):
    """Print summary statistics to stdout."""
    n = len(records_raw)
    print(f"\n{'='*60}")
    print(f"  Vacation Planner Dataset Export")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}\n")
    print(f"  Total destinations: {n}")

    if n == 0:
        return

    # Average cost
    costs = [r.get("estimated_cost_per_person_per_night", 0) for r in records_raw if r.get("estimated_cost_per_person_per_night")]
    if costs:
        avg_cost = sum(costs) / len(costs)
        min_cost = min(costs)
        max_cost = max(costs)
        print(f"  Cost range: ${min_cost} - ${max_cost} per person/night")
        print(f"  Average cost: ${avg_cost:.0f} per person/night")

    # Average rating
    ratings = [r.get("overall_rating", 0) for r in records_raw if r.get("overall_rating")]
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        print(f"  Average rating: {avg_rating:.2f} / 5.0")

    # Type breakdown
    print(f"\n  By type:")
    types = {}
    for r in records_raw:
        t = r.get("type", "unknown")
        types[t] = types.get(t, 0) + 1
    for t in sorted(types.keys()):
        print(f"    {t}: {types[t]}")

    # Verification breakdown
    print(f"\n  By verification level:")
    levels = {}
    for r in records_raw:
        v = r.get("verification_level", "unknown")
        levels[v] = levels.get(v, 0) + 1
    for level in ["VERIFIED", "CONFIRMED", "UNVERIFIED"]:
        count = levels.get(level, 0)
        pct = (count / n * 100) if n > 0 else 0
        print(f"    {level}: {count} ({pct:.0f}%)")

    # Travel time
    times = [r.get("travel_time_hours", 0) for r in records_raw if r.get("travel_time_hours")]
    if times:
        avg_time = sum(times) / len(times)
        print(f"\n  Travel time range: {min(times):.1f} - {max(times):.1f} hours")
        print(f"  Average travel time: {avg_time:.1f} hours")

    print(f"\n{'='*60}\n")


def main():
    script_dir = Path(__file__).parent
    exports_dir = script_dir / "exports"
    exports_dir.mkdir(exist_ok=True)

    # Find all DEST-*.md files
    dest_files = sorted(script_dir.glob("DEST-*.md"))
    if not dest_files:
        print("No DEST-*.md files found.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(dest_files)} destination file(s)...\n")

    # Parse all files
    records_raw = []
    records_flat = []
    for filepath in dest_files:
        data = parse_frontmatter(filepath)
        if data:
            records_raw.append(data)
            records_flat.append(flatten_for_csv(data))
            print(f"  Parsed: {data.get('destination_id', '???')} - {data.get('destination_name', '???')}")
        else:
            print(f"  SKIPPED: {filepath.name}")

    if not records_flat:
        print("\nNo valid records to export.", file=sys.stderr)
        sys.exit(1)

    # Determine columns and write CSV
    columns = collect_all_csv_columns(records_flat)
    csv_path = exports_dir / "destinations.csv"

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for rec in records_flat:
            writer.writerow(rec)

    print(f"\nExported CSV to: {csv_path}")

    # Print summary
    print_summary(records_raw)


if __name__ == "__main__":
    main()
