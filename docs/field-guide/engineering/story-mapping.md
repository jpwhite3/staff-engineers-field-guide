# Story Mapping & Story Splitting: Building the Right Thing, Incrementally

## The Scenario

A product team is planning a new feature: an automated recommendation engine for their e-commerce platform. The product manager writes a user story: "As a customer, I want personalized product recommendations so I can discover products I might like." The engineering team estimates it as "epic-sized" — too large to fit in a single sprint. They struggle to break it down, eventually creating arbitrary technical slices: "Set up recommendation database schema," "Create API endpoints," "Build UI components." Two months later, they have many completed stories but still no working recommendation feature for users. The project is technically "on track" but delivering no value.

This scenario illustrates a common problem in agile development: the challenge of breaking down large features into valuable, independently deliverable slices. Story mapping and story splitting are powerful techniques that help teams deliver incremental value rather than incremental construction. As a Staff Engineer, mastering these techniques will help you ensure your team is building the right thing in the right order.

## What is Story Mapping?

Story mapping, developed by Jeff Patton, is a technique for organizing user stories to create a model of the system from a user-centric perspective. Unlike a flat backlog, which obscures the big picture, a story map creates a two-dimensional view of your product:

- **The horizontal axis (backbone)** represents user activities in sequential order
- **The vertical axis (walking skeleton)** represents priority, with the most critical functionality at the top

This visualization helps teams:

- Understand the full scope of the system
- Identify the minimum viable product (MVP)
- Plan releases that deliver end-to-end value
- Communicate the product vision to stakeholders

## Creating a Story Map

### 1. Identify User Activities (The Backbone)

Start by mapping the major activities users perform, in sequential order:

**E-commerce Example:**

1. Browse products
2. Search for specific items
3. Learn about products
4. Add to cart
5. Checkout
6. Track order
7. Receive product
8. Return if needed

These activities form the "backbone" of your map.

### 2. Drill Down into User Tasks (The Ribs)

Under each activity, list the specific tasks users perform:

**Under "Search for specific items":**

- Enter search terms
- Filter search results
- Sort results by relevance/price/rating
- Compare multiple products
- Save items for later

### 3. Slice into Releases (The Walking Skeleton)

Draw horizontal lines across your map to define releases, prioritizing tasks that create a "walking skeleton"—a thin end-to-end slice of functionality:

**Release 1 (MVP):**

- Basic search by keyword
- Simple product detail page
- Add to cart
- Simple checkout flow
- Order confirmation email

**Release 2:**

- Search filters
- Product recommendations
- Save for later
- Multiple payment methods

This approach ensures each release delivers end-to-end value to users.

## The Art of Story Splitting

Once you have a story map, you still need to split large stories into sprint-sized pieces. The key is to split stories by value rather than by technical layer.

### Common Anti-patterns in Story Splitting

#### 1. Horizontal/Layer Splitting

❌ **Bad:** Splitting by technical layer

- Frontend: Build recommendation UI
- Backend: Create recommendation API
- Data: Set up recommendation database

**Problem:** No value until all three are complete

#### 2. Technical Task Splitting

❌ **Bad:** Turning development tasks into stories

- Set up development environment
- Create database schema
- Write automated tests

**Problem:** These are tasks, not valuable increments

#### 3. Split by "Happy Path" vs. Edge Cases

❌ **Bad:** Deferring all edge cases

- Basic recommendation engine (happy path)
- Handle new users with no history
- Handle product categories with limited inventory

**Problem:** The system isn't truly usable without handling key edge cases

### Better Approaches to Story Splitting

#### 1. Split by User Workflow Steps

✅ **Good:** Split a complex workflow into smaller steps

**Instead of:** "As a user, I want a complete checkout process"

**Split into:**

- "As a user, I want to enter shipping information"
- "As a user, I want to enter payment information"
- "As a user, I want to review my order before confirming"

#### 2. Split by User Personas or Segments

✅ **Good:** Deliver to one user type before expanding

**Instead of:** "As a user, I want personalized recommendations"

**Split into:**

- "As a returning user, I want recommendations based on my purchase history"
- "As a new user, I want recommendations based on popular items"
- "As a user browsing a category, I want similar items in that category"

#### 3. Split by Business Rules or Capabilities

✅ **Good:** Implement one business rule at a time

**Instead of:** "As a user, I want dynamic pricing based on multiple factors"

**Split into:**

- "As a user, I want time-based discounts (happy hour pricing)"
- "As a user, I want volume-based discounts"
- "As a user, I want loyalty tier-based discounts"

#### 4. Split by Data Types or Parameters

✅ **Good:** Handle one type of data before expanding

**Instead of:** "As a user, I want to import data from any source"

**Split into:**

- "As a user, I want to import CSV files"
- "As a user, I want to import Excel files"
- "As a user, I want to import Google Sheets"

#### 5. Split by Operational Qualities

✅ **Good:** Deliver core functionality first, then enhance performance/scale

