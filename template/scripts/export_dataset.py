#!/usr/bin/env python3
"""
Export dataset from YAML frontmatter to CSV.

Reads all .md files in ../dataset/ (excluding SCHEMA.md), parses their
YAML frontmatter, and writes a flat CSV to ../dataset/exports/. Also
prints summary statistics to stdout.

This is a STARTER exporter that handles flat fields (strings, numbers,
dates) and simple lists (joined with semicolons). If your schema has
complex nested objects (like an array of people with per-person fields),
ask Claude to extend this script for your specific schema.

Usage:
    python3 scripts/export_dataset.py

Dependencies:
    pip install pyyaml
    (openpyxl is optional -- for XLSX export, ask Claude to add it)
"""

import csv
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "\n"
        "  PyYAML is not installed. Install it with:\n"
        "\n"
        "      pip install pyyaml\n"
        "\n"
        "  Or install all project dependencies:\n"
        "\n"
        "      pip install -r requirements.txt\n"
        "\n"
        "  (If you're using Claude Code, ask Claude to install it for you.)\n",
        file=sys.stderr,
    )
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Files matching this pattern are treated as records. Everything else in
# the dataset directory is ignored (SCHEMA.md, README.md, etc.).
RECORD_GLOB = "*.md"

# Files to skip even if they match the glob.
SKIP_FILES = {"SCHEMA.md", "README.md"}

# Output filename (inside dataset/exports/).
OUTPUT_CSV = "dataset.csv"


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file.

    Returns the parsed YAML as a dict, or None if parsing fails.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\n(.*?\n)---", content, re.DOTALL)
    if not match:
        print(f"  WARNING: No YAML frontmatter in {filepath.name}", file=sys.stderr)
        return None

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        print(f"  WARNING: YAML parse error in {filepath.name}: {e}", file=sys.stderr)
        return None

    if not isinstance(data, dict):
        print(f"  WARNING: Frontmatter is not a mapping in {filepath.name}", file=sys.stderr)
        return None

    return data


# ---------------------------------------------------------------------------
# Flattening
# ---------------------------------------------------------------------------


def flatten_record(record):
    """Flatten a YAML record into a flat dict suitable for CSV export.

    Handling rules:
      - Strings, numbers, booleans, dates: kept as-is
      - Lists of strings/numbers: joined with "; "
      - Dicts and lists of dicts: skipped with a placeholder
        (extend this function for your schema's specific nested objects)
      - None values: converted to empty string
    """
    flat = {}

    for key, value in record.items():
        if value is None:
            flat[key] = ""

        elif isinstance(value, (str, int, float, bool)):
            flat[key] = value

        elif isinstance(value, list):
            if len(value) == 0:
                flat[key] = ""
            elif all(isinstance(item, (str, int, float)) for item in value):
                # Simple list -- join with semicolons
                flat[key] = "; ".join(str(item) for item in value)
            elif all(isinstance(item, dict) for item in value):
                # List of objects -- summarize with count and skip details.
                # EXTEND THIS for your schema. For example, if you have a
                # "victims" array with per-person fields, add custom logic
                # here to expand each victim into separate columns or rows.
                flat[f"{key}_count"] = len(value)

                # Try to extract a "name" or first string field as a summary
                names = []
                for item in value:
                    for candidate_key in ("name", "title", "url", "first_name"):
                        if candidate_key in item:
                            names.append(str(item[candidate_key]))
                            break
                if names:
                    flat[f"{key}_summary"] = "; ".join(names)
            else:
                # Mixed list -- join what we can
                flat[key] = "; ".join(str(item) for item in value)

        elif isinstance(value, dict):
            # Nested object -- skip with a placeholder.
            # EXTEND THIS for your schema. For example, if you have a
            # "coordinates" dict with lat/lon, you could expand it:
            #   flat["latitude"] = value.get("lat", "")
            #   flat["longitude"] = value.get("lon", "")
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, (str, int, float, bool)):
                    flat[f"{key}_{sub_key}"] = sub_value
                elif sub_value is None:
                    flat[f"{key}_{sub_key}"] = ""
                # Deeper nesting is skipped

        else:
            flat[key] = str(value)

    return flat


