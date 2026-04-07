# Publishing and Sharing Your Research

You've built a dataset. It's clean, verified, and organized. Now you want other people to be able to find it, use it, and cite it.

This guide walks you through the three main ways to publish research data, from quick sharing to permanent academic citation.

---

## When to Publish

Not every dataset needs to be published. But yours might be ready if:

- You have records with independent verification (not just a collection of unconfirmed leads)
- The data fills a gap -- there's no existing public dataset covering what you've documented
- You'd want someone else to cite your work rather than recreate it from scratch
- A professor, collaborator, or journal reviewer has asked for your data

Publishing doesn't mean your work is "done." Datasets get versioned. You can publish version 1.0 today and update it as your research continues.

---

## Before You Publish: The Checklist

Run through these steps before making your dataset public. Each one takes a few minutes and saves you from embarrassment later.

### 1. Run /clean one last time

Open Claude Code and run:

```
/clean
```

Fix every error. Review every warning. This is your last chance to catch a typo, a missing field, or an inconsistency before the world sees it.

### 2. Run /export to generate fresh outputs

```
/export
```

This regenerates your CSV and XLSX files from the current dataset files. The spreadsheet in `dataset/exports/` is what most people will download and use. Make sure it's current.

### 3. Review DATA-GOVERNANCE.md

Open `DATA-GOVERNANCE.md` and read it as if you were a stranger seeing your project for the first time:

- Are your source rules clearly explained?
- Is it obvious what data came from public records vs. other sources?
- Are there any ethical considerations you should document?

If your project doesn't have a DATA-GOVERNANCE.md yet, create one. It doesn't need to be long -- a half page covering where the data comes from and what privacy considerations apply is enough.

### 4. Privacy check

This is the most important step. Before publishing, ask yourself:

- **Are there names of living people?** If yes, is the data genuinely public-record (news articles, court documents, published government reports)? If the information came from private communications, social media posts that were later deleted, or conversations, remove it.
- **Are there names of minors?** This is common in epidemiology when working with public health records. It's standard practice when the data comes from public records, but be thoughtful. If the names aren't essential to the research value, consider replacing them with initials.
- **Could someone be harmed by this data being public?** If a record contains sensitive health information that isn't already public, think carefully.
- **Are there any source URLs that might break or lead to paywalled content?** Note these limitations.

When in doubt, err on the side of caution. You can always add data back later. You can't un-publish it.

### 5. Add a LICENSE file

If your project doesn't already have a LICENSE file in the root directory, add one. Two common choices for research:

**For the dataset itself (the CSV, XLSX, and record files):** Use **CC0** (Creative Commons Zero). This puts the data in the public domain. Anyone can use it for any purpose without asking permission. This is the standard for research data because you want people to use your work, and data facts aren't copyrightable anyway.

**For any code (export scripts, analysis scripts):** Use **MIT License**. This lets anyone use and modify your code with minimal restrictions.

You can have both in one project. Put the CC0 text in a `LICENSE-DATA` file and the MIT text in a `LICENSE-CODE` file, or use a single LICENSE file that explains which applies to what.

If you're not sure, use CC0 for everything. It's the most permissive and most common for open research data.

---

## Option 1: GitHub Releases

The simplest way to share. If your project is already on GitHub, this takes five minutes.

### What it does

A GitHub release is a tagged snapshot of your project with downloadable files attached. People can download your CSV/XLSX without cloning the entire repository.

### Step by step

1. **Make sure your latest work is pushed.** Open GitHub Desktop, commit any remaining changes with `/save`, then click "Push origin."

2. **Go to your repository on GitHub.com.** Click the "Releases" link on the right side of the page (or go to `https://github.com/your-username/your-repo/releases`).

3. **Click "Draft a new release."**

4. **Create a tag.** In the "Choose a tag" dropdown, type a version number like `v1.0.0` and click "Create new tag." Use semantic versioning:
   - `v1.0.0` for your first release
   - `v1.1.0` when you add new records
   - `v2.0.0` if you change the schema significantly

5. **Write a release title and description.** Example:
   ```
   Title: v1.0.0 -- Initial dataset release
   
   Description:
   Dataset of 85 measles outbreak records (2018-2025), covering 32 states.
   - 45 verified, 25 confirmed, 15 unverified
   - Includes CSV and XLSX exports
   - See SCHEMA.md for field definitions
   ```

6. **Attach your export files.** Drag your CSV and XLSX files from `dataset/exports/` into the "Attach binaries" area at the bottom of the release form.

7. **Click "Publish release."**

Now anyone can go to your releases page and download the spreadsheet files directly.

### Limitations

GitHub releases don't give you a DOI (a permanent academic citation identifier). For that, you need OSF or Zenodo.

---

## Option 2: OSF (Open Science Framework)

OSF is a free platform built specifically for sharing research. It's widely used in public health, epidemiology, and social sciences.

### What it is

OSF (osf.io) is run by the Center for Open Science. It gives you:

- A project page with a description, contributors, and tags
- File storage with version history
- A DOI (Digital Object Identifier) for citation
- The ability to link to your GitHub repository
- Wiki pages for documentation
- Preprint hosting if you write a paper about your findings

### Step by step

