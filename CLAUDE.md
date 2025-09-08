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
**Status:** 🔲 Not Started

**Authority Sources:**
- Jim Collins - "Good to Great" (Level 5 Leadership, Hedgehog Concept)
- Liz Wiseman - "Multipliers" (5 Disciplines, force multiplier techniques)
- Kim Scott - "Radical Candor" (feedback frameworks)
- Matthew Skelton & Manuel Pais - "Team Topologies" (organizational design) ⭐
- Simon Sinek - "Leaders Eat Last" & "Start with Why" (purpose-driven leadership) ⭐

**Key Deliverables:**
- Team topology interaction maps and assessment tools
- Level 5 Leadership integration with staff engineering roles
- Golden Circle framework for technical vision
- Circle of Safety organizational design principles

#### Phase 2: Technical Architecture & Operations Excellence  
**Issue:** [#2 - Technical Architecture Enhancement](https://github.com/jpwhite3/staff-engineers-field-guide/issues/2)
**Timeline:** Months 2-5
**Status:** 🔲 Not Started

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

#### Phase 3: Performance Science & Team Excellence
**Issue:** [#3 - Organizational Behavior Integration](https://github.com/jpwhite3/staff-engineers-field-guide/issues/3)
**Timeline:** Months 3-6
**Status:** 🔲 Not Started

**Authority Sources:**
- Stanley McChrystal - "Team of Teams" (network organizations)
- Patrick Lencioni - "Five Dysfunctions of a Team" (trust-based development)
- Chip Heath & Dan Heath - "Switch" (change management)
- Neel Doshi & Lindsay McGregor - "Primed to Perform" (performance science) ⭐

**Key Deliverables:**
- Total Motivation (ToMo) assessment tools for technical teams
- Network organization design principles
- Change management frameworks for technical transformation
- Team dysfunction assessment with performance integration

#### Phase 4: Decision Science & Personal Excellence
**Issue:** [#4 - Decision-Making and Strategic Enhancement](https://github.com/jpwhite3/staff-engineers-field-guide/issues/4)
**Timeline:** Months 4-7  
**Status:** 🔲 Not Started

**Authority Sources:**
- Daniel Kahneman - "Thinking, Fast and Slow" (cognitive science)
- Richard Rumelt - "Good Strategy Bad Strategy" (strategy frameworks)
- Eric Ries - "The Lean Startup" (experimental approaches)
- Brian Christian & Tom Griffiths - "Algorithms to Live By" (computational thinking) ⭐
- James Clear - "Atomic Habits" (habit formation science) ⭐
- John Doerr - "Measure What Matters" (OKR frameworks) ⭐

**Key Deliverables:**
- Algorithmic decision-making tools for technical leaders
- Habit formation systems for continuous improvement
- OKR implementation guides for engineering teams
- Computational approaches to leadership challenges

#### Phase 5: Engineering Excellence & Product Integration
**Issue:** [#5 - Software Engineering Classics Integration](https://github.com/jpwhite3/staff-engineers-field-guide/issues/5)
**Timeline:** Months 5-8
**Status:** 🔲 Not Started

**Authority Sources:**
- Robert C. Martin - "Clean Code" (SOLID principles, craftsmanship)
- Martin Fowler - "Refactoring" (comprehensive refactoring catalog)
- David Thomas & Andrew Hunt - "The Pragmatic Programmer" (practical techniques)
- Michael Feathers - "Working Effectively with Legacy Code" (legacy mastery) ⭐
- Kent Beck - "Test-Driven Development By Example" (TDD excellence) ⭐
- Marty Cagan - "INSPIRED" (product-engineering partnership) ⭐
- Jeff Patton - "User Story Mapping" (requirements engineering) ⭐

**Key Deliverables:**
- Legacy code characterization and improvement frameworks
- Product discovery integration for technical leaders
- TDD implementation patterns and techniques
- Engineering-product collaboration templates

#### Phase 6: Publication & Cross-Reference Excellence
**Issue:** [#6 - Cross-Reference System and Book Compilation](https://github.com/jpwhite3/staff-engineers-field-guide/issues/6)
**Timeline:** Months 7-10
**Status:** 🔲 Not Started

**Key Deliverables:**
- 300+ bidirectional cross-reference system
- Professional book compilation infrastructure (PDF, EPUB)
- Competency-based learning path optimization
- Comprehensive visual asset library (60+ diagrams)
- Academic-standard citation and attribution system

### Progress Tracking

**Overall Status:** 🔲 Planning Complete - Ready for Implementation

**Phase Status Legend:**
- 🔲 Not Started
- 🟡 In Progress  
- ✅ Completed
- 🔄 Under Review

**Next Actions:**
1. Begin Phase 1 implementation with Team Topologies integration
2. Establish visual design standards and template system
3. Create authority source citation framework
4. Set up cross-reference tracking system

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