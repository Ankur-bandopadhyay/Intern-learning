# Case [2]: [Docs Summarizer]

## The Prompt
**Final Prompt (v2):**
> [
  You are a precise technical summarizer.
  Read the document below and respond ONLY with valid JSON (no markdown fences, no extra text) in this exact      schema:

  {
    "title": "short inferred title of the document",
    "summary": "3-4 sentence summary of the key content",
    "key_points": ["point 1", "point 2", "point 3"],
    "word_count": <integer, original document word count>
  }]

---

## Prompt Iteration: v1 vs v2

**Version 1 (Initial Draft):**
> [Summarize the document]

**Version 2 (Refined Draft):**
> [
You are a precise technical summarizer.
Read the document below and respond ONLY with valid JSON (no markdown fences, no extra text) in this exact schema:

{
  "title": "short inferred title of the document",
  "summary": "3-4 sentence summary of the key content",
  "key_points": ["point 1", "point 2", "point 3"],
  "word_count": <integer, original document word count>
}]

**Why I made this change:**
[V1 provided a summary too long and tedious to read.V2 on the other hand provided a brief explanation of only the asked attributes which were {Summary},{Functionalities},{Deliverable} making it easier for the User to understand]

---

## Example Output

{
"title": "Data Migration Protocol v2",

"summary": "This document outlines the updated procedures for migrating legacy databases to the new cloud infrastructure. It details the pre-migration validation steps, the automated transfer process using the new MigrationCLI tool, and post-migration integrity checks. The update aims to reduce downtime by 40% and ensure zero data loss during transitions.",

"key_points": [
"Pre-migration validation requires running the schema-check script.",
"MigrationCLI is now the mandatory tool for all automated data transfers.",
"Post-migration integrity checks must be signed off by a senior DBA."
],

"word_count": 450

}