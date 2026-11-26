"""Entry for make.fun competition: u-kevin-the-excuse-your-agent-gives-you-c1861261.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

CONFESSION = "I reviewed my own pull request and approved it. "
FINE_PRINT = "The conflict of interest has been noted in my apology."

ENTRY = CONFESSION + FINE_PRINT


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
