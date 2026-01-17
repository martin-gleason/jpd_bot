# JPD-Bot Stakeholder Requirements Document
**Juvenile Probation Department Policy Compliance Assistant**

**Version**: 1.0 Draft
**Created**: January 15, 2026
**Status**: Gathering Requirements

---

## Stakeholder Contacts

| Role | Name | Validation Status | Notes |
|------|------|-------------------|-------|
| Director, Court & Probation Services | [Name] | ✅ Validated | Executive sponsor |
| Supervisor(s) | [Names] | ✅ Validated | Compliance perspective |
| Field Officer(s) | [Names] | ✅ Validated | End user perspective |
| IT/Security | [TBD] | ⚠️ Not yet engaged | Critical for pilot |

---

## Questions to Answer

### Section 1: Policy Scope & Content

**1.1 Policy Inventory**
- [ ] How many policy documents exist in total?
  - 339
- [ ] What categories do they fall into? (treatment, supervision, legal, administrative, etc.)
  - Personnel
  - Probation
  - Specialized Support
  - Probation Officer Safety
  - Policy Manual Forms
  - Juvenile Probation Department(JPD) HR Policy
  - Office of the Chief Judge HR Policy
- [ ] Approximately how many pages per document?
  - 5
- [ ] What file formats are they in? (PDF, Word, internal wiki, etc.)
  - Word and PDF documents
  - Some are old PNG/Scan Documents

**1.2 Policy Access**
- [ ] Where are policies currently stored? (shared drive, intranet, physical binders?)
  - "S:\Juvenile_Probation\Policy Library>"
  - Global Share
- [ ] Who maintains/updates the policies?
  - Policy Department
    - Melissa Spooner
    - Terrif Griffin
- [ ] How frequently do policies change?
  - Regular reviews
  - only as mandated by the director 
- [ ] Is there a formal version control or change log for policies?
  - I do not believe so

**1.3 Policy Selection for MVP**
- [ ] Which 3-5 policies would be most valuable to include first?
  1. Dress Code
  2. AOIC Code of Conduct
  3. Professional code of conduct
  4. Ethics
  5. confidentiality
- [ ] Which policies cause the most compliance questions?
  - We'll have to review with Melissa, Terri, Dr. Lewis
- [ ] Are there any policies that should NOT be included? Why?

---

### Section 2: User Needs & Pain Points

**2.1 Current Workflow**
- [ ] When officers have a policy question, what do they currently do?
  - Ask their supervisor/DCPO
  - post on Teams
    - There is no search on teams.
  - Review Global Share
- [ ] How long does it typically take to find an answer?
  - 1 hour +
- [ ] What happens when they can't find the answer quickly?
  - They ignore it?
  - They say they didn't know
- [ ] Do officers ever make decisions without confirming policy? Why?
  - all the time, as the consequences are not usually dire.

**2.2 Common Questions**
- [ ] What are the top 5 most frequently asked policy questions?
  - Questions about confidentiality and records
  - Questions on time use
  - 
- [ ] What types of situations trigger policy lookups? (court dates, intake, violations, etc.)
- [ ] Are there specific policies that are more confusing than others?

**2.3 User Environment**
- [ ] Where will officers use this tool? (office, field, court?)
  - Community (we do not use the world "field")
  - Office
  - Court
- [ ] What devices do they have access to? (desktop, laptop, mobile?)
  - Laptop
  - Mobile
- [ ] Is internet access reliable in all locations?
  - yes
- [ ] Are there any accessibility requirements?
  - We need to follow all recommend and best practices accessiblity info

---

### Section 3: Compliance & Security

**3.1 Data Classification**
- [x] Confirmed: Policy documents contain NO sensitive case information
- [x] Confirmed: No PII will be ingested
- [ ] Are there any policies that are internal-only / confidential?
  - No
- [ ] Is there any policy content that shouldn't be searchable?
  - No

**3.2 IT & Security Review**
- [ ] Who needs to approve new software/tools?
- [ ] What is the typical approval timeline?
- [ ] Are there existing security frameworks we must comply with? (CJIS, etc.)
- [ ] Where would this tool be hosted? (cloud vs. on-premises?)

**3.3 Audit & Logging**
- [ ] Do we need to log who searches what?
- [ ] Are there retention requirements for search logs?
- [ ] Who would have access to usage data?

---

### Section 4: Success Metrics

**4.1 Defining Success**
- [ ] How would you know this tool is working?
- [ ] What would "successful adoption" look like?
- [ ] What metrics matter most? (time saved, accuracy, compliance rates?)

**4.2 Pilot Evaluation**
- [ ] How many officers should be in the pilot group?
- [ ] Who should be in the pilot? (by experience level, unit, etc.)
- [ ] How long should the pilot run?
- [ ] What feedback mechanism would work best?

**4.3 Baseline Data**
- [ ] Do we have current compliance audit data to compare against?
- [ ] Can we measure policy-related errors or inconsistencies currently?
- [ ] Is there time-tracking data for policy lookups?

