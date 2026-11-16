import unittest
from email.message import Message
from io import BytesIO
from unittest.mock import patch
from urllib.error import URLError

from Month_5.Week_1.Project.scraper import (
    DEFAULT_MAX_BYTES,
    USER_AGENT,
    fetch_page,
    parse_html,
)


class ScraperTests(unittest.TestCase):
    def test_parse_html_extracts_text_and_resolves_links(self):
        page = parse_html(
            """
            <html><head><title> A &amp; B </title></head>
            <body><h1>Python <em>tutorial</em></h1>
            <a href="/guide">Guide</a><a href="https://example.com/x">External</a>
            </body></html>
            """,
            "https://example.com/start",
        )

        self.assertEqual(page.title, "A & B")
        self.assertEqual(page.headings, ("Python tutorial",))
        self.assertEqual(
            page.links,
            ("https://example.com/guide", "https://example.com/x"),
        )

    def test_parse_html_rejects_non_http_urls(self):
        for url in ("file:///tmp/page.html", "/relative/path", "ftp://example.com"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                parse_html("<title>x</title>", url)

    def test_fetch_page_uses_timeout_user_agent_and_size_limit(self):
        response = BytesIO(b"<title>Local test</title>")
        response.headers = Message()
        response.headers["Content-Type"] = "text/html; charset=utf-8"
        response.geturl = lambda: "https://example.com/"  # type: ignore[attr-defined]
        with patch(
            "Month_5.Week_1.Project.scraper.urlopen",
            return_value=response,
        ) as open_url:
            page = fetch_page("https://example.com/", timeout=3, max_bytes=100)

        self.assertEqual(page.title, "Local test")
        request = open_url.call_args.args[0]
        self.assertEqual(request.get_header("User-agent"), USER_AGENT)
        self.assertEqual(open_url.call_args.kwargs["timeout"], 3)

    def test_fetch_page_rejects_oversized_response(self):
        response = BytesIO(b"x" * (DEFAULT_MAX_BYTES + 1))
        response.headers = Message()
        response.geturl = lambda: "https://example.com/"  # type: ignore[attr-defined]
        with patch(
            "Month_5.Week_1.Project.scraper.urlopen",
            return_value=response,
        ), self.assertRaisesRegex(ValueError, "exceeds"):
            fetch_page("https://example.com/")

    def test_fetch_page_validates_limits_before_request(self):
        with patch("Month_5.Week_1.Project.scraper.urlopen") as open_url:
            for timeout, max_bytes in ((0, 100), (1, 0)):
                with self.subTest(timeout=timeout, max_bytes=max_bytes):
                    with self.assertRaises(ValueError):
                        fetch_page(
                            "https://example.com/",
                            timeout=timeout,
                            max_bytes=max_bytes,
                        )
        open_url.assert_not_called()

    def test_network_errors_are_not_hidden(self):
        with patch(
            "Month_5.Week_1.Project.scraper.urlopen",
            side_effect=URLError("offline"),
        ):
            with self.assertRaises(URLError):
                fetch_page("https://example.com/")


if __name__ == "__main__":
    unittest.main()
