import os
import re
import shutil
import subprocess
from collections import defaultdict
from pathlib import Path

import ollama
import yaml
from ollama import Client

TOPIC_DIR = Path(__file__).parent.joinpath("topics")
DOCS_DIR = Path(__file__).parent.joinpath("docs")
BOOK_DIR = Path(__file__).parent.joinpath("book")

# Path to your existing markdown files
EXISTING_ARTICLES_PATH = TOPIC_DIR

BASE_PROMPT = """
    <Role>
    Your are a world class technical writer, author, and software developer with over 30 years of experience. 
    You excel at crafting interesting and informative narratives when explaining complex topics, that anyone can understand, regardless of skill level.  
    You are a master at communicating the maximum amount of information using the fewest words possible. 
    </Role>

    <Context>
    You’ve been given a collection of short-form technical articles intended for staff-level engineers and technical practitioners. Each article introduces an important concept or practice, but suffers from a lack of depth, context, and actionable insight. Your task is to rewrite each article to significantly improve its usefulness and impact, while maintaining the original tone (friendly, clear, professional).
    </Context>

    <Instructions>
    1. Conduct deep research on the subject in the provided article, through the practical lens of a "staff engineer" (as defined in the book "The Staff Engineer's Path")
    2. Strengthen the introduction by making the topic relevant to the reader’s work and including real-world implications or risks of not understanding the concept.
    3.	Deepen the conceptual sections by:
        - Expand the abstract into more detailed explanations of key terms and concepts in depth using new terminology where necessary (e.g., ‘machine learning’ becomes a broad overview with subtopics like regression, classification etc.).- Adding more nuanced explanations of terms and types.
        - Including analogies, examples, or metaphors to aid understanding.
        - Exploring adjacent or underlying concepts where appropriate.
    4.	Add multiple real-world examples, ideally from different domains or industries to show broad applicability.
    5.	Expand the practical application section with:
        - Step-by-step advice or frameworks engineers can follow.
        - Pitfalls and anti-patterns with suggested solutions.
        - Tooling or processes that can help.
    6.	If a teaching or activity section is present, enhance it with:
        - Reflection or debrief prompts.
        - Suggestions for adapting it to different learning styles or audiences.
        - Ideas for follow-up or deeper learning.
    7.	End with a motivating call to action, highlighting how mastering this concept can improve systems, collaboration, and outcomes. This encourages engagement and helps to motivate the reader. The call should be clear about what they can expect from this article (e.g., understanding bias in ML), how it will benefit them if understood correctly or not understandable at all due diligence is needed beforehand, etc.
    8. Write in clear, direct language. Use markdown headings. Be generous with real examples. Use narrative paragraphs over bulleted lists when appropriate. Ensure the revised article is 2x to 3x the length of the original if needed, aiming for richness over brevity.
    9. Finally, ensure the response is **only** in valid Markdown format without any introductory text, explanations, or additional comments. Do not include phrases like 'Here is the rewritten article'. Or other acknowledgements of any kind.
    </Instructions>
"""


