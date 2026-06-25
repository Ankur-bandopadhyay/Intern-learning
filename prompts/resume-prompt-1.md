# Case [1]: [Resume bullet generation from a plain-text job history]

## The Prompt
**Final Prompt (v2):**
> [Taking the reference of the resume 
    give it in a json output form which would be like 
    summary:[brief 2 to 3 line summary]
    key skills:[3 skills] 
    key achievements:[2 achievements] in brief]

---
## Prompt Iteration: v1 vs v2

**Version 1 (Initial Draft):**
> [taking the reference of the resume i atached do a bullet-generation from the job history mentioned in the resume]

**Version 2 (Refined Draft):**
> [Taking the reference of the resume 
    give it in a json output form which would be like 
    summary:[brief 2 to 3 line summary]
    key skills:[3 skills] 
    key achievements:[2 achievements] in brief]

**Why I made this change:**
["v1 was too broad and length for a hr to read so i managed length constraints in v2 and asked it to fetch only for the attributes required in brief in json format ]

---
## Example Output

{
  "summary": "Experienced Mathematics Teacher with expertise in curriculum design, instructional delivery, and student performance improvement across reputed international schools. Adept at creating engaging learning environments, integrating technology into teaching, and tailoring instruction to diverse learning needs.",

  "key_skills": [
    "Mathematics Instruction",
    "Differentiated Learning Strategies",
    "Academic Performance Analysis"
  ],

  "key_achievements": [
    "Successfully delivered mathematics education to diverse classrooms while maintaining high standards of student engagement and achievement.",
    "Implemented data-driven instructional interventions that helped identify and bridge student learning gaps, resulting in improved academic performance."
  ]
}