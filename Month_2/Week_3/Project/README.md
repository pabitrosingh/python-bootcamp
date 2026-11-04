# Project - File Analyzer

Build a command-line tool that reads a UTF-8 text file and reports the number of characters, logical lines, words, and most frequent words. This is the Month 2 roadmap's File Analyzer project.

The runnable reference implementation is [`file_analyzer.py`](./file_analyzer.py), with acceptance tests in [`test_file_analyzer.py`](./test_file_analyzer.py).

## Run

From the repository root:

```bash
python -m Month_2.Week_3.Project.file_analyzer path/to/notes.txt
```

Or from this directory:

```bash
python file_analyzer.py path/to/notes.txt
```

Run the automated tests from the repository root:

```bash
python -m unittest -v Month_2.Week_3.Project.test_file_analyzer
```

The analyzer does not modify the input file. It reports file-system and UTF-8 decoding errors to standard error and exits with a non-zero status.

## Definitions used

- **Characters:** `len(text)`, including whitespace and newline characters.
- **Lines:** `len(text.splitlines())`; an empty file has zero lines, and a final newline does not create an extra logical line.
- **Words:** whitespace-separated tokens after stripping surrounding punctuation and case-folding.
- **Most frequent:** up to five words, ordered by descending count and then alphabetically for ties.

## Acceptance checklist

- [ ] Empty files and files with only whitespace are handled.
- [ ] Punctuation and capitalization do not create separate counts for the same word.
- [ ] Missing files and invalid UTF-8 are reported explicitly.
- [ ] The source file remains unchanged.
- [ ] The tests pass.

## Extensions

- Add a `--top N` argument.
- Add a CSV report using the `csv` module.
- Add a recursive directory mode, skipping directories the user cannot read with a clear error report.
