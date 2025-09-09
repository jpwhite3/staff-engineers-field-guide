# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Staff Engineer's Field Guide - a comprehensive, community-driven resource for Staff, Principal, and Distinguished Engineers. The content is organized into a structured learning path covering technical leadership, influence, and execution at senior levels.

## Architecture

**Documentation Structure:**
- `docs/field-guide/` - Core field guide content organized into chapters (Leadership, Engineering, Execution, etc.)
- `docs/appendix/` - Supplementary materials including antipatterns, design patterns, domain-driven design concepts, laws, tools, and values
- `src/` - Source content that may be used for generation or processing
- `mkdocs.yml` - Site navigation and configuration

**Content Organization:**
The guide follows a hierarchical structure with major sections:
- Introduction (archetypes: Tech Lead, Architect, Solver, Right Hand)
- Learning (expertise development, mentorship, staying current)
- Ethics (bias, privacy, frameworks, scale, innovation)
- Leadership (influence, feedback, communication, storytelling)
- Teamwork (formation, dysfunction patterns, collaboration)
- Execution (agile, decision-making, strategy, prioritization)
- Engineering (CI/CD, architecture, security, testing)
- Critical Thinking (mental models, biases, problem-solving)
- Business (alignment, pitching, cost optimization)

## Development Commands

**Bootstrap environment:**
```bash
make bootstrap
```

**Local development:**
```bash
make serve
```
Site will be available at http://127.0.0.1:8000

**Build site:**
```bash
make build
```

**Deploy to GitHub Pages:**
```bash
make deploy
```

## Technology Stack

- **Documentation Engine:** MkDocs with Material for MkDocs theme
- **Content Format:** Markdown with support for Mermaid diagrams
- **Dependency Management:** Poetry (Python 3.12+)
- **Deployment:** Automated via GitHub Actions to GitHub Pages

## Content Conventions

- All markdown files use `.md` extension
- Images stored in topic-specific `images/` subdirectories
- Mermaid diagrams supported via pymdownx.superfences extension
- Navigation structure defined in mkdocs.yml matches directory hierarchy

## Enhancement Strategy: Comprehensive Source Integration

### Strategic Overview
Major initiative to transform the field guide into the definitive industry authority through systematic integration of 30+ foundational books, creating 60+ visual frameworks, 300+ cross-references, and professional publication capability.

