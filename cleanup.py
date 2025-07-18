from pathlib import Path

TOPICS_DIR = Path("topics")
REWRITTEN_FILE_SUFFIX = "_rewritten.md"
REWRITTEN_FILE_GLOB = f"**/*{REWRITTEN_FILE_SUFFIX}"
REWRITTEN_FILES = [f for f in TOPICS_DIR.glob(REWRITTEN_FILE_GLOB) if f.is_file()]

for f in REWRITTEN_FILES:
    original_file = Path(str(f).replace(REWRITTEN_FILE_SUFFIX, ".md"))
    if original_file.is_file():
        print(f"Deleting {original_file} ...")
