# Team Topology Assessment Framework

> *"You can't improve what you don't measure, and you can't measure what you don't understand."*

Ever walked into an engineering organization and immediately sensed something was "off"? Maybe teams seemed frustrated, delivery was slower than it should be, or there was constant friction between groups? Often, the root cause isn't technical—it's organizational.

**This assessment framework helps you diagnose organizational health using Team Topologies principles.** Think of it as a health check for your engineering organization, designed to identify problems before they become crises and find opportunities for improvement.

Whether you're joining a new company, restructuring existing teams, or just trying to understand why things feel harder than they should be, these tools will give you the data you need to make informed decisions about team structure and evolution.

## Quick Team Type Assessment

Use this flowchart to identify the appropriate team type for a given team or proposed team:

```mermaid
flowchart TD
    A[New Team Need] --> B{Primary Purpose?}
    
    B -->|Deliver user value| C{End-to-end capability?}
    B -->|Enable other teams| D{Temporary engagement?}
    B -->|Serve internal teams| E{Developer tooling/infrastructure?}
    B -->|Complex specialized domain| F[Complicated Subsystem Team]
    
    C -->|Yes| G[Stream-Aligned Team]
    C -->|No - depends on others| H{Can dependencies be minimized?}
    H -->|Yes| G
    H -->|No| I[Consider splitting value stream]
    
    D -->|Yes| J[Enabling Team]
    D -->|No| K[Consider Platform Team or different structure]
    
    E -->|Yes| L[Platform Team]
    E -->|No| M[Reassess team purpose]
    
    style G fill:#e1f5fe
    style J fill:#e8f5e8
    style L fill:#f3e5f5
    style F fill:#fff3e0
```

## How Healthy Are Your Teams? A Comprehensive Assessment

**Before you start:** These assessments work best when completed by multiple people (team members, stakeholders, leadership) and compared. Different perspectives often reveal blind spots.

### Stream-Aligned Team Health Check

> **Quick gut check**: Is this team able to deliver value to users independently, or are they constantly waiting for other teams?

**Rate each dimension from 1 (Poor) to 5 (Excellent).** Be honest—this is about identifying opportunities for improvement, not scoring perfect 5s.

!!! abstract "Stream-Aligned Team Health Assessment"
    
    === "Value Stream Clarity (25%)"
        - [x] Clear understanding of users and needs
        - [x] Can articulate business value creation
        - [ ] Has direct access to user feedback
        - [ ] Measures success through outcomes
        
        **Score: 2/4** - Need better user feedback loops
    
    === "Technical Capability (30%)"
        - [x] Has all needed skills for value stream
        - [x] Can build, test, deploy, and operate
        - [ ] Can resolve production issues independently
        - [x] Technical decisions align with architecture
        
        **Score: 3/4** - Improve production issue resolution
    
    === "Autonomy & Flow (25%)"
        - [ ] Can deploy without coordinating with others
        - [ ] Minimal waiting for external dependencies
        - [x] Makes most technical decisions independently
        - [x] Work batch sizes appropriate
        
        **Score: 2/4** - Address deployment dependencies
    
    === "Cognitive Load (20%)"
        - [x] Workload appropriate for capacity
        - [x] Focus on core domain
        - [ ] Adequate time for learning
        - [x] Not overwhelmed by tool complexity
        
        **Score: 3/4** - Create more learning time
    
    **Overall Health: Strong (10/16)** - Focus on independence and feedback loops

!!! abstract "Platform Team Health Assessment"
    
    === "Customer Focus (30%)"
        - [x] Treats engineering teams as customers
        - [ ] Regularly collects feedback from stream teams
        - [x] Measures success by team adoption
        - [ ] Understands stream team pain points
        
        **Score: 2/4** - Improve feedback collection and pain point understanding
    
    === "Product Excellence (25%)"
        - [x] Provides self-service capabilities
        - [x] Has clear APIs and documentation
        - [ ] Maintains backwards compatibility
        - [x] Has appropriate reliability/performance
        
        **Score: 3/4** - Focus on backwards compatibility
    
    === "Developer Experience (25%)"
        - [x] Reduces cognitive load for stream teams
        - [ ] Accelerates stream team delivery
        - [x] Easy to onboard and use
        - [ ] Helpful error messages and debugging
        
        **Score: 2/4** - Improve delivery acceleration and debugging experience
    
    === "Strategic Alignment (20%)"
        - [x] Roadmap aligns with organizational strategy
        - [x] Balances standardization with flexibility
        - [x] Investment appropriate for scale
        - [ ] Enables rather than constrains innovation
        
        **Score: 3/4** - Ensure platform enables innovation
    
    **Overall Health: Good (10/16)** - Focus on feedback loops and developer experience

