# Data Governance

<!--
This document establishes the rules for what data you collect, where it
comes from, how you handle privacy, and what ethical considerations apply.

Fill in each section with the specifics of your project. If a section
doesn't apply (e.g., your data doesn't include personal information),
say so explicitly -- it's better to document "not applicable" than to
leave it blank.

This file is modeled after the ESD drowning research project's data
governance document, which covers publicly available data about
identifiable individuals in an epidemiological context.
-->

This document describes the data sources, privacy considerations, and governance policies for this research project.

---

## Data Sources and Legal Basis

<!--
List every category of source you use. For each one, explain WHY you
have the right to use it. Common bases include:
- Published for public consumption (news, press releases)
- Public domain (US federal government works, 17 U.S.C. 105)
- Public records (court filings, government reports)
- Fair Use for research purposes
- Open data license (CC-BY, CC0, Open Data Commons)
- Terms of service allow research use

EXAMPLE (from the ESD project):
  The project uses published news articles, obituaries, court records,
  federal government data (OSHA, CDC, USCG -- public domain), state
  government records (public records laws), academic literature, and
  publicly posted video/community content.
-->

All data in this repository derives from **[publicly available sources / describe your access basis]**. [State whether any data was obtained from protected systems, and if so, under what agreement.]

### Source Categories

| Source Type | Examples | Legal Basis |
|-------------|----------|-------------|
| [e.g., Published news articles] | [e.g., Local newspapers, wire services] | [e.g., Published for public consumption; Fair Use for research] |
| [e.g., Government data] | [e.g., CDC reports, state health department data] | [e.g., Public domain / public records] |
| [e.g., Academic literature] | [e.g., Peer-reviewed journal articles] | [e.g., Published research; Fair Use for citation] |
| [e.g., Organization data] | [e.g., WHO situation reports] | [e.g., Published for public distribution] |
| [Add more rows as needed] | | |

### Third-Party Dataset Attributions

<!--
If you use datasets created by others (even if they're freely available),
credit them here. Include the license or terms that allow your use.
-->

| Dataset | Source | License/Terms | Location in Repo |
|---------|--------|---------------|------------------|
| [e.g., WHO Global Measles Data] | [World Health Organization] | [Open access] | [reference/who-data/] |
| [Add more rows as needed] | | | |

---

## Privacy Considerations

<!--
Does your dataset contain information about identifiable people? If so,
this section is critical. Even publicly available information deserves
careful handling when aggregated into a research database.

Key questions to answer:
- What personal information does your dataset contain?
- Are any subjects minors or vulnerable populations?
- Does any law (HIPAA, FERPA, GDPR, state laws) apply?
- What is the ethical basis for including personal information?

If your dataset contains no personal information (e.g., you're studying
weather patterns or chemical compounds), state that clearly and you can
keep this section brief.
-->

### Personally Identifiable Information in This Dataset

[Describe what personal information your dataset contains, if any. Examples: names, ages, locations, health status, demographic data. If none, state: "This dataset does not contain personally identifiable information."]

### Legal Framework

<!--
Check which regulations apply to your data. Common frameworks:
- HIPAA (US health data from covered entities)
- FERPA (US education records)
- GDPR (data about EU/EEA residents)
- Common Rule / 45 CFR 46 (US human subjects research)
- State-specific privacy laws
-->

- **[Regulation 1, e.g., HIPAA]:** [Does it apply? Why or why not?]
- **[Regulation 2, e.g., Common Rule]:** [Does it apply? Why or why not?]
- [Add more as relevant to your jurisdiction and data type]

### Ethical Considerations

<!--
Even when something is legally permissible, it may warrant ethical care.
Address these questions honestly:
- Could your dataset be used to harm the people in it?
- Does aggregation create risks that individual sources don't?
- Are there vulnerable populations represented?
-->

[Describe any ethical considerations specific to your project. For example:
- Are you aggregating publicly available information in a way that increases its accessibility?
- Does your dataset include information about vulnerable populations?
- Could your findings be misused? How do you mitigate this risk?]

---

## Researcher Responsibilities

Users of this dataset should:

- [e.g., Obtain appropriate institutional review (IRB determination) before using this data in formal research]
- [e.g., Consider whether individual-level identifiers are necessary for their analysis]
- [e.g., Follow their institution's data governance policies]
- [e.g., Cite this dataset and its sources appropriately in any publications]
- [e.g., Not attempt to contact individuals identified in the dataset without IRB approval]

---

## IRB Status

<!--
If you're affiliated with a university or research institution, you
likely need IRB review (even if it's just an exemption determination).
Document the status here.
-->

[e.g., "This project has not yet undergone formal IRB review." or "Exempt under 45 CFR 46.104(d)(4)" or "Not applicable -- this dataset contains no human subjects data."]

---

## Restricted Data Policy

<!--
If some data sources require special agreements (Data Use Agreements,
institutional access, FOIA requests), document them here even if you
haven't obtained the data yet. This helps future collaborators understand
what's in scope and what requires additional approvals.

If all your data is freely available, you can simplify this to:
"All data in this project is from publicly available sources. No
restricted-access data is used or planned."
-->

[Describe any restricted data sources you plan to use, or state that none are planned.]

| Data Source | Access Mechanism | Restrictions |
|-------------|-----------------|--------------|
| [e.g., NDI mortality data] | [e.g., IRB approval + NCHS application] | [e.g., DUA required; no redistribution] |
| [Add more rows as needed] | | |

[If restricted data will be obtained, describe where it will be stored and how access will be controlled.]

---

## Data Quality and Completeness

<!--
Be honest about what your dataset does and does not represent. Research
integrity depends on clearly stating limitations.
-->

This dataset is a research work product, not a [definitive registry / complete census / authoritative database]. Known limitations:

- [e.g., "The dataset covers [time period] and may miss [earlier/later] events"]
- [e.g., "Verification reflects source availability at time of research, not definitive determination"]
- [e.g., "Geographic coverage is uneven -- [regions] are better represented than [others]"]
- [e.g., "The true number of [events] is likely higher than documented here"]

---

## License

<!--
Choose a license for your research work product. Common options:
- CC0 1.0 Universal: Maximum reuse, no restrictions (recommended for data)
- CC-BY 4.0: Requires attribution
- MIT: For code/scripts specifically

The license applies to YOUR original work (analysis, code, schema),
not to the underlying facts or third-party sources.
-->

The research work product (analysis, code, schema, documentation) in this repository is released under **[CC0 1.0 Universal / CC-BY 4.0 / your choice]**. This license applies to the original analytical work, not to the underlying facts or third-party source materials, which retain their original terms.
