# Exercise 2 - Add useful logs

Add a module-level logger to a small inventory or contact service. Log a successful operation at `INFO` and an unexpected-but-recoverable condition at `WARNING`.

**Test:** Configure logging in the executable entry point, not inside the reusable service module. Confirm the service still raises domain errors for callers to handle.

**Try next:** Include an identifier as contextual information rather than logging the entire record.
