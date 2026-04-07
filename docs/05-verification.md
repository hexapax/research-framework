# Verifying Your Data

Collecting information is only half the job. The other half is making sure it's actually true.

This guide covers why verification matters, how to think about sources, and how to use the `/verify` skill to do the work systematically.


## Why Verification Matters

Here's a real story. The Electric Shock Drowning Prevention Association (ESDPA) maintains a list of 175 incidents where people were killed or injured by electrical current in water near docks and marinas. It's the most widely cited dataset on this topic. Researchers and legislators reference it.

When an independent research project verified every entry against primary sources -- news articles, obituaries, court records, government reports -- here's what they found:

- **39% of entries had zero independent sources.** They existed only on the ESDPA list. Nobody could confirm they actually happened as described.
- **80% of verified entries had the wrong date.** Some were off by days, others by nearly two years.
- **One "near miss" where everyone survived was actually a double fatality.** Two people died. The list said everyone lived.
- **One entry was a phantom duplicate.** It was the same incident copied with a different date, inflating the count.

This wasn't a bad list made by careless people. It was a well-intentioned effort maintained by a nonprofit. The errors accumulated over decades because nobody systematically checked each entry against original sources.

**That's what verification prevents.** Your dataset will have errors. Every dataset does. Verification is how you find them before someone else does.


## Source Independence: The Core Concept

**Independent** means the source got its information on its own, not by copying someone else.

A newspaper reporter who interviewed witnesses and wrote an article? That's an independent source. A blog post that summarized that newspaper article? Not independent -- it's just a copy. A government agency that conducted its own investigation? Independent. A website that scraped the government database? Not independent.

The test is simple: **if source B got its information from source A, then B is not an independent source. It's just a copy.**

Two independent sources agreeing on the same facts is meaningful. Ten copies of the same source agreeing on the same facts tells you nothing new -- you still have only one source.


## The Circular Sourcing Trap

This is the most dangerous data quality problem, and it's surprisingly easy to fall into.

Here's how it worked in the ESD research project:

1. The ESDPA published their incident list on their website.
2. The MikeHolt.com electrical forum reposted the list.
3. An electrical services company (OnTimeService.com) copied it too.
4. A researcher finds the "incident" mentioned on three different websites and thinks: "Three sources confirm this!"

But it's **zero independent sources**. All three trace back to the same original list. The information traveled in a circle: ESDPA created it, others copied it, and the copies look like confirmation but aren't.

**How to avoid this:** When you find a source, ask yourself: "Where did THIS source get its information?" If the answer is "from the same place as my other sources," it doesn't count.

Your project's CLAUDE.md file has a **Source Exclusion Rule** section where you list the sources that are the subject of your study -- the ones that can never count as independent verification. For the ESD project, that included ESDPA.org, MikeHolt.com, and OnTimeService.com. For your project, you'll define your own list.


## Verification Levels

Not every record needs the same level of proof. The framework uses five levels, from strongest to weakest:

**VERIFIED** -- Multiple independent sources confirm the key facts. This is the gold standard. A news article AND a court record AND an obituary all agree on who, what, when, and where. Use this when you have 2 or more independent sources that agree.

**CONFIRMED** -- One independent source confirms the record. A single news article describes the event. You have real evidence, but only from one place. If that one source got it wrong, you'd have no way to catch the error.

**PROBABLE** -- Strong circumstantial evidence, but no direct confirmation. The pieces fit together convincingly even though no single source tells the whole story. For example: an obituary mentions a drowning at a lake on a date that matches a dock inspection report showing electrical faults at the same marina.

**SUSPECTED** -- Some evidence points in this direction, but it's thin. The scenario is plausible but not well-supported. Maybe a forum post mentions a "shocking" incident at a marina, but there's no news coverage or official record.

**UNVERIFIED** -- The record exists in your dataset, but you haven't found any independent sources yet. This is the starting point for most records. It doesn't mean the record is wrong -- it means you haven't confirmed it yet.

**There is no shame in UNVERIFIED.** A well-labeled unverified record is more honest than a poorly-labeled "verified" one. The level tells future readers (and your future self) how much confidence to place in each record.


## Using /verify

The `/verify` skill walks you through checking a record against independent sources. Here's what happens when you run it:

1. **Pick a record.** You can specify one (e.g., `/verify REC-2024-003`) or let Claude show you the unverified records so you can choose.

2. **Review what's claimed.** Claude reads the record and identifies the key claims that need checking: dates, locations, names, counts, descriptions.

3. **Check source rules.** Claude reads your CLAUDE.md to understand which sources count as independent for your project.

4. **Search for sources.** Using web search (or MCP tools like Perplexity if you've set those up), Claude searches for independent confirmation. It tries multiple search strategies: names, dates, locations, related terms.

5. **Evaluate what's found.** For each potential source, Claude assesses: Is it independent? Does it confirm or contradict the record? How reliable is it?

6. **Update the record.** New sources get added to the sources list. The verification level gets updated if warranted. Any corrections or discrepancies get noted.

7. **Report back.** Claude tells you what it found, what changed, and what still needs your judgment.

If Claude searches and finds nothing, that's documented too. The search terms and tools used go into the record's `research_notes` field so you (or a future session) don't repeat the same dead-end searches.


## When Sources Disagree

Sometimes you'll find two independent sources that say different things. One newspaper says the incident was on July 4th; another says July 5th. One report says 12 cases; another says 15.

**Do not pick one and hide the other.** Document both. Note the discrepancy in your record's `research_notes` field. Use the value you think is most likely correct as the primary value, but explain why.

For example:

```
research_notes: |
  Date discrepancy: Local newspaper (July 4) vs. state health report (July 5).
  Using July 4 per the newspaper, which was published the day after the event.
  The state report was published 3 months later and may have used a different
  date reference (report date vs. onset date).
```

Disagreements between sources are actually valuable data. They tell you something about the reliability of each source and the complexity of the event.


## When to Stop Looking

Research can go on forever. At some point, you need to stop searching and move on.

**A reasonable stopping point:** If you've searched using 3 different approaches (different search terms, different tools, different source types) and found nothing, note your search attempts and move on.

For example, you might search for:
1. The person's name + location in web search
2. The event description + date in a news archive
3. The location + year in government records

If all three come up empty, record what you tried in `research_notes` and leave the verification level as UNVERIFIED. You can always come back later when new sources become available or new search tools are added.

Don't spend two hours verifying a single record when you have fifty more waiting.


## The Value of Negative Results

This is worth its own section because researchers often skip it.

**Recording that you searched and found nothing is still data.**

When you write in `research_notes`: "Searched for [name] in news archives, court records, and obituary databases on 2026-04-06. No results found." -- that tells future readers:

- The record hasn't been ignored; someone tried to verify it.
- These specific search strategies were already attempted (don't waste time repeating them).
- The absence of sources might itself be meaningful (maybe the event was too small or too old to have left digital traces).

In the ESD project, the pattern of which incidents couldn't be verified told a story: pre-2000 incidents were hardest to verify because local newspapers from the 1980s and 1990s aren't digitized. Near-miss incidents where everyone survived rarely generated any media coverage at all. These patterns helped the researchers understand the limits of their data -- which is just as important as the data itself.

**Write down what you didn't find.** Future you will thank present you.
