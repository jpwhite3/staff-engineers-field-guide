# Staff Engineer's Field Guide - Content Page Template

This template provides the standardized structure for all field guide content pages to ensure consistency across the entire guide.

## Standard Page Structure

### Required Sections (All Pages)

1. **Title (H1)** - Clear, descriptive title
2. **Introduction paragraph** - Context and importance
3. **Main content sections** - Core material organized with H2/H3 headings
4. **Cross-Reference Navigation** - Links to related content (see template below)
5. **Further Reading** - Categorized bibliography (see template below)

### Optional Sections (As Appropriate)

- **Key Takeaways** - For complex topics that benefit from summary
- **Learning Path Recommendations** - For foundational or index pages
- **Assessment Tools** - Links to relevant evaluation frameworks

---

## Template: Cross-Reference Navigation Section

```markdown
## Cross-Reference Navigation

### Prerequisites for This Chapter
- **[Required Topic 1](../section/topic.md)** - Brief explanation of why it's prerequisite
- **[Required Topic 2](../section/topic.md)** - Brief explanation of why it's prerequisite

### Related Concepts
- **[Related Topic 1](../section/topic.md)** - How it relates to current topic
- **[Related Topic 2](../section/topic.md)** - How it relates to current topic

### Apply These Concepts
- **[Assessment Tool](../../appendix/tools/assessment.md)** - Description of how to use
- **[Framework Tool](../../appendix/tools/framework.md)** - Description of practical application

### Next Steps in Your Learning Journey
1. **[Next Topic 1](../section/next-topic.md)** - Why this follows logically
2. **[Next Topic 2](../section/next-topic.md)** - Alternative progression path
3. **[Advanced Topic](../section/advanced.md)** - For deeper exploration
```

---

## Template: Further Reading Section

```markdown
## Further Reading

**Core Topic Foundation**:
- Author, Name. *Book Title*. Year. (Brief description of relevance)
- Author, Name. *Book Title*. Year. (Brief description of relevance)

**Advanced Applications**:
- Author, Name. *Book Title*. Year. (Brief description of relevance)
- Author, Name. *Book Title*. Year. (Brief description of relevance)

**Related Disciplines**:
- Author, Name. *Book Title*. Year. (Brief description of relevance)
- Author, Name. *Book Title*. Year. (Brief description of relevance)
```

---

## Template: Learning Path Recommendations (For Index Pages Only)

```markdown
### Learning Path Recommendations

**For New Staff Engineers**: Start with **[Foundation Topic](topic.md)** and **[Essential Skill](skill.md)**, then progress to [advanced topics] as you gain experience with [specific context].

**For Experienced Technical Leaders**: Focus on **[Advanced Topic 1](topic.md)** and **[Strategic Topic](topic.md)**, especially if you're moving into roles with [specific responsibilities].

**For [Specific Role/Context]**: Emphasize **[Specialized Topic 1](topic.md)**, **[Specialized Topic 2](topic.md)**, and **[Integration Topic](topic.md)** for [specific outcomes].
```

---

## Template: Key Takeaways (When Appropriate)

```markdown
## Key Takeaways

1. **Main Concept 1** - Brief actionable insight
2. **Main Concept 2** - Brief actionable insight  
3. **Main Concept 3** - Brief actionable insight
4. **Implementation Focus** - Most important thing to remember
5. **Next Action** - Specific step reader should take
```

---

## Standardization Rules

### Cross-Reference Navigation
- **Always include** for substantial content pages (>1000 words)
- **Prerequisites**: Only list genuine prerequisites, not just related topics
- **Related Concepts**: 2-4 closely related topics maximum
- **Apply These Concepts**: Focus on practical tools and assessments
- **Next Steps**: Logical progression paths, not comprehensive lists

### Further Reading
- **Categorize** by topic relevance (Core Foundation, Advanced Applications, Related Disciplines)
- **3-6 books per category** maximum to avoid overwhelming readers
- **Brief descriptions** (1 sentence) explaining relevance to staff engineering
- **Full citations** with Author, Title, Year format
- **Authority sources** prioritized (established experts, seminal works)

### Learning Path Recommendations
- **Include only on index/foundational pages**
- **3 distinct paths maximum** targeting different experience levels or roles
- **Specific progression** with clear next steps
- **Context explanation** for why each path is recommended

### Key Takeaways
- **Use sparingly** - only for complex topics that truly benefit from summary
- **5 points maximum** to maintain focus
- **Actionable insights** rather than just restatements
- **Implementation-focused** final points

---

## File Naming and Organization

- Index pages: `index.md`
- Topic pages: `kebab-case-topic-name.md`
- Cross-references use relative paths
- Assessment tools in `../../appendix/tools/`
- Maintain consistent directory structure within field-guide/

This template ensures consistency while allowing for content-specific customization where appropriate.