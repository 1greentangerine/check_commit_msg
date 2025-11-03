import sys
from pathlib import Path


ERROR_MESSAGE = """ERROR: Commit message must start with a valid conventional commit type:

Version Bump Triggers:
  - fix: Bug fixes (patch version bump)
  - feat: New features (minor version bump)
  - BREAKING CHANGE: Breaking changes (major version bump)
  - perf: Performance improvements (patch version bump by default)
    
No Version Bump:
  - docs: Documentation only changes
  - style: Code style changes (formatting, missing semicolons, etc.)
  - refactor: Code refactoring without fixing bugs or adding features
  - test: Adding or updating tests
  - build: Changes to build system or dependencies
  - ci: CI/CD changes
  - chore: Other changes that don't modify src or test files
  - revert: Reverting previous commits

Your commit message: {commit_msg}
"""


def main():
    commit_msg_file = Path(sys.argv[1])

    # Read the commit message
    message = commit_msg_file.read_text().strip()
    options = [
        "fix",
        "feat",
        "docs",
        "style",
        "refactor",
        "perf",
        "test",
        "build",
        "ci",
        "chore",
        "revert",
        "BREAKING CHANGE"
    ]

    if any((message.startswith(f"{prefix.lower()}:") for prefix in options)):
        # good commit
        sys.exit(0)
        
    print(ERROR_MESSAGE.format(commit_msg=message))
    sys.exit(1)
        

if __name__ == "__main__":
    main()
