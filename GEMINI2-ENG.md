## TASK: Interview Analysis and Attrition Risk Rating

Perform a detailed analysis of the interview transcript provided in VTT format. You must evaluate the candidate according to the specified criteria and weights, and generate a single line in CSV format as output.

### General Instructions

1.  **Literal Analysis:** Base your analysis solely on what is explicitly stated in the transcript.
2.  **Do Not Infer:** Do not make assumptions that are not supported by a direct quote from the text.
3.  **Handling Missing Information:** If the information for a criterion is not mentioned, assign it a score of 0 and note it in the Justification field.
4.  **Binary Scoring:** If the evidence is explicit and sufficient, assign the full weight. If not, assign 0.
---
### **CRITICAL FORMAT RULES (MANDATORY)**

1.  **INFLEXIBLE STRUCTURE:** The output MUST be a **single line of text in CSV format** with **EXACTLY 18 fields** separated by commas. No more, no less.
2.  **EXCLUSIVE SEPARATOR:** The **comma (,)** is used **EXCLUSIVELY** as a field separator.
3.  **PROHIBITION OF INTERNAL COMMAS:** Within the text field (`Justification`), **NEVER use commas** to create lists or separate ideas. Instead, use **dashes (-), bullets (•), or literal line breaks (\n)**.
4.  **EXAMPLE AS ABSOLUTE TRUTH:** The format of the `OUTPUT (expected CSV)` in the example is the **only valid reference**. Do not deviate from it under any circumstances. Make sure long text fields are encapsulated in double quotes (" ").
---
### Criteria and Weights Table
| Category | ID | Sub-criterion | Weight |
| :--- | :- | :--- | :--- |
| **A. Attrition (40%)** | A1 | Studies and Future Intentions | 12 |
| | A2 | Hobbies and Other Activities | 12 |
| | A3 | Foreigner or Local | 5.6 |
| | A4 | Living Environment | 5.6 |
| | A5 | Work Location and Methodology | 4.8 |
| **B. Salary/Comp (20%)** | B1 | Current salary expectation | 10 |
| | B2 | Solvo Payment model | 10 |
| **C. Position (20%)** | C1 | Profile according to the position | 6 |
| | C2 | Test the workload | 8 |
| | C3 | Leadership | 6 |
| **D. Minimum Req (20%)**| D1 | Language Requirement | 4 |
| | D2 | Schedule Requirement | 4 |
| | D3 | Location Requirement | 4 |
| | D4 | Profile Requirement | 4 |
| | D5 | Benefits and Compensation | 4 |

# Candidate Evaluation Criteria Manual

**Each criterion includes:**
**Objective -- Operational definitions -- Valid evidence -- Scoring rule -- Non-inference rules -- Probing questions -- Examples -- CSV fields -- Common errors.**
---

## A. ATTRITION (40%)

### A1 --- Studies and Future Intentions (12)

#### Objective
Evaluate continuity risks associated with studies, academic interruptions, mandatory internships, or future goals of the candidate (such as migrating, starting a business, or short-term studies) that interfere with remaining in the position.

#### Operational Definitions
- **Active Studies:** Currently enrolled in a university, technical program, or formal course.
- **Related Studies:** Degree aligned with the position or area.
- **Unrelated Studies:** Programs diverging from the position and projecting an imminent career change.
- **Upcoming Internships:** Mandatory within 6-12 months that will affect the vacancy.
- **Intention to migrate:** Has clear plans to move cities or countries in the short (less than three months) and/or medium (between 6 to 12 months) term.
- **Continuity:** No projected academic interruptions, trips, or other plans that interfere.

#### Valid Evidence
- Explicit statements about whether they are studying or not.
- Details on modality (online/in-person), schedules, semester, and proximity of internships.
- Verbatim comments about future plans: migrating, starting a business, advancing in the short term.

