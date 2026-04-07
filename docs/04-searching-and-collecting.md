# Searching and Collecting Data

This is the guide to finding information and turning it into structured records. These are the two activities you'll do most often: searching for data, and collecting what you find.

---

## The /search Skill

**What it does:** `/search` helps you find information that might belong in your dataset. You tell Claude what you're looking for, and it builds search queries, runs them, evaluates the results, and presents what it found -- ranked by relevance and source quality.

**How to use it:** Type `/search` followed by what you're looking for. Be as specific or as broad as you want.

**Examples:**

```
/search measles outbreaks in Ohio 2020-2025
```

```
/search CDC reports on measles genotype D8
```

```
/search school-based measles outbreaks with under-vaccination
```

```
/search
```
(If you just type `/search` with nothing after it, Claude will ask what you're looking for.)

### What happens when you run /search

1. **Claude clarifies the goal.** If your request is vague, it might ask: "What time period? What geographic area? Any specific details?"

2. **Claude builds multiple queries.** Instead of running one search, it approaches your question from different angles. For "measles outbreaks in Ohio," it might search for:
   - "measles outbreak Ohio 2020 2021 2022 2023 2024 2025"
   - "measles cases Ohio school" (targeting school-based outbreaks)
   - site:cdc.gov "measles" "Ohio" (targeting CDC specifically)
   - "Columbus measles" OR "Cleveland measles" OR "Cincinnati measles" (targeting major cities)

3. **Claude evaluates what it finds.** Not every search result is worth collecting. Claude assesses relevance, source quality, and whether the information is already in your dataset.

4. **Claude presents a ranked list.** You'll see something like:

   ```
   Found 4 potentially relevant results:

   1. CDC MMWR: Measles Outbreak -- Columbus, Ohio, 2024
      Source quality: Primary (government)
      Already in dataset: No
      Key details: 85 confirmed cases, D8 genotype, linked to school district

   2. Columbus Dispatch: Health officials report measles cluster
      Source quality: Secondary (news with original reporting)
      Already in dataset: No
      Key details: Timeline of outbreak, community response

   3. Ohio Dept of Health: 2024 Measles Surveillance Summary
      Source quality: Primary (government)
      Already in dataset: No
      Key details: Statewide case counts by county

   4. Blog post: "What the media isn't telling you about Columbus measles"
      Source quality: Tertiary (opinion blog)
      Already in dataset: N/A
      Key details: Not recommended -- no original data
   ```

5. **Claude offers next steps.** For each good result: "Want me to add this to the dataset?" (which triggers `/collect`), "Want me to use this to verify an existing record?" (which triggers `/verify`), or "Want me to dig deeper on this one?"

### Tips for better searches

- **Start broad, then narrow.** Your first search might be "measles outbreaks Ohio." If you get too many results, narrow it: "measles outbreaks Columbus Ohio 2024." If you get too few, broaden it: "measles outbreaks Midwest 2020-2025."

- **Try different phrasings.** Not every source uses the same words. "Measles outbreak" might also appear as "measles cluster," "measles cases," "measles exposure," or "measles notification." If your first search comes up short, try synonyms.

- **Check what's already in your dataset.** Before searching externally, Claude checks your existing records. If you already have three Ohio outbreaks documented, it will tell you so you can focus on gaps.

- **Don't search for everything at once.** Five to eight focused searches per session is more productive than thirty rapid-fire queries. Depth beats breadth.

---

## The /collect Skill

**What it does:** `/collect` walks you through adding a new record to your dataset. It asks you questions, checks for duplicates, creates the file with proper formatting, and sets the verification level.

**How to use it:** Type `/collect` followed by a brief description of what you found. Or just type `/collect` and Claude will ask.

**Examples:**

```
/collect measles outbreak in Columbus Ohio, 85 cases, February 2024
```

```
/collect found a CDC report about measles in Oregon
```

```
/collect
```

### What happens when you run /collect

1. **Claude asks what you found.** If you gave a description, it uses that as a starting point. Otherwise it asks: "What did you find?" and "Where did you find it?"

2. **Claude checks for duplicates.** Before creating a new record, it searches your existing files for potential matches. If it finds something close, it will ask: "This looks like it might be the same as OB-2024-OH-001. Is it the same event, or a different one?"

3. **Claude gathers the details.** It reads your SCHEMA.md to know what fields to collect, then asks you for the information it can't extract from what you've already said. It doesn't fire twenty questions at you -- it asks conversationally, filling in what it can from the source.

4. **Claude assesses the source.** It checks your CLAUDE.md source rules to determine if the source is independent. If you found the information from a source you're studying (not an independent source), it will note that.

5. **Claude creates the file.** It generates the record with proper YAML formatting, the correct filename based on your naming convention, and a markdown summary below the frontmatter.

6. **Claude tells you what's next.** It shows you the file it created, lists any fields that are still empty (so you know what to fill in later), and reminds you to run `/export` to update the spreadsheet.

### The questions /collect asks

You won't get all of these every time -- Claude only asks what it doesn't already know:

- What did you find? (the core event or data point)
- Where did you find it? (the source -- a URL, a report name, a database)
- When did it happen? (date or approximate date)
- Where did it happen? (location)
- Any key measurements? (case counts, costs, quantities -- whatever your schema tracks)

If you don't know something, say so. Claude will leave the field empty rather than guess. Empty fields are fine -- they're a natural part of building a dataset. You can fill them in later when you find the information.

---

## Source Quality: Primary, Secondary, and Tertiary

Not all sources are created equal. Understanding source quality helps you build a dataset people can trust.

### Primary sources

**What they are:** Original data from the people who collected or produced it. The first record of something happening.

**Examples:**
- A CDC Morbidity and Mortality Weekly Report (MMWR) declaring an outbreak
- A state health department press release with case counts
- A court ruling in a legal case
- A peer-reviewed journal article presenting original research
- An OSHA inspection report
- A death certificate

**Why they matter:** Primary sources are the foundation of research. They're the closest you can get to "this actually happened."

### Secondary sources

**What they are:** Reports about primary sources. Someone interpreting, summarizing, or re-reporting original data.

**Examples:**
- A newspaper article about a CDC report
- A textbook chapter summarizing published research
- A Wikipedia article citing journal papers
- A TV news segment about a health department announcement

**Why they're still useful:** Secondary sources help you find primary sources you didn't know about. A news article about a measles outbreak might mention a health department report you haven't seen. The news article is your lead; the health department report is your evidence.

### Tertiary sources

**What they are:** Compilations, opinions, or summaries that are far removed from the original data.

**Examples:**
- Blog posts commenting on news coverage
- Social media posts about an event
- Listicles ("Top 10 Measles Outbreaks of the Decade")
- Forum discussions

**When to use them:** Tertiary sources are useful for discovery -- they might point you toward something worth investigating. But they're not reliable enough to base your data on. If a blog post mentions an outbreak you haven't documented, use that as a lead to find the primary source. Don't put the blog post's claims into your dataset as fact.

### A practical rule

When you find information from a secondary or tertiary source, ask: "Can I find the original?" If a news article says "according to the state health department, there were 85 confirmed cases," go find the health department's report. Use that as your source, not the news article. If you can only find the secondary source, note that limitation in your record's research_notes.

---

## How Claude Searches

Claude has two ways to search for information, and it helps to understand the difference.

### Built-in web search

Every Claude Code session can search the web. This is always available and doesn't cost extra beyond your Claude subscription. Claude uses this for general queries, fact-checking, and finding specific pages.

This is what Claude uses by default when you run `/search`. It's good for most research tasks.

### MCP tools (optional power-ups)

**MCP** stands for Model Context Protocol. These are add-on tools that give Claude specialized search abilities. For example:

- **Perplexity** gives Claude access to a powerful research engine that synthesizes information from many sources at once (costs a small amount per query)
- **PubMed MCP** lets Claude search the medical literature database directly
- **Brave Search** provides an alternative search engine

You don't need MCP tools to use this framework. Claude's built-in search handles most research tasks just fine. MCP tools are upgrades you can add later when you want more powerful or specialized search. If you're curious, `docs/10-mcp-tools.md` covers MCP tools in detail.

When MCP tools are installed, Claude automatically chooses the right tool for each search based on the rules in your CLAUDE.md. You don't have to tell it which tool to use.

---

## Good Search Habits

### 1. Check your dataset first

Before searching the web, see what you already have. You might already have three records from Ohio that would help you understand the landscape before you search for more. Claude does this automatically in `/search`, but it's a good habit to develop yourself.

### 2. Start broad, then narrow

Your first search should cast a wide net. If you're looking for measles outbreaks in Ohio, start with "measles outbreaks Ohio" rather than "measles genotype D8 outbreak Columbus Ohio Franklin County 2024." The broad search shows you the landscape. Then you narrow in on specific gaps.

### 3. Try different phrasings

If "measles outbreak school Ohio" returns nothing useful, try:
- "measles cases school district Ohio"
- "measles exposure notification Ohio"
- "measles vaccination exemption outbreak Ohio"
- "rubeola cases Ohio" (the medical term for measles)

Different sources use different language. Government reports use clinical terminology. News articles use plain language. Legal documents use formal language. Casting a wider vocabulary net catches more.

### 4. Search by what you DON'T have

Look at your dataset and ask: "Where are the gaps?" If you have outbreaks from New York and California but nothing from Texas, search for Texas specifically. If you have data from 2019-2024 but nothing from 2015-2018, search that time range. Gap-filling is often more productive than general searching.

### 5. Document your searches

When Claude runs `/search`, it records what was searched and what was found in each record's research_notes. This prevents you from running the same search twice and wasting time. If you search manually outside of Claude, note what you searched for in the relevant record's research_notes.

---

## When Sources Disagree

This will happen. The CDC report says 85 cases. The state health department says 92. The newspaper says "nearly 100." What do you do?

**Document both. Don't silently pick one.**

In your record:
- Use the most authoritative source for the primary field value (in this case, the state health department's number, since they have the local data)
- Note the discrepancy in research_notes: "CDC MMWR reports 85 confirmed cases. Ohio DH reports 92. Difference may reflect later case confirmation. Newspaper rounded to 'nearly 100.'"
- List all sources in the sources list

The discrepancy itself is valuable information. It might reflect different reporting dates, different case definitions, or a genuine data quality issue. Recording it helps future you (or anyone reviewing your dataset) understand the uncertainty.

**Never change a field value to match a new source without noting the old value.** If the CDC originally said 85 and you're updating to the state's 92, your research_notes should say: "Updated confirmed_cases from 85 (CDC MMWR) to 92 (Ohio DH 2024 annual report, published later with updated count)."

---

## Example Workflow: Finding Measles Outbreaks in Ohio

Here's what a real research session might look like, start to finish.

### 1. Start with /search

```
You: /search measles outbreaks in Ohio 2019-2025
```

Claude runs several searches and comes back with results:

```
Found 6 potentially relevant results:

1. CDC MMWR: Measles Outbreak -- Columbus, Ohio, 2024
   Source: Primary (government)
   Already in dataset: No

2. Ohio DH: 2024 Annual Communicable Disease Report
   Source: Primary (government)
   Already in dataset: No

3. Columbus Dispatch: 85 measles cases in Franklin County
   Source: Secondary (news)
   Already in dataset: No

4. NEJM case report: Measles in an under-vaccinated community
   Source: Primary (academic)
   Already in dataset: No

5. Blog: "Anti-vax consequences in Ohio"
   Source: Tertiary (blog)
   Recommendation: Skip -- no original data

6. Ohio DH: 2019 Measles Summary
   Source: Primary (government)
   Already in dataset: No
```

### 2. Evaluate and prioritize

You scan the list. Results 1 and 2 are primary government sources -- best to start there. Result 4 is a journal article that might have detailed clinical data. Result 3 is a good secondary source for local context. Result 5 is a blog -- skip it. Result 6 is an older report that might fill a time gap in your dataset.

### 3. Collect the first record

```
You: Let's add #1, the Columbus 2024 outbreak.
Claude: I'll run /collect for that. Based on the CDC report, here's what I know...
        [Claude asks a few questions about details not in the search results]
You: [answer questions]
Claude: Created OB-2024-OH-001.md with verification level CONFIRMED (1 primary source).
```

### 4. Verify with additional sources

```
You: Can you check #2 and #3 against this record?
Claude: I'll read the Ohio DH report and the Dispatch article...
        [Claude compares the sources]
        The Ohio DH report confirms the outbreak but lists 92 cases (vs CDC's 85).
        The Dispatch article adds timeline details. Updated the record:
        - Added 2 sources
        - Updated confirmed_cases to 92 (Ohio DH, more recent)
        - Noted discrepancy in research_notes
        - Upgraded verification_level to VERIFIED (3 independent sources)
```

### 5. Move to the next finding

```
You: Now let's look at #6, the 2019 report.
Claude: The 2019 Ohio DH summary mentions a smaller outbreak in Dayton, 12 cases.
        Want me to create a record for that?
You: Yes.
Claude: Created OB-2019-OH-001.md...
```

### 6. Export when you're done

```
You: /export
Claude: Exported 2 records to dataset/exports/dataset.csv.
        Verification breakdown: 1 VERIFIED, 1 CONFIRMED.
```

That's one session. You added two records, verified one with multiple sources, and produced an updated spreadsheet. Over days and weeks, sessions like this build a comprehensive, well-sourced dataset.

---

## Quick Reference

| Task | Skill | What to type |
|------|-------|-------------|
| Find new data | `/search` | `/search measles outbreaks Ohio 2020-2025` |
| Add a record | `/collect` | `/collect 85-case measles outbreak, Columbus OH, Feb 2024` |
| Check a record | `/verify` | `/verify OB-2024-OH-001` |
| Update the spreadsheet | `/export` | `/export` |
| Save your progress | `/save` | `/save` |

---

*The best research dataset isn't the one with the most records. It's the one where every record has a source, every source has been evaluated, and every disagreement has been documented.*
