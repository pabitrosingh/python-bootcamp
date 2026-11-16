# Project - Web Scraper

Build a small, single-page scraper that fetches one HTTP(S) page and extracts its title, headings, and links. The project practices `urllib.request`, `html.parser`, timeouts, bounded reads, and unit tests that do not access the network.

The implementation is in [`scraper.py`](./scraper.py); tests are in [`test_scraper.py`](./test_scraper.py).

## Run

From the repository root:

```bash
python -m Month_5.Week_1.Project.scraper --help
python -m Month_5.Week_1.Project.scraper https://docs.python.org/3/
python -m unittest -v Month_5.Week_1.Project.test_scraper
```

The CLI makes a single request to the URL you supply. It accepts only `http` and `https`, uses a request timeout, and reads at most 1 MiB by default. It does not recursively crawl links or bypass access controls. Follow the site owner's terms, robots policy, and rate limits before scraping.

## Acceptance checklist

- [ ] Parse title text, heading text, and links from HTML, including character references.
- [ ] Resolve relative links against the page URL.
- [ ] Reject invalid or unsupported URL schemes.
- [ ] Bound network wait time and downloaded content size.
- [ ] Test parsing and network handling without requiring an external website.

## Extensions

- Add a delay between pages and a maximum page count for a small, polite crawl.
- Add `robots.txt` handling and a cache, following the target site's rules.
- Add CSV or JSON output with the standard library.

## References

- [`html.parser`](https://docs.python.org/3/library/html.parser.html)
- [`urllib.request`](https://docs.python.org/3/library/urllib.request.html)
- [Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
