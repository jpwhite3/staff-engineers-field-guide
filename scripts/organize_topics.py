#!/usr/bin/env python3
"""
Script to organize and rename files in the topics directory.
"""

import os
import re
import shutil
from pathlib import Path

from build import TOPICS_DIR

# Define categories for organizing files
CATEGORIES = {
    "leadership": [
        "Empowered Teams & Decision-Making",
        "How to Develop Future Staff Engineers",
        "Team Formation & High-Performing Teams",
        "The Five Dysfunctions of a Team",
        "The Importance of Mentorship & Sponsorship",
        "The Power of Vulnerability in Leadership",
        "Psychological Safety & Trust in Teams",
        "Working Across Boundaries & Managing Stakeholders",
        "Feature Teams & Organizational Transformation",
    ],
    "communication": [
        "Asynchronous Communication Best Practices",
        "Cross-Functional Teams & Collaboration",
        "Delivering Difficult Messages",
        "Giving & Receiving Feedback",
        "How to Pitch Engineering Projects to Executives",
        "Influencing Without Authority",
        "Lessons from The Culture Map",
        "Presentation & Persuasion Skills",
        "Storytelling for Engineers",
        "Technical Writing for Influence",
        "The Dirty Dozen – Hardest Questions in Technical Discussions",
    ],
    "technical": [
        "Architecture Decision Records (ADRs)",
        "Balancing Speed vs. Quality in Engineering",
        "Bias in Machine Learning & Automation",
        "Code Hygiene & Refactoring",
        "Continuous Integration & Continuous Delivery",
        "DevOps & Automation Engineering",
        "Hexagonal Architecture & Scalable System Design",
        "Software Supply Chain Security",
        "Source Code Management & Git Best Practices",
        "Test-Driven Development",
    ],
    "strategy": [
        "Aligning Technology to Business Strategy",
        "Building a Better Business Case",
        "Cost Optimization & Cloud Financial Management",
        "Customer-Centric Thinking in Engineering",
        "Decision-Making Frameworks for Engineers",
        "Mental Models for Engineers",
        "Mind Mapping & Visual Thinking for Problem Solving",
        "Revenue & Risk Trade-offs in Engineering",
        "Strategic Thinking for Engineers",
        "Structured Problem-Solving Techniques",
    ],
    "process": [
        "Agile Essentials",
        "Countering Groupthink & Mismanagement of Agreement",
        "Mismanagement of Agreement",
        "Navigating Uncertainty & Change",
        "Story Mapping & Story Splitting",
    ],
    "personal_growth": [
        "Building & Using Your Network",
        "Cognitive Biases in Engineering",
        "Developing Deep Technical Expertise",
        "Lifelong Learning & Staying Ahead of Industry Trends",
        "Power & Influence in Organizations",
        "Self-Awareness & Personality Types",
        "The Ethical Engineer: Decision-Making Under Uncertainty",
    ],
}


def to_kebab_case(text):
    """Convert text to kebab-case."""
    # Remove parentheses and their contents
    text = re.sub(r"\s*\([^)]*\)", "", text)

    # Remove special characters and convert to lowercase
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text).lower()

    # Replace spaces with hyphens and remove consecutive hyphens
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"-+", "-", text)

    return text


def find_category(filename):
    """Find the category for a given filename."""
    for category, patterns in CATEGORIES.items():
        for pattern in patterns:
            if pattern.lower() in filename.lower():
                return category
    return "uncategorized"


def organize_files():
    """Organize files in the topics directory."""
    # Get all markdown files in the root of the topics directory
    files = [f for f in TOPICS_DIR.glob("*.md") if f.is_file()]

    # Create category directories if they don't exist
    for category in CATEGORIES.keys():
        category_dir = TOPICS_DIR / category
        category_dir.mkdir(exist_ok=True)

    # Create uncategorized directory
    uncategorized_dir = TOPICS_DIR / "uncategorized"
    uncategorized_dir.mkdir(exist_ok=True)

    # Process each file
    for file_path in files:
        # Skip files that are already in subdirectories
        if len(file_path.parts) > 2:
            continue

        # Get the original filename without extension
        original_name = file_path.stem

        # Find the category for this file
        category = find_category(original_name)

        # Convert filename to kebab-case
        new_name = to_kebab_case(original_name) + ".md"

        # Create the destination path
        dest_dir = TOPICS_DIR / category
        dest_path = dest_dir / new_name

        print(f"Moving {file_path} to {dest_path}")

        # Move the file
        shutil.move(file_path, dest_path)


if __name__ == "__main__":
    organize_files()
    print("Files have been organized successfully!")
