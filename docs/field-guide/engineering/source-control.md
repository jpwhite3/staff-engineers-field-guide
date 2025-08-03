# Source Control: Mastering Git

## The Scenario

A team is working on a critical service that was built five years ago. The code is difficult to understand, and the Git history is a mess of large, vague commits like "fixed stuff." A new bug has appeared in production, and no one can figure out which change introduced it. The team spends days using `git bisect` to hunt down the problem, a process that could have taken minutes with a clean history.

Source Code Management (SCM) isn't just about saving your work; it's the narrative of your project. A clean, well-managed history is a critical tool for collaboration, debugging, and maintenance. As a Staff Engineer, establishing robust SCM practices is essential for team velocity and system stability.

## Core Principles of Effective SCM

### 1. Commit Often, Commit Small

Each commit should be a single, logical, atomic change.

*   **Good:** A commit that refactors one function and updates its tests.
*   **Bad:** A commit that refactors a function, adds a new feature, and fixes an unrelated bug.

Small commits are easier to understand, review, and revert if they cause problems.

### 2. Write Clear Commit Messages

A commit message should explain the *why* behind a change, not just the *what*. A good structure is:

-   **Subject Line (50 chars max):** A concise summary of the change. Use the imperative mood (e.g., "Add user authentication endpoint," not "Added..." or "Adds...").
-   **Body (Optional):** A more detailed explanation of the problem, the solution, and any relevant context.

### 3. Use Branches for Isolation

All new work should happen on a branch, never directly on `main`. This keeps the main branch stable and deployable at all times. Modern development favors short-lived feature branches that are integrated quickly, often called Trunk-Based Development.

### 4. Review Every Change

Use Pull Requests (or Merge Requests) to review every change before it's merged into the main branch. Code reviews are not just for catching bugs; they are for sharing knowledge, improving code quality, and ensuring consistency.

## A Practical Exercise: The Git Role Play

-   **Objective:** To demonstrate the flow of changes in a collaborative environment.
-   **Setup:** Gather your team with a whiteboard. Draw a line representing the `main` branch.
-   **Execution:** Have team members act as developers. They "create a branch" by drawing a new line off `main`. They add "commits" as sticky notes on their branch. Then, they "open a pull request" and walk through the changes before "merging" the stickies onto the main line.
-   **Debrief:** Discuss how the process felt, where conflicts might arise, and the importance of clear communication.

## Further Reading

-   *Pro Git* by Scott Chacon and Ben Straub
-   Atlassian's Git Tutorials