**Master Tracking Issue:** [#7 - Comprehensive Source Integration Strategy](https://github.com/jpwhite3/staff-engineers-field-guide/issues/7)

### Success Metrics
- **Content Authority**: 30+ authoritative books integrated with full attribution
- **Content Depth**: 75% increase in substantive, actionable content
- **Visual Excellence**: 60+ professional diagrams, decision trees, and assessment tools
- **Cross-References**: 300+ bidirectional topic connections
- **Assessment Tools**: 50+ practical frameworks and evaluation instruments
- **Learning Paths**: 12+ competency-based learning sequences
- **Publication Ready**: Professional book compilation capability

### Implementation Phases

#### Phase 1: Leadership & Organizational Design
**Issue:** [#1 - Leadership Frameworks Integration](https://github.com/jpwhite3/staff-engineers-field-guide/issues/1)
**Timeline:** Months 1-3
**Status:** ✅ Completed - Merged to Main
**Branch:** `phase-1-leadership-organizational-design` (merged)
**Pull Request:** [#8 - Phase 1: Leadership & Organizational Design Integration](https://github.com/jpwhite3/staff-engineers-field-guide/pull/8)

**Authority Sources:**
- Jim Collins - "Good to Great" (Level 5 Leadership, Hedgehog Concept) ✅
- Liz Wiseman - "Multipliers" (5 Disciplines, force multiplier techniques) 🔄 *Planned for future enhancement*
- Kim Scott - "Radical Candor" (feedback frameworks) 🔄 *Existing content enhanced*
- Matthew Skelton & Manuel Pais - "Team Topologies" (organizational design) ✅⭐
- Simon Sinek - "Leaders Eat Last" & "Start with Why" (purpose-driven leadership) ✅⭐

**Key Deliverables - COMPLETED:**
- ✅ Team topology interaction maps and assessment tools (`organizational-design.md`, `team-topology-assessment.md`)
- ✅ Level 5 Leadership integration with staff engineering roles (`leadership/index.md`)
- ✅ Golden Circle framework for technical vision (`technical-vision.md`)
- ✅ Enhanced team formation with Team Topologies patterns (`team-formation.md`)
- ✅ Comprehensive visual frameworks using Mermaid diagrams
- ✅ Cross-reference integration and navigation updates

#### Phase 2: Technical Architecture & Operations Excellence  
**Issue:** [#2 - Technical Architecture Enhancement](https://github.com/jpwhite3/staff-engineers-field-guide/issues/2)
**Timeline:** Months 2-5
**Status:** ✅ Completed - Merged to Main
**Branch:** `phase-2-technical-architecture-operations` (merged)

**Authority Sources:**
- Martin Fowler - "Patterns of Enterprise Application Architecture", "Refactoring"
- Sam Newman - "Building Microservices"
- Martin Kleppmann - "Designing Data-Intensive Applications"
- Google SRE Team - "Site Reliability Engineering" ⭐
- Robert C. Martin - "Clean Architecture" ⭐
- Ford, Parsons, Kua - "Building Evolutionary Architectures" ⭐
- Jez Humble & David Farley - "Continuous Delivery" ⭐

**Key Deliverables:**
- SLI/SLO/Error budget implementation frameworks
- Evolutionary architecture fitness functions
- Clean architecture decision templates
- Comprehensive deployment pipeline patterns

#### Phase 3: Critical Thinking & Decision Making
**Issue:** [#4/#5 - Decision Science Integration](https://github.com/jpwhite3/staff-engineers-field-guide/issues/4)
**Timeline:** Months 3-6
**Status:** ✅ Completed - Merged to Main
**Branch:** `phase-3-critical-thinking-decision-making` (merged)

**Authority Sources:**
- Daniel Kahneman - "Thinking, Fast and Slow" (cognitive science) ✅⭐
- Brian Christian & Tom Griffiths - "Algorithms to Live By" (computational thinking) ✅⭐
- Richard Rumelt - "Good Strategy Bad Strategy" (strategy frameworks) ✅⭐
- John Doerr - "Measure What Matters" (OKR frameworks) ✅⭐
- Dan Ariely - "Predictably Irrational" (behavioral economics) ✅
- Amos Tversky - Cognitive bias research (integrated) ✅

**Key Deliverables - COMPLETED:**
- ✅ Mental models enhancement with System 1/2 thinking (`mental-models.md`)
- ✅ Algorithmic decision-making tools for technical leaders (`algorithmic-decision-making.md`)
- ✅ Strategic thinking frameworks with business alignment (`strategic-thinking.md`)
- ✅ Comprehensive Critical Thinking Assessment framework (`critical-thinking-assessment.md`)
- ✅ Integration of behavioral science with engineering leadership
- ✅ Cross-reference integration and navigation updates

#### Phase 4: Engineering Excellence & Product Integration  
**Issue:** [#6 - Cross-Reference System and Engineering Excellence](https://github.com/jpwhite3/staff-engineers-field-guide/issues/6)
**Timeline:** Months 4-7  
**Status:** 🟡 In Progress - Currently Active
**Branch:** `phase-4-engineering-excellence-product-integration`

**Authority Sources:**
- Kent Beck - "Test-Driven Development By Example" (TDD excellence) ⭐
- Gerard Meszaros - "xUnit Test Patterns" (comprehensive testing) ⭐
- Marty Cagan - "INSPIRED" (product-engineering partnership) ⭐
- Teresa Torres - "Continuous Discovery Habits" (product discovery) ⭐
- Nicole Forsgren, Jez Humble, Gene Kim - "Accelerate" (DORA metrics) ⭐
- Gene Kim, Patrick Debois, John Willis - "The DevOps Handbook" ⭐

**Key Deliverables:**
- Advanced testing strategies and quality frameworks
- Product management integration for technical leaders
- Engineering metrics and measurement systems enhancement  
- Cross-reference system and navigation improvements
- Technical debt management strategies
- DevOps culture and practice integration

#### Phase 5: Organizational Behavior & Team Dynamics
**Issue:** [#3 - Organizational Behavior Integration](https://github.com/jpwhite3/staff-engineers-field-guide/issues/3)
**Timeline:** Months 5-8
**Status:** 🔲 Not Started (Planned after Phase 4)

**Authority Sources:**
- Stanley McChrystal - "Team of Teams" (network organizations)
- Patrick Lencioni - "Five Dysfunctions of a Team" (trust-based development) 
- Chip Heath & Dan Heath - "Switch" (change management)
- Kerry Patterson - "Crucial Conversations" (high-stakes discussions)
- Kim Scott - "Radical Candor" (advanced feedback frameworks)
- Amy Edmondson - "The Fearless Organization" (psychological safety at scale)

**Key Deliverables:**
- Advanced conflict resolution frameworks for technical leaders
- Change management strategies for technical transformations
- Cultural transformation playbook for engineering organizations  
- Advanced mentorship and career development systems
- Network organization design principles
- Team dysfunction assessment with performance integration

#### Phase 6: Publication & Cross-Reference Excellence
**Issue:** [Integrated with Phase 4] - Cross-Reference System and Book Compilation
**Timeline:** Months 7-10
**Status:** 🔄 Partially Integrated (Cross-references in Phase 4)

**Key Deliverables:**
- 300+ bidirectional cross-reference system (🔄 Phase 4 integration)
- Professional book compilation infrastructure (PDF, EPUB)
- Competency-based learning path optimization
- Comprehensive visual asset library (60+ diagrams)
- Academic-standard citation and attribution system

### Progress Tracking

**Overall Status:** ✅ PROJECT COMPLETED - All 5 Phases Successfully Implemented

**Phase Status Legend:**
- 🔲 Not Started
- 🟡 In Progress  
- ✅ Completed
- 🔄 Under Review

**All Phases Completed Successfully:**

**Phase 1: ✅ Leadership & Organizational Design** (PR #8 - Merged)
- Team Topologies integration with organizational design framework
- Level 5 Leadership model for technical leaders  
- Golden Circle framework for technical vision
- Team formation and collaboration patterns

**Phase 2: ✅ Technical Architecture & Operations Excellence** (PR #9 - Merged)
- Site Reliability Engineering comprehensive framework
- Clean Architecture patterns and implementation guide
- Evolutionary Architecture principles and practices
- Continuous Delivery frameworks and best practices
- Engineering Excellence Assessment Framework
- Enhanced with narrative structure and conversational tone

**Phase 3: ✅ Critical Thinking & Decision Making** (Merged)
- Mental Models enhancement with System 1/2 thinking
- Algorithmic decision-making tools for technical leaders
- Strategic thinking frameworks with business alignment
- Comprehensive Critical Thinking Assessment framework
- Integration of behavioral science with engineering leadership

**Phase 4: ✅ Engineering Excellence & Product Integration** (Merged)
- Advanced testing strategies and quality frameworks from Beck and Meszaros
- Product management integration content from Cagan and Torres for technical leaders
- Engineering metrics and measurement systems with DORA metrics and DevOps practices
- Cross-reference system and navigation improvements across all content
- Technical debt management strategies and assessment frameworks
- Comprehensive engineering-product collaboration templates

**Phase 5: ✅ Organizational Behavior & Team Dynamics** (PRs #10 & #12 - Merged)
- Advanced Conflict Resolution frameworks (8,500+ words)
- Change Management for Technical Transformations (8,000+ words)
- Cultural Transformation & Psychological Safety (9,000+ words)
- Advanced Mentorship & Career Development systems (9,500+ words)
- Comprehensive Recommended Reading list with all 25+ authoritative books
- Complete narrative structure enhancement across all content

### Quality Standards

**Content Integration Requirements:**
- Academic-standard citation for all authority sources
- Fair use compliance and copyright clearance
- Original visual assets or properly licensed diagrams  
- Bidirectional cross-references maintained
- Staff engineering practical focus maintained

**Publication Standards:**
- Professional typography and layout
- Multi-format compatibility (web, PDF, EPUB)
- Comprehensive index and glossary
- Legal compliance for all integrated content