---
name: export
description: Generate CSV/XLSX exports from the dataset
user-invocable: true
---

# Export: Generate Spreadsheet Exports

Run the export script to produce CSV (and optionally XLSX) files from the dataset records. Handle dependencies automatically.

## When to Use

Run `/export` after adding or updating records. The export creates a spreadsheet you can open in Excel, Google Sheets, or any data analysis tool.

## Workflow

### Step 1: Check Dependencies

Check if PyYAML is installed:

```bash
python3 -c "import yaml; print('PyYAML OK')" 2>&1
```

If PyYAML is not installed, install it:

```bash
pip install pyyaml
```

If openpyxl is needed for XLSX export:

```bash
pip install openpyxl
```

If pip itself has issues (permissions, PATH), try:

```bash
pip install --user pyyaml openpyxl
```

Tell the user what you're installing and why: "Installing PyYAML so the export script can read your data files."

### Step 2: Run the Export Script

```bash
python3 scripts/export_dataset.py
```

If the script doesn't exist yet or fails, check:
- Is there an `export_dataset.py` in `scripts/`?
- Does it point to the right dataset directory?
- Are there any record files in `dataset/`?

### Step 3: Report Results

After a successful export, tell the user:
- How many records were exported
- Where the output file is (e.g., `dataset/exports/dataset.csv`)
- Summary stats from the script output (verification breakdown, date range, etc.)
- Any warnings or skipped records

Suggest: "Open the CSV in Excel or Google Sheets to review your data."

### Step 4: Flag Data Quality Issues

If the export script reports issues (missing fields, parse errors), summarize them:
- "3 records are missing the [field] field"
- "1 record has malformed YAML and was skipped: [filename]"

Suggest: "Run `/clean` to fix these issues."

## Error Handling

- **No records in dataset:** "The dataset directory has no record files. Use `/collect` to add your first record."
- **Export script missing:** "No export script found. I can create a starter export script for your schema. Want me to do that?"
- **Python not installed:** "Python is required for exports. See docs/01-setup-windows.md for installation instructions."
- **Permission errors:** Try running with `--user` flag. If that fails, explain the issue and suggest fixing Python PATH.
- **YAML parse errors in records:** The export script should skip bad files and report them. List the problematic files so the user can fix them.

## References

- The export script lives at `scripts/export_dataset.py`
- Output goes to `dataset/exports/`
- Read `dataset/SCHEMA.md` if you need to create or modify the export script
