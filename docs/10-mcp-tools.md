# Adding Search and Research Tools

Claude can already search the web, read files, and write code. But you can give it access to specialized research tools -- medical databases, academic paper archives, deep search engines -- by adding plugins called MCP tools.

This guide explains what they are, how to add them, and how to keep things manageable.

---

## What MCP Tools Are

MCP stands for "Model Context Protocol." In plain language: MCP tools are plugins that give Claude access to external services -- search engines, databases, APIs.

Without MCP tools, Claude can:
- Search the web (built-in)
- Read and write files on your computer
- Run code

With MCP tools, Claude can also:
- Search PubMed for medical literature
- Run deep research queries through Perplexity
- Access the WHO disease database
- Search across 200 million academic papers
- Interact with your Open Science Framework project

Each MCP tool is a small server that runs on your computer and connects Claude to a specific service.

---

## The Layered Approach

You don't need to install everything at once. Think of tools in tiers:

### Tier 1: Free, Built-in (start here)

These work out of the box with Claude Code. No setup needed.

- **Claude's web search** -- good for quick fact-checks, finding news articles, getting current information
- **File tools** -- reading your dataset files, writing new records, running scripts

This is enough to do real research. Many projects never need more than this.

### Tier 2: Free MCP Tools (add when you want more depth)

These are free to install and use. They give Claude direct access to academic databases.

- **medical-mcp** -- searches PubMed and WHO databases. Essential for health research.
- **paperplain-mcp** -- searches across 200+ million academic papers from Semantic Scholar. Good for literature reviews.
- **OSF server** -- lets Claude interact with your Open Science Framework project directly.

### Tier 3: Paid Tools (add when you need serious search power)

These cost money per query but provide significantly deeper results.

- **Perplexity** -- AI-powered deep research. Costs roughly $0.003 to $0.10 per query depending on the mode. Excellent for complex searches that require synthesizing multiple sources. Budget roughly $5-50/month depending on how heavily you search.

### Tier 4: Specialized Tools (as they become available)

The MCP ecosystem is growing. New research-oriented tools appear regularly. Add them one at a time as you find specific needs they fill.

---

## How to Install an MCP Tool

MCP tools are configured in a file called `.mcp.json` in your project's root directory. This file tells Claude Code which tools are available and how to connect to them.

### The .mcp.json file

Here's what the file looks like:

```json
{
  "mcpServers": {
    "medical-mcp": {
      "command": "npx",
      "args": ["-y", "medical-mcp"]
    }
  }
}
```

That's it. Each tool gets a name and a command that tells Claude Code how to start it.

### Adding a tool step by step

1. **Open your project in Claude Code.**

2. **Open the `.mcp.json` file.** If it doesn't exist yet, Claude can create it for you. Just say: "Create a .mcp.json file with [tool name]."

3. **Add the tool's configuration.** Each MCP tool's documentation tells you what to put in the file. Here's an example with two tools:

