# Core Engineering Skills & Practices

While the Staff Engineer role is heavily focused on leadership, influence, and strategy, these skills are built upon a bedrock of deep technical expertise. Your credibility as a leader flows directly from your authority as an engineer. You cannot guide a team through complex technical challenges if you haven't mastered the fundamentals of modern software development yourself.

This chapter dives into the core practices that separate high-performing engineering organizations from the rest. It's not about chasing the latest trendy technology; it's about mastering the timeless principles of building and shipping high-quality software efficiently and safely.

As a Staff Engineer, you are no longer just a *practitioner* of these skills; you are a *steward* and a *teacher*. You are responsible for establishing these practices on your team, mentoring others in their use, and continuously improving the systems that enable them. From the discipline of Test-Driven Development to the nuances of scalable system design, from the flow of CI/CD to the security of your software supply chain, this is the technical foundation upon which your leadership is built.

## Discrete Topics Covered

* [Architecture Decision Records (ADRs)](adrs.md): Learn to document significant architectural decisions to preserve context and accelerate future work.

* [Chaos Engineering](chaos-engineering.md): Discover how to proactively test system resilience by injecting controlled failures.
* [CI/CD](cicd.md): Master the principles of Continuous Integration and Continuous Delivery to build a high-velocity, reliable deployment pipeline.
* [Code Hygiene & Refactoring](code-hygiene.md): Adopt the "Boy Scout Rule" to continuously improve codebase health and prevent technical debt.
* [DevOps](devops.md): Embrace the "You Build It, You Run It" mindset to foster team ownership and build more operable systems.
* [Source Control Best Practices](source-control.md): Use Git and other tools as a precise language for collaboration through atomic commits and effective pull requests.
* [Hexagonal Architecture](hexagonal-architecture.md): Protect your core business logic from external concerns using the Ports and Adapters pattern.
* [Software Supply Chain Security](software-supply-chain-security.md): Learn to secure your applications by managing dependencies, creating SBOMs, and hardening your build pipeline.
* [Story Mapping & Splitting](story-mapping.md): Build a shared understanding of the user's journey and deliver value incrementally.
* [Test-Driven Development (TDD)](tdd.md): Use testing as a design tool to create modular, maintainable, and well-designed software.

## Further Reading

This chapter covers a wide range of technical practices, each with a rich history and body of literature. For deeper study, we recommend:

*   **Beck, Kent. *Test Driven Development: By Example*.** (2002). The seminal work on TDD, written by its creator.
*   **Cockburn, Alistair. "Hexagonal Architecture."** (2005). The original article that introduced the Ports and Adapters pattern.
*   **Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software*.** (2003). A foundational text for understanding how to model complex business domains, which pairs well with Hexagonal Architecture.
*   **Feathers, Michael C. *Working Effectively with Legacy Code*.** (2004). An essential guide for applying tests and refactoring techniques to large, existing codebases.
*   **Fowler, Martin. *Refactoring: Improving the Design of Existing Code*.** (1999). The classic catalog of code smells and refactoring techniques.
*   **Freeman, Steve, and Nat Pryce. *Growing Object-Oriented Software, Guided by Tests*.** (2009). A key text on the "London School" of TDD, focusing on outside-in development and mocking.
*   **Kleppmann, Martin. *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*.** (2017). A comprehensive guide to the principles of modern data systems.