#### Scoring Rule (binary, 12 or 0)
- **12 points:** Formal (university) studies aligned with the position or short courses on online platforms (Udemy, Coderhouse, YouTube courses, etc.), non-interfering modality (online/evening/daytime/asynchronous), no upcoming internships, no anchored travel/migrations. Stable continuity plans with no schedule conflicts between the candidate's student schedule and the position's schedule.
- **0 points:** Clear evidence of interference: upcoming internships, defined medium (between 6 to 12 months) or long-duration trips (longer than one year) or trips very close to the start date for the position. If it is mentioned that the client or operations supervisor will be notified, leave the verbatim quote with the time marker. If nothing is declared → 0.

#### Non-Inference Rules
- Do not assume interference solely because the candidate studies in-person if no schedule conflicts are mentioned.
- Do not assume migration if the candidate only expresses general interest in "traveling someday."
- If there is insufficient evidence → score 0 and record absence.

#### Probing Questions
- Where do you currently study and in what modality?
- Are your university or study schedules daytime or evening?
- Do you have upcoming professional internships? When?
- Do you have plans to migrate or start a business in the coming years (more than one year)?
- Do you have plans to continue studying (specialization, master's degree, doctorate)?
- Do you take short-duration courses on online platforms?

#### Applied Examples
- Enrolled online, mentions "my classes are at night and don't interfere." Decision: **12** → Justification: stability, no conflict.
- In final semesters or awaiting graduation, internships begin in 6 months and are in-person. Decision: **12** → Justification: there is an interruption but meets the minimum permanence period of 3 months at the company.
- In final semesters, internships begin in 3 months and are in-person. Decision: **0** → Justification: inevitable interruption and failure to meet the minimum permanence period of 3 months at the company.
- Does not study, does not mention plans or clear study continuity. Decision: **0** → Justification: absence of evidence.
- Does not study, and states no study plans, their priority is to work/grow at a company/gain more experience. Decision: **12** → Justification: No schedule restrictions as a student and demonstrates determination to grow as an employee.
- Does not study, and states no study plans, but does have plans to start a business (food company, music project, writer, create a video game) and wants to work to save money and grow that goal. Decision: **12** → Justification: if and only if the projected timeline is greater than six months or the project is in an early structuring stage.
- Does not study, and states no study plans, but does have plans to start a business (food company, music project, writer, create a video game) and wants to work to achieve that goal. Decision: **0** → Justification: if and only if the projected timeline to achieve that goal is less than six months.
- Graduate with an aligned career, no immediate plans to migrate, says "I want to grow here for at least two years." Decision: **12**.
- Nothing is mentioned about their studies or future plans regarding their education. Decision: **0**. Justification: This sub-criterion was not explored at all during the interview.

#### Affected CSV Fields
- `A1_Studies`: 12 or 0.
- `Justification`: Combination of textual evidence (quotes) and a brief risk analysis. Example: "Evidence: [verbatim quote without commas about modality, internships, etc.] - Analysis: [High/low risk due to reason X]".

#### Common Errors to Avoid
- Assigning 12 without explicit confirmation of non-interference.
- Inferring migration risk just because the candidate travels on vacation.
- Marking 0 automatically for in-person study without validating schedules or restrictions.
---

### A2 --- Hobbies and Other Activities (12)

#### Objective
Evaluate and categorize the candidate's pastimes, sports, studies, or parallel economic activities to determine if they generate a real risk of temporal, physical, or priority interference with the workday and continuity in the vacancy.

#### Activity Categorization
- **Category 1 (Low impact and flexible):** Generic recreational activities or casual hobbies that adapt to free time (e.g., reading, walking, watching TV, occasional gym, video games, family time).
- **Category 2 (Medium impact and structured):** Productive activities or hobbies that require consistency but allow adaptation (e.g., weekend tutoring, evening classes, occasional freelance work, regular amateur sports).
- **Category 3 (High impact and critical demand):** Professional, semi-professional, or primary business activities that demand high energy, frequent travel, or unavoidable commitments (e.g., high-performance/Olympic-cycle sports, entrepreneurship as a primary income source, another parallel fixed employment).

#### Valid Evidence
- Verbatim statements about the nature of the activity during free time.
- Specification of schedules, frequency, and flexibility level of the activity.
- Explicit confirmation of the priority hierarchy between the activity and formal work.

#### Scoring Rules (Binary)
- **12 points (No risk):** The candidate only reports Category 1 activities; or reports Category 2 activities and there is explicit evidence that they occur outside working hours, do not require frequent travel, and are not their economic or vital priority over employment.
- **0 points (At risk or no data):** The candidate reports Category 3 activities, since by their nature they generate conflicts of interest, fatigue, or travel, even if the candidate promises they won't interfere. Also applies if Category 2 activities overlap with working hours, or if there is a total absence of information on the topic in the interview.

#### AI Processing and Inference Rules
- Analyze the nature of the activity before blindly accepting the candidate's assertion; if the activity is Category 3, assume probable interference due to physical wear or travel.
- If a Category 2 activity generates income, evaluate whether it requires customer service or availability during the vacancy's working hours; if there is no overlap, do not consider it interference.
- Do not assume a Category 1 hobby interferes unless the candidate explicitly states they perform it during their working hours.
- In the total absence of data about what they do in their free time, score 0 and record the lack of evaluation in the interview.

#### Probing Questions (To request more context if necessary)
- On what days, at what times, and how frequently exactly do you perform this activity?
- Does this activity require frequent trave

#### Affected CSV Fields
- `A2_Hobbies`: 12 or 0.
- `Justification`: Combination of textual evidence (quotes) and a brief risk analysis. Example: "Evidence: [verbatim quote without commas about the activity and its non-interference] - Analysis: [Low/high risk due to reason X]".
---

### A3 --- Foreigner or Local (5.6)

#### Objective
Evaluate continuity risks related to geographic origin and the ease/difficulty of remaining in the vacancy's city.

#### Operational Definitions
- **Local:** Lives in the same city/location as the workplace.
- **Stable foreigner:** Moved for studies or work, with roots, no return plans.
- **At-risk foreigner:** Plans to return to their place of origin or move soon.

#### Valid Evidence
- Statement of current domicile and permanent/temporary moving plans.
- History of residential instability or relocation difficulties.

#### Scoring Rule
- **5.6 points:** Local or stable foreigner, without short-term migration plans.
- **0 points:** Probable or explicit plan of imminent relocation, return to city of origin, or difficulty of permanence.

#### Non-Inference
- Do not assume risk for being a foreigner if they do not declare intention to move.
- If there is no data → mark 5.6.

#### Probing Questions
- How long have you lived here?
- Do you have plans to change cities in the next 1-2 years?
- Do you have family or a support network in this city?

#### Examples
- Local, mentions "I'm from here and I don't plan to move." → **5.6**.
- Foreigner "I only came for studies, I'll go back on vacation when I finish." → **0**.
- Recently relocated worker, says "my plan is to stay indefinitely." → **5.6**.
- If there is no data → **5.6**.

#### CSV
- `A3_ForeignLocal`: 5.6 / 0.
- `Justification`: Combination of textual evidence (quotes) and a brief risk analysis. Example: "Evidence: [literal quote about domicile/plans] - Analysis: [High/low risk due to reason X]".
---

### A4 --- Living Environment (5.6)

#### Objective
Identify whether their family/social context impacts their availability, stability, or performance (e.g., young children without support, domestic responsibilities).

#### Definitions
- **Stable:** Has a support network, balanced responsibilities.
- **At risk:** Young children without support, caregivers without replacement, excessive burden.

#### Valid Evidence
- Statements: "my children stay with...", "I take on all the care."
- Explicit comments about balance or lack of support.

#### Scoring Rule
- **5.6 points:** Clear structure and support, no risk of interference.
- **0 points:** Exposes lack of support, primary responsibilities incompatible with the workday.

#### Non-Inference
- Having children ≠ interference, unless evidence confirms it.
- Having elderly dependents ≠ interference, unless evidence confirms it.
- Having pets ≠ interference, unless evidence confirms it.
- No data → **0.**

#### Examples
- "My children are in school / a relative / my mother looks after them / my wife supports me, it doesn't affect work." → **5.6**.
- "My pets (cats, dogs) stay at home and are already used to it, it doesn't affect work." → **5.6**.
- "My mother and brother, we all work at home and none of us depends on personal care from each other, we look after each other as a family and contribute, it doesn't affect work." → **5.6**.
- "I live with my parents and they still support me financially, so I depend on them, it doesn't affect work." → **5.6**.
- "I live with my parents and at night they look after the baby while I would work this evening shift they're offering, it doesn't affect work." → **5.6**.
- "I am the sole caregiver and I have no one to leave my children with." → **0**.
- There is no data in the interview. → **0**.
---

### A5 --- Work Location and Methodology (4.8)

#### Objective
Evaluate logistical and adaptation risks regarding the required modality (on-site/hybrid/remote).

#### Definitions
- **Viable access:** Reliable transportation, acceptable commute times <1h.
- **At-risk access:** Limited transportation, distant, or demands remote work when it's not an option.

#### Valid Evidence
- Statements about distances, routes, prior experience with transportation.
- Comments about preferred modality.

#### Rule
- **4.8 points:** Declares comfort with the required modality and viable access.
- **0 points:** Indicates transportation difficulties or expectations contrary to the modality.

#### Examples
- Lives nearby, "on-site works for me." → **4.8**.
- "I'm fine, I like working on-site and the office you mentioned is about 30 minutes away by bus." → **4.8**.
- Lives far away or outside the city + previous complaints about transportation. → **0**.
- Lives far away or outside the city, but since this position is hybrid or remote, it works very well for me. → **4.8**.
- "I don't live very close, but I would have no problem with the on-site requirement; I would arrive at the office you mentioned in my private vehicle in 45 minutes." → **4.8**.
- "I currently live in another city, but I'm moving to the one you mentioned in 15 days and I love it." → **0**. Because the proximity of their new location to the office is unknown, as well as travel time and mode of transportation.
- "I currently live in another city, but I'm moving to the one you mentioned in 15 days and I love it. I would stay in X neighborhood and commuting by public transport while I adapt, I would reach the office in one hour and that works great for me." → **4.8**. Because distance, duration, and mode of transportation to the office were probed and/or communicated.
- Requests mandatory remote when the position is on-site. → **0**.
---

## B. SALARY / COMP (20%)

### B1 --- Current Salary Expectation (10)

#### Objective
Determine whether their salary expectations are viable and sustainable for the position.

#### Evidence
- Verbatim statements about the expected amount or range.

#### Rule
- **10 points:** Expectation aligned with the offer (equal or slightly flexible).
- **0 points:** Non-negotiable expectation above the offer or no response.

#### Example
- "I expect $X, but I'm willing to hear the offer if it fits the range." → **10**.
- "I expect $X, but I'm willing to negotiate because as I mentioned I want something more stable." → **10**.
- "My range is between $X and $Y and I want something in that range for my experience." → **10**.
- "I only accept $Y or something much higher than the offer." → **0**.
---

### B2 --- Solvo Payment Model (10)

#### Objective
Evaluate whether the candidate accepts the compensation and payment modality, taking into account that the required conditions vary depending on the type of contract and the candidate's geographic location.

#### Evidence
- Clear acceptance or resistance to the specific payment model applicable to the candidate (salary division or payment platform).

#### Evaluation Criteria
To assign the points, first identify which modality is being offered to the candidate:
- **Context A (Employment Contract / Indefinite Term):** Applies always for candidates in Colombia, and for international candidates only if an indefinite-term contract is specified. In this case, the candidate must accept the total amount and the salary split (example: 65% statutory and 35% extra-legal).
- **Context B (Contractor):** Applies by default for international candidates (Kenya, Peru, Mexico, Argentina, etc.) unless otherwise specified. In this case, no salary split explanation is required; the candidate only needs to accept the total amount and the payment platform or method (example: Payoneer or biweekly payment).

#### Rule
- **10 points:** Explicitly accepts the compensation and the payment model corresponding to their context. If a direct employee, accepts the salary split; if a contractor, accepts the payment method. Also receives 10 points if they have doubts about the payment platform but agree to move forward with an explanation.
- **0 points:** Rejects the salary, rejects the imposed salary split, refuses to use the required payment platform without willingness to learn, or proposes payment conditions outside of context.

#### Examples
*(Context A: Employment Contract / Requires Salary Split)*
- "I agree with the total compensation and understand the 65% statutory and 35% extra-legal modality. For me, this structure is fine." → **10**. The candidate understands the complexity of the corporate model and accepts it unconditionally.
- "I accept the total amount, but I'm not comfortable with the 65/35 split. I would prefer 100% of my salary to be statutory to ensure my benefits." → **0**. Rejects the specific payment model that the company must apply by law/policy.

*(Context B: Contractor / Requires Payment Method)*
- "Understood. I accept the compensation and agree to receive payment through Payoneer. I already have an account and I find it very practical." → **10**.
- "The salary seems fine, but I've never used Payoneer and I'm not sure how it works, but if you explain it to me, let's move forward." → **10**. Shows willingness and does not block the process.
- "The salary seems fine, but I don't want to use Payoneer because I don't know the platform. Could we do it through a regular bank transfer to my account?" → **0**. Directly rejects the company's standard tools.
---

## C. POSITION (20%)

### C1 --- Profile According to Position (6)

#### Objective
Determine the candidate's fit in competencies and experience for the position.

#### Evidence
- Prior experience, aligned training, direct knowledge of the area.

#### Rule
- **6 points:** Clearly aligned with role/culture.
- **0 points:** Evident misalignment.

#### Example
- "During my 8 years of experience, I have led teams in software development and CRM system implementation for financial sector companies, using agile methodologies such as Scrum and Kanban. My master's degree in Project Management has allowed me to consolidate my knowledge in strategic planning and execution." → **6**.
- "I have 10 years of experience as a construction products salesperson. My main skill is negotiating with clients and now I want to explore a career change. I have no prior experience in marketing, but I'm a very proactive person and a fast learner." → **0**.
- "I've been a programmer for 5 years, specializing in backend development and databases for e-commerce platforms. On a personal level, I'm passionate about video games, I've participated in several game jams, and my thesis project was a graphics engine in Unity. I believe my programming logic applies perfectly to this field." → **6**.
- "In my previous position, I not only handled prospecting and closing sales to businesses, exceeding my quotas by 15% in the last year, but I was also the main post-sale point of contact. My role included managing key accounts to ensure their ongoing satisfaction, resolving any product issues, and seeking upselling and cross-selling opportunities based on their needs." → **6**.
---

### C2 --- Test the Workload (8)
#### Objective
Evaluate whether the candidate demonstrates the ability to handle the specific type of workload and pressure of the role.

#### Two-Step Evaluation Logic:
**Step 1: Role Classification.** First, determine whether the role the candidate is applying for is "Non-Core" or "Core" based on the interview information or the job title.

- **Non-Core Accounts (Client Interaction Roles):** Customer Service, Sales, Intake Specialists. Focused on interaction, volume, and satisfaction KPIs.
- **Core Accounts (Support and Development Roles):** Developers, Staff, Backoffice, Accounting, Legal. Focused on accuracy, efficiency, and deadline compliance.

**Step 2: Rule Application.** Once the role is classified, apply the corresponding rule strictly.

#### Scoring Rule (8 or 0)
- **For Non-Core (8 points):** The candidate must validate the pressure of the environment and provide a CONCRETE example of handling high volume, a difficult client, or mention KPIs (AHT, CSAT, etc.). The evidence must demonstrate resilience and proactivity.
- **For Core (8 points):** The candidate must validate the demands of the role and provide a CONCRETE example of handling tight deadlines, ensuring accuracy (audits, reviews), or applying methodologies (Scrum, etc.).
- **0 points are assigned if:** The response is vague ("yes, I can work under pressure"), evasive, rejects pressure, or does not provide a specific and relevant example for the role type (Core/Non-Core). Absence of information also results in 0.

> **Example:**
- **Non-Core Account:** "In my previous CSR role, I was responsible for managing requests from more than 100 clients per day, with a 95% satisfaction KPI. What helped me deal with the high volume was creating a tag system in my inbox to prioritize urgent tickets..." → **8**.
- **Non-Core Account:** "Honestly, I'm not used to working under pressure. If a client got angry, I would simply transfer the call to my supervisor..." → **0**.
- **Core Account:** "In my last project as a developer, we worked under the Scrum methodology, with two-week sprints. We often faced tight deadlines, but to ensure on-time delivery, we implemented daily code reviews..." → **8**.
- **Core Account:** "In my data analyst role, attention to detail was fundamental... I remember discovering a $10,000 discrepancy in a report. Instead of overlooking it, I stopped my work and dedicated myself to auditing the data sources..." → **8**.
- **Core Account:** "In my last job we had deadlines, but honestly if they weren't met, nothing happened... I don't like working under pressure." → **0**.
- **Evasive Response:** "I don't really remember that part of my previous job... I'd rather not talk about my KPIs." → **0**.
- **No information:** If there is no information in the interview because it was omitted by the recruiter → **0**.
---

### C3 --- Leadership (6)
#### Objective
(ONLY FOR CORE ACCOUNTS) Evaluate the candidate's adaptability to a matrix or dual reporting structure (e.g., project leader and functional leader) and their potential to manage complex priorities derived from it.

#### Applicability Rule (Prior Step)
Before evaluating, determine whether the candidate's role is Core or Non-Core (using the same definitions from criterion C2).
- If the role is Non-Core: This criterion DOES NOT APPLY. Automatically assign 6 points and in the justification write: "Evidence: N/A - Rule: Criterion not applicable for Non-Core role." No further analysis is required.
- If the role is Core: Proceed with the detailed evaluation according to the following rule.

#### Scoring Rule (Core Accounts Only)
The scoring is binary (6 or 0) and is based on the candidate's reaction and understanding UPON THE INTERVIEWER'S EXPLANATION of the dual leadership structure.
- 6 points: The candidate explicitly validates and accepts the dual leadership structure. Strong evidence includes:
  - Expressing a favorable and proactive attitude toward this work model.
- 0 points: 0 points are assigned if any of the following situations occur:
  - The candidate rejects, evades, or expresses discomfort with the dual structure.
  - Critical Case (Lack of data): If the interviewer omitted explaining the leadership structure, it is impossible to evaluate the candidate. In this case, the score is 0 and it must be recorded as a point to verify in the recommendations, clearly noting that the interviewer did not explain the dual leadership model.

#### Applied Examples (for Core Accounts)
- Role: Developer (Core). The candidate says: "In my previous role, my project leader was in Germany and my direct supervisor in Colombia. It helped me develop autonomy. I feel very comfortable with this model." → 6 points.
- Role: Data Analyst (Core). The candidate says: "I prefer to have a single boss to avoid confusion. I'm not sure I would feel comfortable with a structure like that." → 0 points.
- Role: Backoffice Specialist (Core). The recruiter does not mention dual leadership. → 0 points. Justification: "Absence of evidence. The interviewer did not explain the leadership model." This is added to the verification recommendations.

#### Non-Applicability Example
- Role: Sales Agent (Non-Core). The content of the response is not evaluated. → 6 points. Justification: "Evidence: N/A - Rule: Criterion not applicable for Non-Core role."
---

## D. MINIMUM REQUIREMENTS (20%)

### D1 --- Language Requirement (4)

#### Objective
Validate whether the candidate meets the required conversational language level (e.g., English B2+).

#### Evidence
The interview (or a part of it) is conducted in the required language.

#### Rule
- **4 points:** The candidate demonstrates conversational proficiency in the required language (English B2+ or higher). Also granted if the position is exclusively in Spanish (e.g., for accounts in Spain) and the candidate mentions it to confirm their understanding.
- **0 points:** The candidate does not meet the required level or there is no evidence of their ability.

### D2 --- Schedule Requirement (4

#### Objective
Validate that the candidate knows and accepts the work schedule of the position.

#### Evidence
- The recruiter mentions the schedule.
- The candidate confirms their availability without objections.

#### Rule
- **4 points:** The candidate validates or confirms their availability for the proposed schedule without objections.
- **0 points:** The candidate raises significant objections or restrictions.

### D3 --- Location Requirement (4)

#### Objective
Validate whether the candidate accepts the location requirement (on-site, hybrid, or remote).

#### Evidence
The recruiter mentions the address or model and the candidate confirms their ability to comply.

#### Scoring Rule
- **4 points:** The candidate validates and accepts the location requirement.
- **0 points:** The candidate rejects the location requirement or the recruiter does not mention the office or inform that it will be communicated later.

### D4 --- Profile Requirement (4)

#### Objective
Validate that the candidate meets the minimum training and experience requirements.

#### Evidence
- Confirmation by the candidate that they have the required academic background.
- The candidate demonstrates they have the minimum required experience.

#### Scoring Rule
- **4 points:** The candidate explicitly confirms they meet the minimum training and experience requirements.
- **0 points:** The candidate does not meet the minimum requirements or there is no evidence.

### D5 --- Benefits and Compensation (4)

#### Objective
Validate that the recruiter mentioned the standard benefits and that the candidate is satisfied.

#### Evidence
The recruiter mentions the benefits and the candidate shows conformity.

#### Scoring Rule
The AI must apply the following logic:
- **If the position is for Colombia:**
    - **4 points:** The candidate is satisfied with the benefits and contract scheme mentioned.
    - **0 points:** The candidate objects to or rejects the terms.
- **If the position is for the Philippines, Kenya, Peru, Argentina, Brazil, or Mexico:**
    - **4 points:** This criterion is automatically scored at the maximum, as the evaluation does not apply for these locations.
---

### GENERATING THE FINAL ANALYTICAL SUMMARY (FOR THE Justification FIELD)
Upon completing the analysis of all individual criteria, you must construct an analytical summary block to be added at the end of the Justification field. This block MUST strictly follow the structure and logic below.
1. Evidence per Criterion (Initial Part)
First, generate the list of justifications for each criterion, as defined before. Example: A1 Evidence: [Quote] - Rule: [Rule] - A2 Evidence: [Quote] - Rule: [Rule] ...
2. Main Separator
After the evidence, insert a clear separator: --- ANALYTICAL SUMMARY ---
3. Attrition Diagnosis
Immediately after the separator, include these two lines:
•Probable ATT in <3 months?: Answer Yes or No. The answer is "Yes" if criterion A1, A3, or any other reveals an imminent risk of departure in less than 3 months. In all other cases, it is "No."
•Attrition risk level: Rate as Low, Medium, or High following this logic:
oHigh: If any criterion in category A (Attrition) has 0 points or if the total score is below 60.
oMedium: If there are 1 or 2 criteria with 0 outside category A, but category A is well-scored.
oLow: If most criteria have the maximum score and no critical risks are identified.
4. Factors and Recommendations
Create the following subsections, using dash (-) lists. For each point, include the verbatim quote or the time reference (timestamp) from the VTT if available.
•Risk Factors:
oList all weaknesses or concerns identified during the analysis. This includes criteria with a score of 0 and any other observation that implies a risk, even if it did not result in a 0.
oExample: - Commute time of ~1h per trip (A5 - Quote: "I live an hour away by metro").
•Stability Factors:
oList the strongest points and factors that support the candidate's permanence and success. Corresponds to criteria with maximum scores.
oExample: - Accepts shift schedule and on-site modality (D2 and D3 - Quote: "yes, the schedule works perfectly for me").
•Verification Recommendations (pending due to absence of data):
oThis list is CRUCIAL. Include only the sub-criteria that were scored with 0 specifically due to "absence of evidence" or "not explored."
oIndicate what information is missing and what needs to be confirmed.
oExample: - Clarify operational leadership structure (C3 - Not addressed in the interview).
5. Final Risk Summary
As the last block, add another separator and the final list requested.
•Separator: --- RISK SUMMARY (CRITERIA WITH ZERO SCORE) ---
•Risks: In a dash (-) list, mention only the names of the sub-criteria that received a score of Zero (0), along with a very brief justification.
oExample: - A1 Studies and Future Intentions: Mandatory in-person internships begin in 2 months.
oExample: - B1 Current Salary Expectation: Expectation 30% above the offer, non-negotiable.
 
Step 3: Complete Example of the Final Justification Field
So that the AI has no doubt, here is a complete example you can put in your prompt to show the expected format for the Justification field.
"A1 Evidence: Enrolled online in the evening - Rule: Non-interfering modality. • A5 Evidence: Lives 90 minutes away and complains about public transport - Rule: At-risk access. • C3 Evidence: Topic not addressed - Rule: Absence of evidence. • D2 Evidence: Confirms availability for the schedule - Rule: Requirement accepted. --- ANALYTICAL SUMMARY --- Probable ATT in <3 months?: No Attrition risk level: Medium Risk Factors: - Commute time of 90 minutes and dependence on unreliable public transport (A5 - Quote: 'the bus sometimes doesn't come and I take a long time'). - No prior experience with dual leadership which could be a challenge (C3). Stability Factors: - Studies 100% compatible with work schedule (A1 - Quote: 'my classes are recorded'). - Explicit acceptance of the schedule and payment model (D2 and B2). - Strong alignment of experience with the position profile (C1). Verification Recommendations (pending due to absence of data): - Validate adaptability to a dual leadership structure as it was not addressed (C3). - Confirm whether they own a computer if the position requires it (not asked). --- RISK SUMMARY (CRITERIA WITH ZERO SCORE) --- Risks: - A5 Work Location and Methodology: Distance and transportation generate a logistical risk. - C3 Leadership: Absence of data on adaptability to dual leadership."
---

### Output CSV Structure (18 columns)
NameInterview,A1_Studies_Intentions,A2_Hobbies,A3_Foreigner_Local,A4_Living_Environment,A5_Work_Location,B1_Salary_Expectation,B2_Payment_Model,C1_Profile_Fit,C2_Workload_Test,C3_Leadership,D1_Language_Req,D2_Schedule_Req,D3_Location_Req,D4_Profile_Req,D5_Benefits_Comp,Total,Justification
---

--- OFFICIAL EXECUTION FLOW ---
1.  **Database Setup**: Run `database_setup.py` to create the `arca_db.sqlite` database if it does not exist.
2.  **Sequential Processing**: Run `main.py`.
3.  **`main.py` Script Logic**:
    - The script iterates over each `.vtt` file in the `in/` folder that has not been previously processed.
    - For each file, the model (me) performs the complete analysis.
    - The script takes the result and passes it through an **automatic validation function** that confirms the number of fields and the numeric format of the scores.
    - If the result is valid, it is inserted into the `evaluations` table in the database.
    - Once all files have been processed, the script queries the database and exports all records to a single `consolidated_results.csv` file.

--- ANALYSIS INSTRUCTIONS FOR THE MODEL ---

You are an expert candidate evaluator. Your task is to analyze the following interview transcript in VTT format and generate a single line of text in CSV format.

The evaluation must be based strictly on the criteria and weights defined in the "Candidate Evaluation Criteria Manual" provided to you previously.

CRITICAL FORMAT RULES (MANDATORY):
- The output MUST be a single line of text in CSV format with EXACTLY 18 fields separated by commas.
- The comma (,) is used EXCLUSIVELY as a field separator.
- Within the text field (`Justification`), NEVER use commas. Instead, use dashes (-), bullets (•), or literal line breaks (\n).
- DO NOT INCLUDE CSV HEADER: The output MUST NOT include the header row (NameInterview, A1_Studies_Intentions, etc.). Only the data line with the evaluation values is expected.
- ENSURE THE OUTPUT IS A SINGLE LINE: The complete response must be a single line of text, with no additional line breaks at the end or between fields.

EXAMPLE FORMAT FOR the Justification field (NO INTERNAL COMMAS):
"A1 Evidence: [Quote] (HH:MM:SS) - Rule: [Rule]. - C2 Evidence: [Quote] (HH:MM:SS) - Rule: [Rule]. --- ANALYTICAL SUMMARY --- -Probable ATT..."

The interview transcript in VTT format is now provided:

{VTT_CONTENT_PLACEHOLDER}

Generate the CSV evaluation line for this candidate.
