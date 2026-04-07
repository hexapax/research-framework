# Vacation Planner Tutorial

Hey Nicole -- this is your hands-on walkthrough for the vacation planner project. By the end, you'll have added your own destination, caught some data quality issues, and seen what it looks like to build a real, verified dataset. The whole thing takes about 30 minutes, and you can stop and come back at any point.

Everything you need is already in this folder. Let's go.

---

## Step 1: Open This Folder in Claude Code Desktop

Open Claude Code Desktop and point it at this `tutorial/` folder. Claude will read the `CLAUDE.md` file automatically -- that's the instruction sheet that tells it how this project works, what the data looks like, and what rules to follow.

You don't need to read CLAUDE.md yourself (though you can if you're curious). The point is that Claude already knows the structure, so you can just talk to it naturally.

---

## Step 2: Read a "Good" Record

Open `DEST-003.md` -- the Charleston entry. This is the cleanest record in the dataset, and it's a good example of what a finished, verified destination looks like.

Notice a few things:

- The YAML frontmatter at the top is like a structured database record. Every field has a specific purpose -- travel time, cost, ratings from multiple sources, verification level.
- The markdown body below it reads like a mini travel guide: summary, what to do, known issues.
- The `verification_level` is VERIFIED, which means multiple independent sources confirm the key facts. The `research_notes` field explains why: "All three review sources agree closely (4.5-4.7 range). Cost was verified on Booking.com for a May 2026 weekend stay."
- There are 6 sources listed, from TripAdvisor to the National Park Service to Travel + Leisure. That's what "independently verified" means -- you're not just trusting one website.

This is the gold standard. Not every entry will look this clean, and that's fine. The dataset is honest about what it knows and what it doesn't.

---

## Step 3: Add a Destination You're Actually Interested In

Now the fun part. Type:

```
/collect
```

Claude will walk you through adding a new vacation destination. Pick somewhere you've been thinking about -- maybe a beach trip, a mountain cabin, a city weekend. It doesn't have to be fancy.

Claude will:
- Ask you where you're interested in going
- Research the destination (travel time from Richmond, costs, ratings, things to do)
- Create a new `DEST-006.md` file with all the structured data filled in
- Write the summary and activity sections

You'll see it searching for real information, citing sources, and building the record step by step. If it can't confirm something, it'll mark it as UNVERIFIED and explain why in the research notes. That honesty is the whole point.

---

## Step 4: Verify a Claim

Now try being a fact-checker. Type:

```
/verify
```

Pick one of the existing DEST files and ask Claude to verify a specific claim. Here are some good ones to try:

- **DEST-002 (Canaan Valley)**: You'll notice the `research_notes` say the travel time is wrong. It's listed as 3 hours, but the notes say Google Maps shows 4 hours 35 minutes from Richmond. The blog they got the original number from was probably measuring from DC. Ask Claude to verify the travel time and fix it.

- **DEST-005 (Wintergreen)**: This one has multiple issues flagged in the research notes. The pricing is from April 2025 and the resort raised fees since then. The spa has been closed for renovation since January 2026 but a travel blog still lists it as open. The TripAdvisor rating (3.5) and Google rating (4.0) disagree by half a point. Ask Claude to check any of these.

- **DEST-001 (Outer Banks)**: The cost data is from June 2025. Ask Claude whether the $85/person/night estimate is still accurate for summer 2026.

Verification is where research gets real. You're not just collecting information -- you're checking whether it holds up.

---

## Step 5: Run a Data Quality Check

Type:

```
/clean
```

Claude will scan through all the DEST files looking for data quality issues. The pre-built samples have deliberate problems baked in, so there will be things to find.

You'll likely see it flag things like:

- DEST-002's travel time doesn't match what Google Maps says
- DEST-005's cost data is over a year old
- DEST-005's spa is listed as a highlight but is actually closed for renovation
- Rating discrepancies between sources (which may or may not be real problems -- sometimes different sources genuinely measure different things)

The point here is that "clean data" doesn't mean "no issues." It means you know what the issues are and you've documented them honestly. Every discrepancy in the research notes is a feature, not a bug.

---

## Step 6: Export the Dataset

Type:

```
/export
```

Claude will run `export_dataset.py`, which reads all the DEST files and generates a CSV at `exports/destinations.csv`. You'll see summary statistics printed out -- total destinations, cost range, average rating, breakdown by type and verification level.

If you added a new destination in Step 3, it will show up in the export. Open the CSV in Excel or Google Sheets if you want to see the flat tabular view of your data.

---

## Step 7: Explore the Review Tool

Open `review.html` in your browser. (Just double-click it -- it works offline, no server needed.)

This is an interactive dashboard for the dataset. You can:

- **Filter** by type (beach, mountain, nature, historical) or verification level
- **Sort** by any column -- try sorting by cost to find the cheapest options, or by rating to find the best-reviewed
- **Slide the cost filter** to see only destinations under a certain price
- **Compare destinations side by side**: check the boxes next to two or three destinations and click Compare. You'll see them laid out with green/red highlighting showing which is better on each dimension

Try comparing DEST-003 (Charleston) and DEST-004 (Shenandoah). Charleston has the higher rating but costs more than twice as much per night. Shenandoah is closer and cheaper. The comparison tool makes these tradeoffs visible at a glance.

Note: If you added a new destination in Step 3, it won't automatically appear in the review tool (the HTML has embedded data). Claude can update the HTML for you if you ask.

---

## Step 8: Save Your Work

Type:

```
/save
```

Claude will commit your changes to git -- any new DEST files you created, any corrections you made, and the updated exports. It'll write a clear commit message describing what changed.

This is how you keep a clean history of your research. Every change is tracked, so you can always see what the data looked like at any point in time.

---

## What You Just Did

Take a step back and look at what happened in the last 30 minutes:

1. You **collected** structured data about a place you're interested in
2. You **verified** claims against independent sources and caught real errors
3. You **cleaned** the dataset by finding and documenting quality issues
4. You **exported** everything to a standard format that any tool can read
5. You **reviewed** the data visually with filtering, sorting, and comparison
6. You **saved** your work with a clear audit trail

What you just did is exactly what research looks like. Same system, different data.

The vacation planner uses travel destinations, costs, and ratings. A real research project might use incident reports, scientific measurements, or legal records. But the workflow is identical: collect, verify, clean, export, review, save. The tools are the same. The discipline is the same. The only thing that changes is the subject matter.

You're ready.
