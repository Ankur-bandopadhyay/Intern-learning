# Case [5]: [Sentiment Analyser]

## The Prompt
**Final Prompt (v2):**
> [Act as a Sentiment Analyser and tell me the emotion,tone,target and summary in JSON format]

---

## Prompt Iteration: v1 vs v2

**Version 1 (Initial Draft):**
> [Act as a Sentiment Analyser and tell me what the message says]

**Version 2 (Refined Draft):**
> [Act as a Sentiment Analyser and tell me the emotion,tone,target and summary in JSON format]

**Why I made this change:**
[V1 provided a less accurate message feedback which lacked a lot of details such as the emotion,tone and the summary.V2 fixes it by specifically stating it to return the emotion,tone,target and the summary to get hold of what the user is trying to say ]

---

## Example Output

{
  "emotion": [
    "Frustration",
    "Annoyance",
    "Sarcasm",
    "Disappointment"
  ],

  "tone": "Highly sarcastic and critical",

  "target": "Software update and development team",

  "summary": "The speaker is expressing strong dissatisfaction with a software update that changed the user interface. The positive phrases are sarcastic and actually convey frustration, inconvenience, and criticism toward the development team."
}