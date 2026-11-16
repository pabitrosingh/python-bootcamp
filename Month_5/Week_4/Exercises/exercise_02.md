# Exercise 2 - Add useful logs

Add a module-level logger to a small batch-processing script.

Requirements:

- Configure logging in the CLI entry point, not at import time.
- Log a useful summary at `INFO` level.
- Include exception context when reporting a failure and re-raise errors the caller cannot recover from.
- Keep normal, user-facing output separate from diagnostics.