**Instead of:** "As a user, I want lightning-fast search results"

**Split into:**

- "As a user, I want relevant search results (within 2 seconds)"
- "As a user, I want search results to appear as I type"
- "As a user, I want search results in under 200ms"

### The SPIDR Technique for Story Splitting

SPIDR is a mnemonic for five approaches to splitting stories:

- **S**pike: Create a small experiment to resolve uncertainty
- **P**ath: Split by happy path vs. alternative paths
- **I**nterface: Split by different interfaces or access methods
- **D**ata: Split by data types or sources
- **R**ules: Split by business rules or algorithms

## Validating Good Story Splits

After splitting stories, validate them against these criteria:

### 1. Independence

Can this story be delivered independently of other stories?

### 2. Value

Does this story deliver real value to users or stakeholders?

### 3. Estimable

Is the story small enough and clear enough to estimate confidently?

### 4. Testable

Can we write acceptance criteria that verify when it's done?

### 5. Small

Can it be completed within a sprint by a pair of developers?

## Case Study: Splitting the Recommendation Engine

Let's return to our original example and split it properly:

**Original Epic:** "As a customer, I want personalized product recommendations so I can discover products I might like."

### Story Map for Recommendations Feature:

**User Activities:**

1. View recommended products
2. Interact with recommendations
3. Receive increasingly relevant recommendations

**Vertical Slicing - Release 1 (MVP):**

- "As a customer viewing a product, I want to see 'Customers who bought this also bought' recommendations"
- "As a customer, I want recommended products to link directly to their detail pages"

**Release 2 (Enhanced):**

- "As a returning customer, I want homepage recommendations based on my purchase history"
- "As a customer, I want to rate recommendations as helpful or not helpful"

**Release 3 (Advanced):**

- "As a customer, I want recommendations based on my browsing behavior"
- "As a customer, I want to see why each item was recommended to me"

Each story:

- Delivers tangible value
- Can be implemented end-to-end in a single sprint
- Builds upon previous stories
- Is independently valuable

## The Staff Engineer's Role

As a Staff Engineer, you play a crucial role in story mapping and splitting:

### 1. Bridge Business and Technical Perspectives

Help product managers understand technical constraints and help engineers understand business priorities. Facilitate conversations that lead to valuable story splits.

### 2. Identify Technical Dependencies

Spot dependencies that might impact the sequencing of stories and recommend ways to minimize them through architectural decisions.

### 3. Balance Short-term Delivery with Long-term Architecture

Ensure that incremental delivery doesn't create technical debt that will slow future iterations. Identify foundational work that enables rapid delivery of subsequent stories.

### 4. Teach and Coach

Help the team learn effective story splitting techniques. Review proposed splits and provide feedback on how to improve them.

### 5. Challenge Artificial Constraints

Question assumptions about what must be built together versus what can be separated. Often, what seems coupled can be decoupled with creative thinking.

By mastering story mapping and story splitting, you help your team focus on delivering value incrementally rather than building components that only deliver value when integrated. This results in faster feedback, earlier return on investment, and more satisfied users.

## Cross-Reference Navigation

<div class="grid cards" markdown>

- **:material-account-group: Team Collaboration Integration**

    **User-Centric Development**

    Connect with [Team Formation](../teamwork/team-formation.md) for collaborative development practices and [Product Engineering Collaboration](../business/product-engineering-collaboration.md) for effective product-engineering partnerships

- **:material-chart-line: Strategic & Business Alignment**

    **Value-Driven Development**

    Integrate with [Strategic Thinking](../execution/strategic-thinking.md) for business-aligned technical decisions and [Engineering Metrics](../business/engineering-metrics-business-alignment.md) for value measurement

- **:material-sitemap: Architecture & System Design**

    **Incremental Architecture**

    Apply to [Clean Architecture](clean-architecture.md) for modular, incrementally deliverable systems and [Evolutionary Architecture](evolutionary-architecture.md) for value-driven architectural evolution

- **:material-rocket-launch: Delivery & Quality Integration**

    **Incremental Delivery Excellence**

    Support with [Continuous Delivery](continuous-delivery.md) for frequent value delivery and [Advanced Testing Strategies](advanced-testing-strategies.md) for story-level quality assurance

- **:material-clipboard-check: Assessment & Development**

    **Track Collaboration Skills**

    Use [Staff Engineer Competency Assessment](../../appendix/tools/staff-engineer-competency-assessment.md) for product collaboration evaluation and [Team Health Diagnostic](../../appendix/tools/team-health-diagnostic.md) for cross-functional team effectiveness

- **:material-map-marker-path: Learning Progression**

    **Deepen Product Leadership**

    Progress to [Product Engineering Collaboration](../business/product-engineering-collaboration.md) mastery, [Strategic Thinking](../execution/strategic-thinking.md) development, and [Business Integration](../business/index.md) for comprehensive product-engineering expertise

</div>