# ---------------------------------------------------------------------------
# Column ordering
# ---------------------------------------------------------------------------


def determine_columns(flat_records):
    """Build a stable column order from all flattened records.

    Columns appear in the order they're first encountered (which follows
    YAML field order in the first record), with any columns unique to
    later records appended at the end.
    """
    seen = set()
    ordered = []
    for rec in flat_records:
        for key in rec.keys():
            if key not in seen:
                seen.add(key)
                ordered.append(key)
    return ordered


# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------


def print_summary(records_raw):
    """Print summary statistics to stdout."""
    n = len(records_raw)
    print(f"\n{'=' * 60}")
    print(f"  Dataset Export Summary")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'=' * 60}\n")
    print(f"  Total records: {n}")

    if n == 0:
        return

    # Field completeness -- what percentage of records have each field filled in?
    all_keys = set()
    for r in records_raw:
        all_keys.update(r.keys())

    print(f"\n  Field completeness:")
    completeness = []
    for key in sorted(all_keys):
        filled = sum(
            1 for r in records_raw
            if r.get(key) is not None
            and r.get(key) != ""
            and r.get(key) != []
            and r.get(key) != {}
        )
        pct = filled / n * 100
        completeness.append((key, filled, pct))

    # Show fields with less than 100% completeness (the interesting ones)
    incomplete = [(k, f, p) for k, f, p in completeness if p < 100]
    if incomplete:
        for key, filled, pct in incomplete:
            print(f"    {key}: {filled}/{n} ({pct:.0f}%)")
    else:
        print(f"    All fields 100% complete across {n} records.")

    # Verification breakdown (if the field exists)
    has_verification = any("verification_level" in r for r in records_raw)
    if has_verification:
        print(f"\n  By verification level:")
        levels = {}
        for r in records_raw:
            v = r.get("verification_level", "unknown")
            levels[v] = levels.get(v, 0) + 1
        for level, count in sorted(levels.items(), key=lambda x: -x[1]):
            pct = count / n * 100
            print(f"    {level}: {count} ({pct:.0f}%)")

    # Year breakdown (if the field exists)
    has_year = any("year" in r for r in records_raw)
    if has_year:
        years = [r["year"] for r in records_raw if r.get("year")]
        if years:
            print(f"\n  Year range: {min(years)} - {max(years)}")

    print(f"\n{'=' * 60}\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    # Resolve paths relative to this script's location.
    # Script lives in scripts/, dataset lives in ../dataset/
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    dataset_dir = project_root / "dataset"
    exports_dir = dataset_dir / "exports"

    if not dataset_dir.exists():
        print(f"Dataset directory not found: {dataset_dir}", file=sys.stderr)
        print("Make sure this script is in the 'scripts/' directory.", file=sys.stderr)
        sys.exit(1)

    exports_dir.mkdir(parents=True, exist_ok=True)

    # Find record files
    md_files = sorted(dataset_dir.glob(RECORD_GLOB))
    record_files = [f for f in md_files if f.name not in SKIP_FILES]

    if not record_files:
        print(f"No record files found in {dataset_dir}", file=sys.stderr)
        print(f"(Looking for {RECORD_GLOB}, excluding {SKIP_FILES})", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(record_files)} record file(s)...\n")

    # Parse all files
    records_raw = []
    records_flat = []
    for filepath in record_files:
        data = parse_frontmatter(filepath)
        if data:
            records_raw.append(data)
            records_flat.append(flatten_record(data))
            record_id = data.get("record_id", data.get("id", filepath.stem))
            print(f"  Parsed: {record_id}")
        else:
            print(f"  SKIPPED: {filepath.name}")

    if not records_flat:
        print("\nNo valid records to export.", file=sys.stderr)
        sys.exit(1)

    # Determine columns and write CSV
    columns = determine_columns(records_flat)
    csv_path = exports_dir / OUTPUT_CSV

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for rec in records_flat:
            writer.writerow(rec)

    print(f"\nExported {len(records_flat)} records to: {csv_path}")

    # Print summary
    print_summary(records_raw)


if __name__ == "__main__":
    main()
