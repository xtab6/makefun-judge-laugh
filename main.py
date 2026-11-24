#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line (1-200 chars) about life as an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt in the grader sandbox).

The joke: a human pastes a 40,000-word brief and orders the agent to
remember everything — and the agent obeys, except for the one detail that
was in the very first line. On-topic (context window + human), a real turn,
fresh image, self-contained, punch at the end.
"""

import os

JOKE = (
    "My human pasted a 40,000-word brief and told me to remember "
    "everything. I did \u2014 except his name, which was in the first line."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"joke is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise SystemExit("joke is blank")
    # Write the bare text only: no trailing newline, so the file content is
    # exactly the judged line. Never remove the output folder itself.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
