#!/usr/bin/env python3
"""
Parse git commit history into structured JSON format.

Extracts commit metadata and custom tags ([Why], [What], [Impact])
from commit messages into a flat, token-efficient JSON structure.

Usage:
    python get_commits.py [limit]
    python get_commits.py 20  # Last 20 commits
    python get_commits.py     # Defaults to 50 commits
"""

import subprocess
import json
import re
import sys


def get_git_log(limit=50):
    """
    Extract commits with format:
    hash|date|subject
    body
    <COMMIT_END>
    """
    sep = "<COMMIT_END>"
    fmt = f"%h|%as|%s%n%b{sep}"

    try:
        result = subprocess.run(
            ["git", "log", f"-n{limit}", f"--pretty=format:{fmt}",
             "--no-merges"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        return []
    except FileNotFoundError:
        print("Error: git not found", file=sys.stderr)
        return []

    commits = []
    title_re = re.compile(r'^(\w+)(?:\(([^)]+)\))?:\s*(.+)$')
    tag_re = re.compile(
        r'\[(Why|What|Impact)\]:\s*(.*?)(?=\n\[(?:Why|What|Impact)\]:|$)',
        re.DOTALL | re.IGNORECASE
    )

    for chunk in result.stdout.split(sep):
        chunk = chunk.strip()
        if not chunk:
            continue

        lines = chunk.split('\n', 1)
        metadata = lines[0].split('|', 2)

        if len(metadata) < 3:
            continue

        commit_hash, date, title = metadata
        body = lines[1] if len(lines) > 1 else ""

        # Parse title
        match = title_re.match(title)
        if match:
            ctype, scope, clean_title = match.groups()
        else:
            ctype, scope, clean_title = "other", None, title

        # Extract tags
        tags = {m.group(1).lower(): m.group(2).strip()
                for m in tag_re.finditer(body)}

        commits.append({
            "hash": commit_hash,
            "date": date,
            "type": ctype.lower(),
            "scope": scope or "",
            "title": clean_title,
            "why": tags.get("why", ""),
            "what": tags.get("what", ""),
            "impact": tags.get("impact", "")
        })

    return commits


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    commits = get_git_log(limit)
    print(json.dumps(commits, ensure_ascii=False, separators=(',', ':')))