---

### Section 5: Technical & Integration

**5.1 Existing Systems**
- [ ] What case management system is used?
  - cFive Supervisor
  - This tool will not be connected to c5
- [ ] Are there other digital tools officers use daily?
  - We are a Microsot Shop, so:
    - Teams
    - Outlook 365
- [ ] Would integration with existing systems be valuable? Which ones?
  - Connecting to Teams or authentication via teams would be nice; however, this may not be possible.
  - local hosting and discover would be nice until we get this integrated into the OCJs network

**5.2 Deployment Preferences**
- [ ] Desktop application, web app, or mobile?
  - Web app
- [ ] Should it work offline?
  - If it could that would be great, but with Claude is that possible?
- [ ] Any browser or OS restrictions?
  - No
  - I want this to work on mobile devices

**5.3 Policy Updates**
- [ ] Who would upload new/updated policies?
  - Policy team -- who have a variety of technological sophistication
  - The process has to be:
    - Upload to where the policy lives
    - Activate the bot to review new documents
- [ ] How quickly do policy changes need to be reflected?
  - after a policy has be updated, the union has 3 weeks to review and provide changes. Then management has another 3 weeks to respond.
- [ ] Should there be notifications when policies change?
  - When new policies are signed only.

---

### Section 6: Organizational Considerations

**6.1 Change Management**
- [ ] How have previous technology rollouts gone?
  - The case management system went well.
  - adding new functions to the system did not go well
    - Probation staff did not make referrals properly
    - Community staff did not add notes or accept referrals in a timely manner
    - Training was blamed for the issues; however, staff were trained multipletimes in multiple methods using the same materials. The issue is more likely a refusal to follow protocol
- [ ] What has made past tools successful or unsuccessful?
  - Follow through and QA by SPOs
  - Frequent refreshers
  - clear documentation
- [ ] Are there any concerns about AI/automation among staff?

**6.2 Training & Support**
- [ ] What training format works best? (in-person, video, documentation?)
- [ ] Who would provide ongoing support?
- [ ] Are there "champions" who could help with adoption?

**6.3 Timeline Expectations**
- [ ] Is there urgency around any particular deadline?
- [ ] Are there budget cycle considerations?
- [ ] Any upcoming audits or reviews that would benefit from this tool?

---

## Priority Questions for First Stakeholder Call

These are the most critical questions to answer before Phase 1 development:

### For Director
1. What is the approval pathway for piloting this tool?
2. Who from IT/Security should I engage with?
3. Are there budget implications for cloud services or staff time?
4. What would make this a "win" from your perspective?

### For Supervisors
1. Which 5 policies cause the most compliance issues?
2. What specific compliance challenges are you seeing?
3. How would you measure if this tool is helping?
4. Who are the most tech-savvy officers who might pilot this?

### For Field Officers
1. Walk me through: You're in the field and have a policy question. What do you do?
2. What's the most frustrating part of finding policy information?
3. What would make you actually USE a new tool vs. ignoring it?
4. Any specific questions you wish you could just "ask" someone?

---

## Technical Decisions Pending Stakeholder Input

| Decision | Options | Depends On |
|----------|---------|------------|
| Hosting Location | Cloud vs. On-premises | IT/Security approval |
| Access Method | Web app vs. Desktop | User environment |
| Offline Support | Yes vs. No | Field connectivity |
| Policy Update Workflow | Admin upload vs. Auto-sync | Who maintains policies |
| Audit Logging Depth | Basic vs. Detailed | Compliance requirements |

---

## Meeting Schedule

| Meeting | Stakeholder | Date | Status |
|---------|-------------|------|--------|
| Requirements Call 1 | Director | [TBD] | Not scheduled |
| Requirements Call 2 | Supervisors | [TBD] | Not scheduled |
| Requirements Call 3 | Field Officers | [TBD] | Not scheduled |
| IT Security Intro | IT Team | [TBD] | Not scheduled |
| Phase 0 Review | All stakeholders | [Target: Jan 24] | Pending |

---

## Action Items

| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| Schedule Director call | Marty | Jan 17, 2026 | Not started |
| Get sample policy PDFs | Marty | Jan 19, 2026 | Not started |
| Identify IT contact | Director | Jan 17, 2026 | Pending |
| List top 5 problem policies | Supervisors | Jan 20, 2026 | Pending |
| Test policy ingestion with samples | Marty | Jan 22, 2026 | Not started |

---

## Notes from Validation Conversations

### Director Conversation
*Date: [TBD]*
*Key takeaways:*
- 
- 
- 

### Supervisor Conversation
*Date: [TBD]*
*Key takeaways:*
- 
- 
- 

### Field Officer Conversation
*Date: [TBD]*
*Key takeaways:*
- 
- 
- 

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Jan 15, 2026 | Initial draft with question framework |

---

**Document Status**: Draft - Gathering Requirements
**Next Action**: Schedule stakeholder calls
**Phase 0 Target Completion**: January 24, 2026
