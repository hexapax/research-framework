# Research Framework

An AI-assisted research framework for building structured, verifiable datasets from primary sources.

## What This Is

A file-based research system where:
- **Each record is a markdown file** with structured YAML data at the top and free-form notes below
- **Claude Code is your research assistant** -- it searches, collects, verifies, and exports data through guided workflows
- **Git tracks every change** -- your full research history is preserved automatically
- **Your files become spreadsheets** -- export to CSV or Excel at any time

No programming required. The system works through slash commands (`/collect`, `/verify`, `/search`, `/export`) that walk you through each step.

## Who This Is For

Researchers who want to:
- Build a structured dataset from scattered sources (news, government data, academic papers, public records)
- Independently verify claims across multiple sources
- Produce a citable, reproducible dataset with a clear audit trail
- Use AI to accelerate research without sacrificing rigor

The framework was developed from a real epidemiological research project studying [Electric Shock Drowning](https://github.com/hexapax/esd-research) -- 193 incidents documented across 14 systematic search strategies. This framework generalizes those patterns for any research domain.

## Quick Start

### Prerequisites

- [Claude Code Desktop](https://claude.ai/download) (Windows, Mac, or Linux)
- [GitHub Desktop](https://desktop.github.com/) (for version control without the terminal)
- [Python 3](https://www.python.org/downloads/) (for data export)

### Get Started

1. Clone this repository
2. Open `GETTING-STARTED.md`
3. Follow the tutorial (about 75 minutes for your first session)

The tutorial walks you through a **vacation planner** project -- you'll search for destinations, structure the results, verify claims across sources, and export an interactive comparison page. Same system, different data.

## What's Inside

```
research-framework/
  GETTING-STARTED.md         -- Start here
  
  template/                  -- Copy this to start your own project
    CLAUDE.md                -- Tells Claude how to help with your research
    dataset/                 -- Your structured records live here
      SCHEMA.md              -- Your data dictionary
    .claude/skills/          -- Guided research workflows
      collect/               -- /collect: Add a new record
      verify/                -- /verify: Check a record against sources
      search/                -- /search: Find information
      export/                -- /export: Generate CSV/Excel
      clean/                 -- /clean: Data quality check
      review/                -- /review: Interactive HTML review page
      save/                  -- /save: Commit your work
      next/                  -- /next: What to work on next
  
  tutorial/                  -- Vacation planner tutorial
    TUTORIAL-GUIDE.md        -- Step-by-step walkthrough
    DEST-001.md ... 005.md   -- Sample destinations with deliberate issues
    review.html              -- Interactive comparison page
  
  docs/                      -- Reference guides
    01-setup-windows.md      -- Installation
    ...
    12-creating-skills.md    -- Create your own workflows
  
  examples/                  -- Worked examples
    esd-research-patterns.md -- How the ESD project uses these patterns
    measles-quickstart.md    -- Domain-specific starter
```

## Available Commands

Once you've set up your project, these slash commands guide you through research workflows:

| Command | What it does |
|---------|-------------|
| `/collect` | Add a new record -- asks you questions, creates the file |
| `/verify` | Verify a record against independent sources |
| `/search` | Search for information using available tools |
| `/export` | Generate CSV/Excel exports from your dataset |
| `/clean` | Check data quality -- find missing fields, stale dates, inconsistencies |
| `/review` | Generate an interactive HTML page for browsing your data |
| `/save` | Commit your changes to git |
| `/next` | Get suggestions for what to work on |

## The Idea

Your research data lives in plain text files that you can read, edit, search, and version-control. Claude Code reads those files and understands your project through `CLAUDE.md` -- a set of instructions you write that tell Claude your research rules, source policies, and data schema.

When you type `/collect`, Claude doesn't just dump data into a file. It walks you through: What did you find? Where did you find it? Is this source independent from your subject of study? Does this duplicate an existing record? Then it creates a properly formatted file, sets the verification level, and reminds you to export.

Over time, you build a dataset that's structured enough for statistical analysis, documented enough for peer review, and versioned enough to show exactly how you got there.

## Growing With the System

The framework is designed as training wheels you can outgrow:

- **Week 1**: Use the built-in commands, follow the patterns
- **Month 1**: Customize your CLAUDE.md, adapt your schema, ask Claude to write scripts for you
- **Month 2**: Create your own slash commands for workflows you repeat
- **Month 3**: Add MCP tools for specialized search (academic databases, government records)

See `docs/12-creating-skills.md` for how to create your own commands.

## Documentation

| Guide | When to read |
|-------|-------------|
| `GETTING-STARTED.md` | Day 1 -- setup and first tutorial |
| `docs/03-how-records-work.md` | When starting your real project |
| `docs/05-verification.md` | When you have 10+ records |
| `docs/08-git-basics.md` | After your first session |
| `docs/10-mcp-tools.md` | When you want more powerful search |
| `docs/12-creating-skills.md` | When you're ready to create your own workflows |

## License

MIT. See [LICENSE](LICENSE).

## Origin

This framework was extracted from the [ESD Research Project](https://github.com/hexapax/esd-research), an epidemiological study of Electric Shock Drowning incidents in the United States. The research methodology, file structures, verification patterns, and export tools were generalized into this domain-agnostic framework.
