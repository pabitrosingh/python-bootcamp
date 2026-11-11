# Exercise 2 - Factory and repository

Create a factory that selects a notification implementation by a supported name, plus a repository that stores records by identifier.

**Test:** Unknown names should raise a clear `ValueError`; a saved record should be retrievable by its identifier.

**Try next:** Keep selection logic out of the service that uses the notification.