```json
{
  "mcpServers": {
    "medical-mcp": {
      "command": "npx",
      "args": ["-y", "medical-mcp"]
    },
    "perplexity": {
      "command": "npx",
      "args": ["-y", "@anthropic/perplexity-mcp"],
      "env": {
        "PERPLEXITY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

4. **Restart Claude Code** (or start a new conversation) so it picks up the new tool.

5. **Test it.** Ask Claude to use the new tool: "Search PubMed for measles outbreak case studies in the US since 2020."

### The npm registry issue

Some MCP tools are installed through npm (Node Package Manager). If you have a work or corporate computer, your npm might be configured to use a company registry instead of the public one. If tool installation fails, the fix is simple.

Create a file called `.npmrc` in your project root with this content:

```
registry=https://registry.npmjs.org/
```

Or when running install commands, add the registry flag:

```
npx --registry https://registry.npmjs.org/ -y medical-mcp
```

This tells npm to use the public registry instead of your company's private one.

---

## Tool Count Management

This is important, so it gets its own section.

**More tools is not better.** Each tool you add is another thing Claude might reach for when you don't want it to. If you have 15 tools installed, Claude has to decide between 15 options every time it needs to search for something. It might use Perplexity (which costs money) when built-in search would have been fine. It might search PubMed when you wanted a news article.

**Start with 3-5 tools.** Add one at a time. Use it for a week. See if it helps. If it doesn't, remove it.

**Recommended starter setup for health/epidemiology research:**

1. Claude's built-in web search (already there)
2. Claude's file tools (already there)
3. Perplexity (deep research when built-in search isn't enough)
4. medical-mcp (PubMed access for academic literature)

That's four tools. It's enough for serious research. Add more only when you hit a wall that these four can't solve.

---

## Teaching Claude Which Tools to Use

Having the right tools installed is half the battle. The other half is telling Claude when to use each one. You do this by adding rules to your CLAUDE.md file.

Open `CLAUDE.md` and add a section like this:

```markdown
## Tool Usage Rules

- Use built-in web search for quick fact-checks and finding news articles
- Use Perplexity for broad research questions that need depth 
  ("find measles outbreaks in Ohio 2020-2025 with case counts")
- Use PubMed MCP for academic literature and clinical studies
- Do NOT use web search when the answer is in our own dataset files -- 
  check the dataset first
- Always check existing records before searching externally
```

Be specific. "Use Perplexity for broad searches" is okay. "Use Perplexity for research questions where I need synthesis across multiple sources, and use built-in search for single-fact lookups" is better.

Update these rules as you learn what works. If Claude keeps using the wrong tool, add a more specific rule.

---

## Cost Awareness

MCP tools that call paid APIs cost money per query. This is real money that adds up.

**Perplexity pricing (approximate):**
- Quick ask: ~$0.003 per query
- Deep research: ~$0.05-0.10 per query

If you run 50 deep research queries in a session, that's $2.50-5.00. Over a month of active research, expect $5-50 depending on how heavily you search.

**How to manage costs:**

- Use built-in search first. Only escalate to Perplexity when you need deeper results.
- Add a rule to CLAUDE.md: "Prefer built-in web search. Only use Perplexity when built-in search doesn't find what we need or when I specifically ask for deep research."
- Monitor your API usage through the provider's dashboard.
- Set spending limits if the provider supports them.

Free MCP tools (medical-mcp, paperplain-mcp) don't cost anything to query. They call free public APIs. Use them as much as you want.

---

## Troubleshooting

If a tool isn't working:

1. **Check server status.** In Claude Code, type `/mcp` to see which MCP servers are running and which have errors.

2. **Check your .mcp.json file.** A missing comma, bracket, or quote will break the entire file. Ask Claude to check it: "Is my .mcp.json file valid?"

3. **Check API keys.** Paid tools like Perplexity require an API key. Make sure it's correct and hasn't expired.

4. **Restart Claude Code.** MCP tools are loaded when Claude Code starts. If you just added or changed a tool, start a new conversation.

5. **Check your internet connection.** MCP tools need to reach external services. If you're offline or behind a restrictive firewall, they won't work.

6. **npm errors.** If a tool fails to install, try the registry fix described earlier. Also make sure Node.js is installed on your machine.

---

## Summary

| What | When | Cost |
|------|------|------|
| Built-in web search | Always available, use first | Free |
| medical-mcp (PubMed) | Academic literature in health sciences | Free |
| paperplain-mcp | Broad academic paper search | Free |
| Perplexity | Deep multi-source research | $0.003-0.10/query |

Start small. Add tools as you need them. Teach Claude when to use each one. Watch the costs.

---

## Next Steps

- If you want Claude to build custom scripts and visualizations for your data, see [Getting Claude to Build Things for You](11-asking-claude-to-code.md).
- If you find yourself repeating the same steps over and over, see [Creating Your Own Workflows](12-creating-skills.md).