### Enabling Team Health Check

Rate each item from 1 (Poor) to 5 (Excellent):

#### Knowledge Transfer Excellence (Weight: 35%)
- [ ] Team has strong teaching and coaching skills (1-5)
- [ ] Team creates lasting capability in other teams (1-5)
- [ ] Team's engagements have clear success criteria (1-5)
- [ ] Team measures success by other teams' capability growth (1-5)

**Score: ___/20 → Weighted Score: ___/7**

#### Expertise Depth (Weight: 25%)
- [ ] Team has deep expertise in their specialized area (1-5)
- [ ] Team stays current with industry best practices (1-5)
- [ ] Team can solve complex problems others cannot (1-5)
- [ ] Team's expertise is recognized across the organization (1-5)

**Score: ___/20 → Weighted Score: ___/5**

#### Engagement Model (Weight: 25%)
- [ ] Team has clear engagement processes and boundaries (1-5)
- [ ] Team balances multiple concurrent engagements effectively (1-5)
- [ ] Team knows when to end engagements (1-5)
- [ ] Team avoids becoming a permanent dependency (1-5)

**Score: ___/20 → Weighted Score: ___/5**

#### Organizational Impact (Weight: 15%)
- [ ] Team addresses systemic rather than just local problems (1-5)
- [ ] Team's work has multiplier effects across the organization (1-5)
- [ ] Team identifies and fills capability gaps proactively (1-5)

**Score: ___/15 → Weighted Score: ___/3**

**Overall Enabling Team Health: ___/20**

## Team Interaction Assessment

### Current State Mapping

For each pair of teams that interact, identify the current interaction mode:

| Team A | Team B | Current Mode | Desired Mode | Health (1-5) | Actions Needed |
|--------|---------|--------------|--------------|--------------|----------------|
| | | Collaboration/X-as-a-Service/Facilitating | | | |
| | | | | | |
| | | | | | |

### Interaction Mode Health Indicators

#### Collaboration Mode Health
- [ ] High trust and psychological safety between teams
- [ ] Regular, effective communication channels established
- [ ] Shared goals and success metrics
- [ ] Joint problem-solving and decision-making
- [ ] Acceptable cognitive load from high communication

#### X-as-a-Service Mode Health  
- [ ] Clear, well-documented APIs and contracts
- [ ] Minimal communication needed for routine interactions
- [ ] Service provider meets agreed SLAs consistently
- [ ] Consumer team can use service independently
- [ ] Appropriate escalation paths for issues

#### Facilitating Mode Health
- [ ] Clear engagement model and success criteria
- [ ] Knowledge transfer is effective and measurable
- [ ] Temporary nature of engagement is respected
- [ ] Capability building rather than just problem-solving
- [ ] Clear exit strategy when capability is established

## Cognitive Load Assessment

### Individual Team Assessment

For each team, assess their cognitive load across three dimensions:

#### Intrinsic Load (Domain Complexity)
Rate the inherent complexity of the team's primary domain:
- [ ] Business domain complexity (1-5)
- [ ] Technical domain complexity (1-5)
- [ ] User needs complexity (1-5)
- [ ] Regulatory/compliance complexity (1-5)

**Intrinsic Load Score: ___/20**

#### Extraneous Load (Unnecessary Complexity)
Rate sources of unnecessary cognitive burden:
- [ ] Tool complexity and proliferation (1-5) 
- [ ] Process overhead and bureaucracy (1-5)
- [ ] Context switching between unrelated domains (1-5)
- [ ] Poor documentation and knowledge management (1-5)

**Extraneous Load Score: ___/20** (Lower is better)

#### Germane Load (Capability Building)
Rate investment in building long-term capabilities:
- [ ] Time available for learning and skill development (1-5)
- [ ] Knowledge sharing and documentation practices (1-5)
- [ ] Investment in automation and tooling (1-5)
- [ ] Reflection and continuous improvement activities (1-5)