1. **Create an account** at [osf.io](https://osf.io). Use your institutional email if you have one -- it adds credibility.

2. **Create a new project.** Click "Create new project" from your dashboard. Give it a clear title that describes the dataset, not just the topic:
   - Good: "US Measles Outbreak Dataset, 2018-2025"
   - Too vague: "Measles Research"

3. **Write a description.** Explain what the dataset contains, how it was built, and what it's for. A few paragraphs is enough. Mention the methodology, the number of records, the verification approach.

4. **Upload your files.** On the project's Files page, upload:
   - The CSV and/or XLSX from `dataset/exports/`
   - Your SCHEMA.md (so users understand the fields)
   - Your DATA-GOVERNANCE.md
   - Optionally, the full repository as a zip file

5. **Link your GitHub repository.** In project settings, go to "Add-ons" and enable the GitHub add-on. Connect it to your repository. This lets people see the full project history and access the individual record files.

6. **Add tags.** Add relevant keywords: your disease, your methodology, your geographic scope. This helps other researchers find your project.

7. **Add contributors.** If you had collaborators or an advisor, add them with appropriate credit.

8. **Get your DOI.** Once you're satisfied with the project, go to Settings and click "Create DOI." This gives you a permanent identifier like `10.17605/OSF.IO/XXXXX` that will always point to your project.

9. **Make the project public.** By default, new projects are private. When you're ready, change the visibility to public. You can keep individual files private if needed (for example, keeping the full record files private while sharing the exports).

### Tips

- OSF keeps version history for uploaded files. If you update the CSV, upload the new version and OSF tracks both.
- You can create "Components" (sub-projects) to organize things -- one for the dataset, one for the methodology, one for analysis.
- OSF projects can be registered (frozen in time) to create a permanent, unchangeable snapshot. Do this when you submit to a journal.

---

## Option 3: Zenodo

Zenodo is a research data repository run by CERN. Its primary purpose is giving datasets permanent, citable DOIs.

### What it is

Zenodo is simpler than OSF -- it's focused on archiving and citation rather than project management. Every upload gets its own DOI. When you publish a new version, Zenodo gives it a new DOI but also maintains a "concept DOI" that always points to the latest version.

### Step by step

1. **Create an account** at [zenodo.org](https://zenodo.org). You can log in with your GitHub account, which also enables automatic integration.

2. **Connect your GitHub repository (recommended).** Go to your Zenodo settings and enable the GitHub integration. This lets Zenodo automatically archive each GitHub release you create.

3. **Create a release on GitHub** (see the GitHub Releases section above). If you've connected Zenodo to GitHub, Zenodo will automatically archive the release and assign it a DOI.

4. **Alternatively, upload manually.** Click "New Upload" on Zenodo, fill in the metadata (title, authors, description, license), upload your files, and publish.

5. **Fill in metadata carefully.** Zenodo's metadata fields map to academic citation standards:
   - **Title:** Same as your project name
   - **Authors:** You and any collaborators, with ORCID IDs if available
   - **Description:** What the dataset contains and how to use it
   - **License:** CC0 for data (select "Creative Commons Zero v1.0 Universal")
   - **Keywords:** Your disease, methodology, geography
   - **Related identifiers:** Link to your GitHub repo and OSF project if you have them

6. **Publish.** Once published, you'll get a DOI badge you can add to your GitHub README.

### Versioning on Zenodo

Each time you publish a new version, Zenodo assigns:
- A version-specific DOI (e.g., `10.5281/zenodo.1234567` for v1.0.0)
- A concept DOI (e.g., `10.5281/zenodo.1234566`) that always resolves to the latest version

Use the **concept DOI** in your README and citations. Use version-specific DOIs when someone needs to reference an exact snapshot of your data.

---

## Citing Your Own Dataset

Once you have a DOI, you can cite your dataset in papers, reports, and other publications. Here's the format:

```
Author(s). (Year). Title of Dataset (Version X.X.X) [Data set]. 
Repository Name. https://doi.org/XX.XXXXX/XXXXXXX
```

Example:

```
Chen, N. (2026). US Measles Outbreak Dataset, 2018-2025 (Version 1.0.0) 
[Data set]. Zenodo. https://doi.org/10.5281/zenodo.1234567
```

Add this citation to your project's README.md so others know how to reference your work.

If you published on both OSF and Zenodo, use the Zenodo DOI for citations -- it's the more permanent of the two and follows standard data citation practices.

---

## Summary: Which Platform When

| Situation | Use |
|-----------|-----|
| Quick sharing with a colleague | GitHub release with CSV attached |
| Academic project, need a citable DOI | OSF or Zenodo |
| Journal submission, need permanent archive | Zenodo (automatic DOI per version) |
| Collaborative project with ongoing updates | OSF linked to GitHub |
| All of the above | Use all three -- they complement each other |

The most common setup for a published research dataset: GitHub for the working project, Zenodo for the permanent archive and DOI, and a link between them so they stay in sync. Add OSF if your field expects it or if you want the project management features.

---

## Next Steps

- If you want to add more powerful search tools to your research workflow, see [Adding Search and Research Tools](10-mcp-tools.md).
- If you want Claude to build custom analysis or visualization for your dataset, see [Getting Claude to Build Things for You](11-asking-claude-to-code.md).