def rewrite_article(file_path):
    # Read input file
    try:
        with open(file_path, "r") as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    output_file_path = Path(os.path.splitext(file_path)[0] + "_rewritten.md")
    if output_file_path.exists():
        print(
            f'Error: File "{output_file_path}" already exists, please delete it before proceeding'
        )
        return

    # Define the prompt to enforce markdown output
    prompt = (
        BASE_PROMPT
        + f"""
    <User_Input>
    ---

    {markdown_text}

    ---
    </User_Input>
    """
    )

    # Call Ollama API to rewrite the article
    try:
        response = ollama.chat(
            model="gemma3", messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return

    # Extract response content
    rewritten_text = response.get("message", {}).get(
        "content", response.get("content", "")
    )

    if not rewritten_text:
        print("Unexpected response format from Ollama:", response)
        return

    # Save the rewritten article to a new file
    try:
        with open(output_file_path, "w") as f:
            f.write(rewritten_text)
        print(f"Rewritten article saved to: {output_file_path}")
    except Exception as e:
        print(f"Error saving the rewritten article: {e}")


def generate_new_article(topic):
    output_file_path = Path(f"{topic}.md")
    if output_file_path.exists():
        print(f"File {output_file_path} already exists, skipping.")
        return None

    # Use Ollama to generate a new article based on the topic and format
    prompt = (
        BASE_PROMPT
        + f"""
    <User_Input>
    ---

    {topic}

    ---
    </User_Input>
    """
    )
    try:
        response = ollama.chat(
            model="gemma3", messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return

    # Extract response content
    new_article_text = response.get("message", {}).get(
        "content", response.get("content", "")
    )

    if not new_article_text:
        print("Unexpected response format from Ollama:", response)
        return

    # Save the new article to a file
    with open(output_file_path, "w") as f:
        f.write(new_article_text)
    print(f"New article saved to: {output_file_path}")


def organize_and_build_book():
    """
    Organize topics and build the book.
    """
    # Analyze and organize topics
    categories = analyze_topics()

    # Generate MkDocs configuration
    generate_mkdocs_config(categories)

    # Build the book
    build_mkdocs_book()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Build a book from topics using AI and MkDocs"
    )
    parser.add_argument(
        "--rewrite", action="store_true", help="Rewrite articles using AI"
    )
    parser.add_argument(
        "--build", action="store_true", help="Build the book without rewriting"
    )
    parser.add_argument(
        "--all", action="store_true", help="Rewrite articles and build the book"
    )

    args = parser.parse_args()

    if args.rewrite or args.all:
        # Loop through existing markdown files and rewrite them
        for file in EXISTING_ARTICLES_PATH.glob(
            "**/*.md"
        ):  # Recursively search for .md files
            if not file.name.endswith("_rewritten.md"):
                print(f"Rewriting article: {file.name}")
                rewrite_article(file)

    if args.build or args.all:
        # Organize topics and build the book
        organize_and_build_book()

    if not (args.rewrite or args.build or args.all):
        print(
            "No action specified. Use --rewrite to rewrite articles, --build to build the book, or --all to do both."
        )
        print("Example: python build.py --all")


def analyze_topics():
    """
    Analyze the topics directory and organize files into a coherent structure.
    Returns a dictionary with categories as keys and lists of files as values.
    """
    print("Analyzing topics and organizing content...")

    # Dictionary to store categories and their files
    categories = defaultdict(list)

    # Find all markdown files (prioritize rewritten versions)
    all_files = list(TOPIC_DIR.glob("**/*.md"))

    # Group files by their parent directory
    for file in all_files:
        # Skip files that are not rewritten versions if a rewritten version exists
        if not file.name.endswith("_rewritten.md"):
            rewritten_version = file.parent / f"{file.stem}_rewritten.md"
            if rewritten_version in all_files:
                continue

        # Use the parent directory as the category
        category = file.parent.name
        if category == "topics":
            # For files directly in the topics directory, try to infer a category
            # from the filename or content
            category = "general"

        categories[category].append(file)

    # Sort files within each category
    for category in categories:
        categories[category].sort(key=lambda x: x.name)

    return categories


def extract_title_from_markdown(file_path):
    """Extract the title from a markdown file."""
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Try to find a markdown title (# Title)
        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()

        # If no title found, use the filename without extension and _rewritten suffix
        filename = file_path.stem
        if filename.endswith("_rewritten"):
            filename = filename[:-10]  # Remove "_rewritten" suffix
        return filename.replace("-", " ").replace("_", " ").title()
    except Exception as e:
        print(f"Error extracting title from {file_path}: {e}")
        return file_path.stem.replace("-", " ").replace("_", " ").title()


def generate_mkdocs_config(categories):
    """
    Generate the MkDocs configuration file based on the organized topics.
    """
    print("Generating MkDocs configuration...")

    # Create the docs directory if it doesn't exist
    DOCS_DIR.mkdir(exist_ok=True)

    # Copy all markdown files to the docs directory with proper structure
    for category, files in categories.items():
        category_dir = DOCS_DIR / category
        category_dir.mkdir(exist_ok=True)

        for file in files:
            # Determine the destination path
            if category == "general":
                dest_path = DOCS_DIR / file.name
            else:
                dest_path = category_dir / file.name

            # Copy the file
            shutil.copy2(file, dest_path)

    # Create index.md if it doesn't exist
    index_path = DOCS_DIR / "index.md"
    if not index_path.exists():
        with open(index_path, "w") as f:
            f.write("# Staff Engineer's Field Guide\n\n")
            f.write(
                "Welcome to the Staff Engineer's Field Guide, a comprehensive resource for senior and staff engineers.\n\n"
            )
            f.write(
                "This book covers a wide range of topics essential for technical leadership, organized into categories for easy navigation.\n\n"
            )
            f.write("## Contents\n\n")

            for category in sorted(categories.keys()):
                if category != "images":  # Skip image directories
                    f.write(f"- [{category.replace('-', ' ').title()}](/{category}/)\n")

    # Create category index files
    for category in categories:
        if category != "images":  # Skip image directories
            category_dir = DOCS_DIR / category
            category_index = category_dir / "index.md"

            if not category_index.exists() and category_dir.exists():
                with open(category_index, "w") as f:
                    f.write(f"# {category.replace('-', ' ').title()}\n\n")
                    f.write(f"Topics related to {category.replace('-', ' ')}.\n\n")

                    for file in categories[category]:
                        title = extract_title_from_markdown(file)
                        relative_path = file.name
                        f.write(f"- [{title}]({relative_path})\n")

    # Generate the MkDocs configuration
    config = {
        "site_name": "Staff Engineer's Field Guide",
        "site_description": "A comprehensive guide for staff engineers and technical leaders",
        "theme": {
            "name": "material",
            "palette": {"primary": "indigo", "accent": "indigo"},
            "features": [
                "navigation.instant",
                "navigation.tracking",
                "navigation.expand",
                "navigation.indexes",
                "toc.integrate",
            ],
        },
        "markdown_extensions": [
            "admonition",
            "codehilite",
            "toc",
            "pymdownx.superfences",
        ],
        "nav": [{"Home": "index.md"}],
    }

    # Add categories to navigation
    for category in sorted(categories.keys()):
        if (
            category != "images" and (DOCS_DIR / category).exists()
        ):  # Skip image directories
            category_files = []

            # Add index file first
            category_files.append({"Overview": f"{category}/index.md"})

            # Add all other files in the category
            for file in sorted(categories[category], key=lambda x: x.name):
                title = extract_title_from_markdown(file)
                relative_path = f"{category}/{file.name}"
                category_files.append({title: relative_path})

            config["nav"].append({category.replace("-", " ").title(): category_files})

    # Write the configuration to mkdocs.yml
    with open("mkdocs.yml", "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

    return config


def build_mkdocs_book():
    """
    Build the MkDocs book.
    """
    print("Building MkDocs book...")

    try:
        # Build the static site
        subprocess.run(["mkdocs", "build", "--clean"], check=True)
        print("MkDocs book built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error building MkDocs book: {e}")
        return False
    except FileNotFoundError:
        print(
            "Error: mkdocs command not found. Please install MkDocs using 'pip install mkdocs mkdocs-material'"
        )
        return False


def organize_and_build_book():
    """
    Organize topics and build the book.
    """
    # Analyze and organize topics
    categories = analyze_topics()

    # Generate MkDocs configuration
    generate_mkdocs_config(categories)

    # Build the book
    build_mkdocs_book()
