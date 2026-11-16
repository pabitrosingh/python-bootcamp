"""Fetch one web page and extract a small set of useful fields."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html.parser import HTMLParser
import logging
from urllib.error import URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen


logger = logging.getLogger(__name__)
DEFAULT_TIMEOUT = 10.0
DEFAULT_MAX_BYTES = 1_048_576
USER_AGENT = "PythonBootcampEducationalScraper/1.0"


@dataclass(frozen=True)
class ScrapedPage:
    """Fields extracted from one HTML document."""

    url: str
    title: str
    headings: tuple[str, ...]
    links: tuple[str, ...]


class _PageParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.title_parts: list[str] = []
        self.headings: list[str] = []
        self.links: list[str] = []
        self._in_title = False
        self._heading_tag: str | None = None
        self._heading_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self._in_title = True
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._heading_tag = tag
            self._heading_parts = []
        elif tag == "a":
            href = next((value for name, value in attrs if name == "href"), None)
            if href:
                self.links.append(urljoin(self.base_url, href))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == self._heading_tag:
            heading = " ".join("".join(self._heading_parts).split())
            if heading:
                self.headings.append(heading)
            self._heading_tag = None
            self._heading_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._heading_tag is not None:
            self._heading_parts.append(data)


def _validate_url(url: str) -> str:
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        raise ValueError("url must be an absolute http or https URL")
    return url


def parse_html(html: str, url: str) -> ScrapedPage:
    """Extract a page title, headings, and absolute links from HTML text."""
    page_url = _validate_url(url)
    parser = _PageParser(page_url)
    parser.feed(html)
    parser.close()
    title = " ".join("".join(parser.title_parts).split())
    return ScrapedPage(
        url=page_url,
        title=title,
        headings=tuple(parser.headings),
        links=tuple(parser.links),
    )


def fetch_page(
    url: str,
    *,
    timeout: float = DEFAULT_TIMEOUT,
    max_bytes: int = DEFAULT_MAX_BYTES,
) -> ScrapedPage:
    """Fetch one bounded HTML response and parse it."""
    page_url = _validate_url(url)
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    if max_bytes <= 0:
        raise ValueError("max_bytes must be positive")

    request = Request(page_url, headers={"User-Agent": USER_AGENT})
    logger.info("Fetching %s", page_url)
    with urlopen(request, timeout=timeout) as response:
        content = response.read(max_bytes + 1)
        response_url = response.geturl()
        charset = response.headers.get_content_charset() or "utf-8"
    if len(content) > max_bytes:
        raise ValueError(f"response exceeds the {max_bytes}-byte limit")
    html = content.decode(charset, errors="replace")
    return parse_html(html, response_url)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="absolute http or https URL to fetch")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    try:
        page = fetch_page(args.url, timeout=args.timeout, max_bytes=args.max_bytes)
    except (ValueError, URLError, OSError) as error:
        parser.error(str(error))

    print(f"URL: {page.url}")
    print(f"Title: {page.title}")
    print("Headings:")
    for heading in page.headings:
        print(f"- {heading}")
    print("Links:")
    for link in page.links:
        print(f"- {link}")


if __name__ == "__main__":
    main()
