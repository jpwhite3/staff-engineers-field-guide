# Staff Engineer's Field Guide Book Builder

This application builds a comprehensive book from a collection of topics using AI and MkDocs.

## Features

- Reads topics from the "topics" directory
- Uses AI (via Ollama) to expand upon and improve the topics
- Organizes topics into a coherent structure
- Generates a book using MkDocs with a material theme

## Requirements

- Python 3.7+
- Ollama (for AI processing)
- MkDocs and MkDocs Material theme

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure Ollama is installed and running with the llama3.1 model:

```bash
ollama pull llama3.1
```

## Usage

### Rewrite Articles with AI

To rewrite all articles in the topics directory using AI:

```bash
python build.py --rewrite
```

### Build the Book

To build the book without rewriting articles:

```bash
python build.py --build
```

### Rewrite Articles and Build the Book

To rewrite all articles and then build the book:

```bash
python build.py --all
```

## Output

- Rewritten articles are saved in the topics directory with "_rewritten" suffix
- The MkDocs configuration is saved as `mkdocs.yml`
- The built book is available in the `site` directory

## Viewing the Book

After building the book, you can view it by:

1. Serving it locally:

```bash
mkdocs serve
```

2. Then open your browser and navigate to http://localhost:8000

## Project Structure

- `build.py`: Main script for rewriting articles and building the book
- `topics/`: Directory containing all the topic markdown files
- `docs/`: Generated directory containing the organized markdown files for MkDocs
- `site/`: Generated directory containing the built static site
- `mkdocs.yml`: Generated MkDocs configuration file

## How It Works

1. **Article Rewriting**: The script uses Ollama's LLM to rewrite and expand upon the existing markdown files in the topics directory.
2. **Topic Organization**: The script analyzes the topics directory and organizes files into a coherent structure based on their directory location.
3. **MkDocs Configuration**: A configuration file for MkDocs is generated based on the organized topics.
4. **Book Building**: MkDocs is used to build a static site from the organized markdown files.

## Customization

You can customize the book by:

1. Modifying the base prompt in `build.py` to change how articles are rewritten
2. Adding new topics to the topics directory
3. Editing the MkDocs configuration in the `generate_mkdocs_config` function