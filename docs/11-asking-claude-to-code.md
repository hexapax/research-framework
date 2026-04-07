# Getting Claude to Build Things for You

Here's the key insight: **you don't need to learn to code. You need to learn to describe what you want.**

Claude can write Python scripts, build interactive web pages, create charts, automate repetitive tasks, and process data in ways that would take you hours to do by hand. You don't need to understand the code it writes. You need to be able to look at the result and say "yes, that's what I wanted" or "no, change this part."

This guide teaches you how to ask well.

---

## What Claude Can Build for You

Here are real examples of things you can ask for, right now, in plain English:

### Custom exports

"I need a CSV with just the date, state, case count, and verification level columns -- nothing else."

"Export all VERIFIED records from 2023 as a spreadsheet, sorted by case count, highest first."

"Create a CSV where each row is a state and the columns are the year, with the cell value being the number of cases that year."

### Interactive web pages

"Build me a dashboard that shows outbreak locations on a US map, colored by severity."

"Create an HTML page where I can filter records by state and year, with a bar chart showing cases over time."

"Make a timeline visualization showing when each outbreak occurred."

These produce self-contained HTML files you can open in any browser and share with anyone. No special software needed.

### Data analysis

"How many verified cases are there per year? Show me a chart."

"What's the average case count by state? Which states have the most outbreaks?"

"Compare the number of outbreaks before and after 2020. Is there a trend?"

### Validation and quality scripts

"Check that every record has at least one source URL."

"Find all records where the date field and the filename date don't match."

"List records that have been UNVERIFIED for more than 30 days."

### File conversion and processing

"Convert these 12 PDF tables into dataset records."

"Read this Excel spreadsheet and create a record file for each row."

"Scan this list of URLs and check which ones are still working."

---

## How to Ask Well

The difference between a frustrating experience and a productive one is how you describe what you want. Here are the patterns that work.

### Be specific about inputs and outputs

**Vague:** "Analyze my data."

**Specific:** "Read all the .md files in dataset/, count how many records have each verification level, and show me the numbers."

**Even better:** "Read all the .md files in dataset/, count how many records have each verification level, and make a bar chart with the levels on the X axis and the count on the Y axis."

Tell Claude what to read, what to do with it, and what the result should look like.

### Show an example of what you want

If you can describe the output, Claude can build it. Sketching an example is the fastest way.

"I want a table that looks like this:"

```
State | 2021 | 2022 | 2023 | 2024 | Total
------|------|------|------|------|------
OH    |    3 |    5 |    2 |    7 |   17
CA    |    8 |    2 |    6 |    3 |   19
```

"Make that from the records in dataset/."

Claude will figure out how to get from your files to that table. You don't need to tell it how -- just what.

### Start small, then scale up

Don't ask for the final perfect version on the first try. Build up to it.

1. "Read one record file and show me the fields it has."
2. "Now read all the record files and count them."
3. "Now make a CSV with the date and state from all records."
4. "Now add a column showing whether each record is verified."
5. "Now make a chart from that data."

Each step takes a few seconds. By step 5 you have exactly what you want, and if something went wrong, you know which step it happened at.

### Iterate on the result

Look at what Claude made. If it's not quite right, tell it what to change.

"That's close, but I want the bars to be blue instead of gray."

"The chart is good, but can you add labels showing the count on top of each bar?"

"This works, but can you also exclude records that are UNVERIFIED?"

"The table is right but the dates are showing as 2024-03-15 -- can you make them say March 15, 2024?"

Small corrections are easy. Claude remembers what it just built and can modify it without starting over.

---

## What Claude Creates

When Claude builds something for you, it creates actual files in your project:

- **Python scripts** go in `scripts/`. These are reusable -- you can run them again anytime.
- **HTML pages** (dashboards, visualizations) go in `dataset/` or wherever makes sense. Open them in your browser.
- **One-off analysis** sometimes happens right in the conversation. Claude shows you the results directly without saving to a file.

If you're not sure where something went, ask: "Where did you save that file?" Claude will tell you the exact path.

---

## Reviewing What Claude Made

You don't need to read the code. But you should always look at the output.

**For a CSV or spreadsheet:** Open it. Do the numbers look right? Does the first row have the column headers you expected? Spot-check a few rows against the actual record files.

**For a chart or visualization:** Does it show what you asked for? Are the labels readable? Does the scale make sense? If a bar chart shows a state with 500 cases but you know it should be 5, something went wrong.

**For an HTML page:** Open it in your browser. Click the filters. Sort the columns. Does everything work? Does the data match what's in your dataset?

If something looks wrong, tell Claude. Be specific: "The chart shows Ohio with 200 cases but there are only 12 Ohio records in the dataset" is much more helpful than "the chart is wrong."

---

## Saving Useful Scripts

When Claude writes a script that does something useful, it's already saved as a file in your project. You don't need to do anything special.

If you want to run it again later:

```
Run the export script in scripts/export_dataset.py
```

Or even simpler:

```
Run the same analysis you did last time -- the cases-by-year chart
```

Claude can find and re-run scripts it created previously.

If a script is particularly useful, mention it to Claude: "This script is important -- add a comment at the top explaining what it does." That way future-you (or a collaborator) can understand it at a glance.

---

## Real Examples

Here are conversations you might actually have:

---

**You:** "I have 80 records in dataset/. Can you show me which states have the most cases?"

**Claude:** *reads all 80 files, counts cases per state, produces a sorted list and a bar chart*

**You:** "Can you make that into a map instead? Color each state by how many cases it has."

**Claude:** *creates an interactive HTML file with a US map, darker colors for more cases, hover to see the count*

---

**You:** "Some of my records have source URLs that might be broken. Can you check them?"

**Claude:** *writes a script that reads each record, extracts URLs from the sources field, checks if they're still accessible, reports which ones return errors*

---

**You:** "I need to send my advisor a one-page summary. Can you make something?"

**Claude:** *generates a clean HTML page with: record count, verification breakdown, date range, top states, a small chart, and a paragraph summarizing the methodology*

---

## The Bridge to Skills

Pay attention to patterns. If you find yourself asking Claude to do the same thing repeatedly -- "check for broken URLs," "generate the summary page," "count records by state" -- that's a sign it should become a skill.

A skill turns a conversation into a single command. Instead of explaining what you want each time, you type `/check-urls` and it just happens.

When you notice a pattern, see [Creating Your Own Workflows](12-creating-skills.md) to turn it into a skill.

---

## Next Steps

- Ready to turn your repeating tasks into one-command workflows? See [Creating Your Own Workflows](12-creating-skills.md).
- Want to add more powerful search tools? See [Adding Search and Research Tools](10-mcp-tools.md).
- Ready to share your dataset with the world? See [Publishing and Sharing Your Research](09-publishing.md).
