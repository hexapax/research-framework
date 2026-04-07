# Exporting Your Data

Your records are stored as individual files -- one per event, one per case, one per whatever you're tracking. That's great for research and version control. But when you want to analyze the data, share it with a colleague, or open it in Excel, you need a spreadsheet.

That's what exporting does. It reads all your record files and combines them into a single CSV or XLSX file.


## What /export Does

When you type `/export`, Claude:

1. **Checks that Python and the required libraries are installed.** If they're not, Claude installs them for you. You don't need to do anything.

2. **Runs the export script.** This reads every record file in your `dataset/` folder, pulls out the YAML fields, and writes them into a spreadsheet.

3. **Reports the results.** How many records were exported, where the file was saved, and any issues found along the way (like a record with broken formatting that had to be skipped).

The output goes to your `dataset/exports/` folder. That's where you'll find the spreadsheet file after each export.


## CSV vs. XLSX: When to Use Which

The export can produce two formats. Here's when to use each.

**CSV (Comma-Separated Values)** is a plain text file that nearly everything can open. Excel, Google Sheets, R, Python, LibreOffice, even a text editor. It's the universal format. If you're not sure what to use, use CSV.

**XLSX (Excel format)** adds features that CSV can't do: multiple sheets, formatting, column widths, and formulas. If you're sending the file to someone who will only open it in Excel, XLSX is nicer to work with.

The default export generates CSV. If you want XLSX too, just ask: "Export to both CSV and XLSX."


## Opening Your Exports

### In Excel

Double-click the CSV or XLSX file. Excel opens it automatically. If you see all the data crammed into column A, that's Excel misreading the CSV delimiter -- go to Data > Text to Columns and select "Comma" as the separator.

### In Google Sheets

Go to Google Sheets, click File > Import, upload the CSV file, and choose "Comma" as the separator. Or upload the file to Google Drive first and double-click it there.

### In R or Python

For researchers who use analysis tools:

```r
# R
data <- read.csv("dataset/exports/dataset.csv")
```

```python
# Python
import pandas as pd
data = pd.read_csv("dataset/exports/dataset.csv")
```

These are one-liners. If you haven't used R or Python before, don't worry about this yet -- the CSV file in Excel or Google Sheets is all you need to get started.


## The Interactive HTML Review Page

Beyond spreadsheets, the framework can generate something more visual: an **interactive HTML review page**. This is a single file you open in your web browser that shows your entire dataset as a filterable, sortable table.

### What it looks like

A clean table with your records as rows and your fields as columns. At the top: a search box and dropdown filters for each category field (like verification level or state). Click any column header to sort. Click any row to see the full details.

### How to generate it

Type `/review` and Claude builds the page from your current data. The output goes to `dataset/review.html`.

### How to use it

Open `review.html` in Chrome, Firefox, Edge, or Safari. Everything works locally -- no internet connection needed, no server to run. The data is embedded right in the HTML file.

Use the filters to explore your data. Want to see only VERIFIED records in Ohio? Set the state filter to OH and the verification filter to VERIFIED. The table updates instantly.

If the review page supports a comparison view, you can check two or more records and compare them side-by-side -- useful for spotting duplicates or seeing how records differ.

### Sharing the review page

The HTML file is self-contained. You can email it to a collaborator and they can open it directly in their browser. No special software needed.


## Sharing Exports

A few ways to share your data with others:

**Email the CSV.** Attach the file from `dataset/exports/`. Simple, universally compatible.

**Share the HTML review page.** Attach `dataset/review.html`. More visual than a spreadsheet, and the recipient doesn't need any software beyond a web browser.

**Push to GitHub.** If your project is on GitHub, the exports folder gets committed along with your records. Anyone with access to the repository can download the latest export.

**Publish to OSF or Zenodo.** For formal sharing with DOIs and citations. See the publishing guide (09-publishing.md) when you're ready for that step.


## Customizing the Export

The starter export script handles simple fields: text, numbers, dates, short lists. It works out of the box for most projects.

But sometimes you need something different. Maybe you want to:

- Combine first_name and last_name into a single full_name column
- Flatten a list of sources into a count instead of a semicolon-separated string
- Include only certain fields for a specific audience
- Calculate a derived value (like days since the last update)

**Just tell Claude what you need.** For example: "I need the export to include a column called full_name that combines first_name and last_name." Claude will modify the export script for you. You don't need to write the code yourself.


## Three Export Sizes

As your dataset grows, you may want different versions of the export for different purposes. The ESD research project uses three:

**Small (key columns only).** Just the essentials: ID, date, location, type, and outcome. Good for a quick overview or a summary table in a paper.

**Medium (adds verification details).** The key columns plus verification level, source count, and data quality notes. Good for methodological discussions or sharing with collaborators who want to see the evidence behind each record.

**Large (everything).** Every field in the schema. Good for your own analysis or for archiving the complete dataset.

You don't need to set this up on day one. Start with a single export that includes everything. If you later find yourself deleting columns in Excel before sharing, that's a sign it's time to ask Claude: "Can you make a smaller export with just these columns: [list]?"


## When to Export

**After adding or changing records.** The export files don't update automatically -- they're a snapshot generated when you run `/export`. If you've added three new records, the CSV still shows the old data until you re-export.

**Before analyzing.** If you're about to do any analysis in Excel, Sheets, or a statistics tool, re-export first so you're working with the latest data.

**Before sharing.** Always generate a fresh export right before you share it. You don't want to send someone a spreadsheet that's three sessions behind your actual dataset.

The `/export` skill is fast -- it takes a few seconds even for large datasets. There's no cost to running it often.
