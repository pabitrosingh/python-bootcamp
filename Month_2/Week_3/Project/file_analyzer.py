"""Analyze word and line statistics in a UTF-8 text file."""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


WORD_PATTERN = re.compile(r"[\w]+(?:['’-][\w]+)*", re.UNICODE)


def analyze_text(text, top_n=5):
    if top_n < 0:
        raise ValueError("top_n must be non-negative.")

    words = [match.group().casefold() for match in WORD_PATTERN.finditer(text)]
    frequencies = Counter(words)
    top_words = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))[:top_n]
    return {
        "character_count": len(text),
        "line_count": len(text.splitlines()),
        "word_count": len(words),
        "top_words": top_words,
    }


def analyze_file(path, top_n=5):
    text = Path(path).read_text(encoding="utf-8")
    return analyze_text(text, top_n=top_n)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Count characters, lines, and words in a UTF-8 text file.")
    parser.add_argument("path", type=Path, help="path to the text file to analyze")
    parser.add_argument("--top", type=int, default=5, help="number of frequent words to display (default: 5)")
    args = parser.parse_args(argv)

    try:
        report = analyze_file(args.path, top_n=args.top)
    except (OSError, UnicodeDecodeError, ValueError) as error:
        print(f"Could not analyze {args.path}: {error}", file=sys.stderr)
        return 1

    print(f"Characters: {report['character_count']}")
    print(f"Lines: {report['line_count']}")
    print(f"Words: {report['word_count']}")
    print("Most frequent words:")
    for word, count in report["top_words"]:
        print(f"  {word}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
