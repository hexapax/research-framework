---
name: review
description: Generate an interactive HTML page for reviewing dataset records
user-invocable: true
---

# Review: Generate Interactive HTML Review Page

Create a self-contained HTML file that displays all dataset records in a filterable, sortable, searchable interface. No external dependencies -- the HTML file works by opening it in any browser.

## When to Use

Run `/review` to get a visual overview of the entire dataset. Useful for spotting patterns, comparing records, finding gaps, and presenting the dataset to others.

## Workflow

### Step 1: Read All Records

Scan the `dataset/` directory for record files (`.md` files, excluding SCHEMA.md and scripts).

For each file:
- Parse the YAML frontmatter
- Extract all fields into a data structure
- Note the filename and any markdown body content (summary section)

Also read `dataset/SCHEMA.md` to understand which fields are enums (for filter dropdowns) and which fields are most important (for default visible columns).

```bash
ls dataset/*.md | grep -v SCHEMA | grep -v export | grep -v __
```

### Step 2: Generate the HTML File

Create a single self-contained HTML file with NO external dependencies (no CDN links, no external CSS or JS). Everything must be inline.

The HTML page must include:

**Data table:**
- One row per record
- Columns for key fields from the schema (prioritize: ID, date, location, key descriptive fields, verification level, source count)
- Sortable columns (click header to sort ascending/descending)
- Alternating row colors for readability

**Filters:**
- A text search box that filters across all visible columns
- Dropdown filters for each enum field (e.g., verification_level, incident_type, state)
- Dropdowns should include an "All" option and be populated from actual data values
- Filters should combine (AND logic): selecting a state AND a verification level shows only records matching both

**Record details:**
- Clicking a row expands or opens a detail panel showing all fields for that record
- Include the markdown summary if present

**Comparison view (optional but recommended):**
- Checkboxes on each row to select records
- A "Compare Selected" button that shows selected records side by side
- Highlight differences between compared records

**Summary statistics:**
- Total record count
- Counts by key enum fields (e.g., "45 verified, 30 confirmed, 18 unverified")
- Date range of the dataset

**Styling:**
- Clean, readable design with a neutral color scheme
- Responsive layout that works on different screen widths
- Print-friendly (no critical information hidden behind interactions)

### Step 3: Embed the Data

Embed the dataset as a JSON array inside a `<script>` tag in the HTML:

```html
<script>
const DATA = [
  {"id": "REC-2024-01-01-1", "date": "2024-01-01", ...},
  ...
];
</script>
```

This keeps the file self-contained and portable. All filtering and sorting happens client-side in JavaScript.

### Step 4: Write the File

Write the HTML file to `dataset/review.html`.

```bash
# Confirm the file was written
ls -la dataset/review.html
```

### Step 5: Tell the User

After generating the file:

1. Report the file path: `dataset/review.html`
2. Report record count: "Generated review page with N records"
3. Instruct: "Open this file in your browser to explore the dataset."
4. Note: "This file is self-contained -- share it with collaborators and they can open it directly."

If the project is using git, mention that `review.html` can be committed to the repo or added to `.gitignore` depending on whether the user wants to track it.

## Error Handling

- **No records found:** If the dataset directory has no record files, inform the user and suggest running `/collect` first.
- **YAML parse errors:** Skip records with malformed YAML, but list them in the HTML page under a "Parse Errors" section so the user knows which files need fixing.
- **Very large dataset (500+ records):** The HTML file may be large. Warn the user about file size. Consider paginating the table (show 50 records at a time with page controls) to keep the browser responsive.
- **SCHEMA.md not found:** Generate the page using whatever fields are present in the records. Use the first record's fields as the column list. Note that having SCHEMA.md would improve the review page (proper column ordering, enum filter dropdowns).
- **Previous review.html exists:** Overwrite it. The review page is always regenerated from current data.

## References

- Read `dataset/SCHEMA.md` for field definitions and enum values (used to build filter dropdowns)
- All data comes from `dataset/*.md` record files
