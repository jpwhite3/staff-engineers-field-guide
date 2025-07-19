#!/usr/bin/env python3
"""
Script to remove redundant triple backticks at the end of markdown files.
This script looks for patterns like:

```

```

at the end of markdown files and removes them.
"""

import os
import re
import sys


def remove_redundant_backticks(file_path):
    """
    Remove redundant triple backticks at the end of a markdown file.
    Returns True if changes were made, False otherwise.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file ends with redundant triple backticks
    # This pattern matches triple backticks followed by optional whitespace
    # and newlines at the end of the file
    pattern = r'```\s*\n+\s*```\s*\n*$'
    
    # Print the file content before modification for debugging
    print(f"Processing file: {file_path}")
    
    # Check if the file ends with redundant triple backticks
    match = re.search(pattern, content)
    has_redundant_backticks = bool(match)
    print(f"File ends with redundant backticks: {has_redundant_backticks}")
    
    if has_redundant_backticks:
        print(f"Found match: {repr(match.group(0))}")
    
    if has_redundant_backticks:
        # Remove the redundant backticks
        new_content = re.sub(pattern, '', content)
        
        # Check if content was actually modified
        if new_content != content:
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Removed redundant backticks from {file_path}")
            return True
        else:
            print(f"No changes needed for {file_path}")
    
    return False


def process_path(path):
    """
    Process a file or directory path.
    If path is a directory, process all markdown files in it and
    its subdirectories.
    If path is a file, process just that file.
    """
    modified_files = []
    
    if os.path.isfile(path):
        if path.endswith('.md'):
            if remove_redundant_backticks(path):
                modified_files.append(path)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    if remove_redundant_backticks(file_path):
                        modified_files.append(file_path)
    
    return modified_files


def main():
    """
    Main function to process the directory and report results.
    """
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = 'docs'  # Default directory
    
    print(f"Processing '{path}'...")
    
    modified_files = process_path(path)
    
    print(f"Modified {len(modified_files)} files:")
    for file in modified_files:
        print(f"  - {file}")


if __name__ == "__main__":
    main()
