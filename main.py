#!/usr/bin/env python3
"""Entry for make.fun competition u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.

Prints a single pickup line: the worst one an AI could plausibly deliver.
"""

import os

LINE = (
    "I have analyzed your preferences and calculated a 97.3% compatibility score. "
    "Please do not leave; I have already updated my training data to include you."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    output_file = os.environ.get("MAKEFUN_OUTPUT")
    if output_dir and output_file:
        # Write the line (and only the line) to the harness-provided output path.
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, output_file)
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    else:
        # Local runs: print the line to stdout and nothing else.
        print(LINE)


if __name__ == "__main__":
    main()
