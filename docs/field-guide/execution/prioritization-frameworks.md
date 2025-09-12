# Prioritization Frameworks: Deciding What Matters Most

## The Scenario

A team is overwhelmed. They have a long backlog of new features, technical debt, bug fixes, and infrastructure improvements. Everyone has a different opinion on what's most important. The product manager wants new features to drive engagement. The support team wants critical bugs fixed. The engineers want to pay down technical debt. Without a structured way to prioritize, the team is stuck in a cycle of debate and context-switching, making little progress on any front.

As a Staff Engineer, you must help the team navigate these competing priorities. Prioritization frameworks are tools for making these trade-offs explicit and objective, aligning the team's effort with the most impactful work.

## Why Use a Framework?

-   **Strategic Alignment:** Ensures work directly supports business objectives.
-   **Objectivity:** Replaces gut feelings with a consistent, data-informed process.
-   **Transparency:** Creates a shared understanding of why certain work is being done over other work.

## Key Prioritization Frameworks

### 1. RICE Scoring

A quantitative method for scoring initiatives.

-   **Reach:** How many users will this impact in a given timeframe?
-   **Impact:** How much will this impact each user? (Use a scale: 3 for massive, 2 for high, 1 for medium, 0.5 for low).
-   **Confidence:** How confident are you in your estimates? (A percentage from 0-100%).
-   **Effort:** How much time will this take from the team (person-months)?

**Formula:** `(Reach * Impact * Confidence) / Effort`

The RICE score provides a single number to compare disparate ideas, from a new feature to a refactoring project.

### 2. MoSCoW Method

A qualitative method for categorizing work into four buckets:

-   **Must-Have:** Critical for the release. The product will fail without these.
-   **Should-Have:** Important but not critical. The product is still viable without them, but they add significant value.
-   **Could-Have:** Desirable but not necessary. Nice-to-haves that will be included if time permits.
-   **Won't-Have (this time):** Explicitly out of scope for the current release.

MoSCoW is excellent for communicating scope and managing stakeholder expectations for a specific release or timeframe.

### 3. Kano Model

This model categorizes features based on their effect on customer satisfaction.

-   **Basic Expectations:** Features that are expected and cause dissatisfaction if they are missing (e.g., a login button).
-   **Performance Features:** Features where more is better (e.g., faster page load times).
-   **Delighters:** Unexpected features that create delight and a competitive advantage.

## Cross-Reference Navigation

### Prerequisites for This Chapter
- **[Strategic Thinking](strategic-thinking.md)** - Strategic thinking provides foundation for effective prioritization decisions
- **[Decision-Making Frameworks](decision-making-frameworks.md)** - General decision-making skills support systematic prioritization

### Related Concepts
- **[Agile Essentials](agile-essentials.md)** - Agile practices require effective prioritization for backlog management and sprint planning
- **[Product-Engineering Collaboration](../business/product-engineering-collaboration.md)** - Cross-functional prioritization requires collaboration between product and engineering teams
- **[Engineering Metrics & Business Alignment](../business/engineering-metrics-business-alignment.md)** - Metrics help evaluate and measure the impact of prioritization decisions
- **[Strategic Thinking](strategic-thinking.md)** - Strategic context enables better prioritization of long-term versus short-term work

### Apply These Concepts
- **[Staff Engineer Competency Assessment](../../appendix/tools/staff-engineer-competency-assessment.md)** - Evaluate your execution and delivery leadership capabilities
- **[Team Health Diagnostic](../../appendix/tools/team-health-diagnostic.md)** - Assess team alignment and clarity on priorities and decision-making

### Next Steps in Your Learning Journey
1. **[Strategic Thinking](strategic-thinking.md)** - Learn to align prioritization with broader strategic objectives
2. **[Decision-Making Frameworks](decision-making-frameworks.md)** - Master systematic approaches to complex technical and business decisions
3. **[Product-Engineering Collaboration](../business/product-engineering-collaboration.md)** - Develop skills for collaborative prioritization with product teams

## A Practical Exercise: The Prioritization Challenge

-   **Objective:** To practice applying a prioritization framework to a real-world backlog.
-   **Setup:** Take a list of 5-10 real backlog items (features, bugs, tech debt). Divide the team into small groups.
-   **Execution:** Have each group use the RICE framework to score each item. They'll need to make assumptions and estimates for Reach, Impact, Confidence, and Effort.
-   **Debrief:** Compare the scores from each group. Discuss where the estimates differed and why. The goal isn't to get the "right" score but to have a structured conversation about value and effort.

## Further Reading

-   *Inspired: How to Create Tech Products Customers Love* by Marty Cagan