**Germane Load Score: ___/20**

### Team Capacity Assessment

| Team | Team Size | Intrinsic Load | Extraneous Load | Germane Load | Load Balance |
|------|-----------|----------------|-----------------|--------------|--------------|
| | | ___/20 | ___/20 | ___/20 | Healthy/At Risk/Overloaded |
| | | | | | |

**Interpretation:**
- **Healthy:** Intrinsic + Extraneous ≤ 12, Germane ≥ 12
- **At Risk:** Intrinsic + Extraneous 13-16, Germane 8-11  
- **Overloaded:** Intrinsic + Extraneous ≥ 17, Germane ≤ 7

## Organizational Design Maturity Assessment

### Conway's Law Alignment

Rate how well your team structure supports your desired architecture:

#### Architecture-Team Alignment (Weight: 40%)
- [ ] Service boundaries match team boundaries (1-5)
- [ ] Team communication patterns support desired system design (1-5)
- [ ] Dependencies between systems match dependencies between teams (1-5)
- [ ] Team ownership model supports system reliability needs (1-5)

**Score: ___/20 → Weighted Score: ___/8**

#### Organizational Evolution Capability (Weight: 30%)
- [ ] Organization can restructure teams as architecture evolves (1-5)
- [ ] Teams can split or merge based on changing needs (1-5)
- [ ] New team types can be introduced when needed (1-5)
- [ ] Team interaction modes can evolve appropriately (1-5)

**Score: ___/20 → Weighted Score: ___/6**

#### Information Flow Optimization (Weight: 30%)
- [ ] Information flows efficiently to where decisions are made (1-5)
- [ ] Teams have appropriate autonomy for their scope (1-5)
- [ ] Communication overhead is minimized (1-5)
- [ ] Knowledge sharing happens effectively across teams (1-5)

**Score: ___/20 → Weighted Score: ___/6**

**Overall Organizational Design Maturity: ___/20**

## Action Planning Template

### Priority Issues Identified

| Issue | Impact (1-5) | Effort (1-5) | Priority | Target Team(s) | Timeline |
|-------|--------------|--------------|----------|----------------|----------|
| | | | High/Medium/Low | | |
| | | | | | |

### Improvement Roadmap

#### Phase 1: Quick Wins (0-3 months)
- [ ] Action item 1
- [ ] Action item 2  
- [ ] Action item 3

#### Phase 2: Structural Changes (3-9 months)
- [ ] Action item 1
- [ ] Action item 2
- [ ] Action item 3

#### Phase 3: Cultural Evolution (6-18 months)  
- [ ] Action item 1
- [ ] Action item 2
- [ ] Action item 3

### Success Metrics

Define specific, measurable outcomes for your team topology improvements:

#### Delivery Metrics
- Lead time: From idea to production
- Deployment frequency: How often teams can deploy
- Change failure rate: Percentage of deployments causing issues
- Recovery time: Time to resolve production issues

#### Team Health Metrics
- Team satisfaction and engagement scores
- Knowledge sharing and learning indicators  
- Cognitive load and workload sustainability
- Inter-team collaboration effectiveness

#### Business Outcome Metrics
- Feature adoption and user engagement
- Business value delivery velocity
- Innovation and experimentation rate
- Technical debt and maintenance overhead

## Regular Assessment Schedule

### Monthly Team Health Checks
- Individual team health scores
- Interaction mode effectiveness review
- Cognitive load monitoring

### Quarterly Organizational Review
- Overall team topology assessment
- Conway's Law alignment evaluation
- Structural improvement planning

### Annual Strategic Assessment  
- Organizational design maturity evaluation
- Long-term evolution planning
- Success metrics and outcome review

This assessment framework provides the data needed to make informed decisions about team structure and evolution. Regular use helps ensure your organization continues to optimize for flow, learning, and business outcomes.

## Further Reading

- Skelton, Matthew, and Manuel Pais. *Team Topologies: Organizing Business and Technology Teams for Fast Flow*. 2019.
- Forsgren, Nicole, Jez Humble, and Gene Kim. *Accelerate: The Science of Lean Software and DevOps*. 2018.
- Conway, Melvin E. "How Do Committees Invent?" *Datamation* 14, no. 4 (1968): 28-31.