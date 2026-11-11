# Week 1 / Example 4 - Inheritance and composition

Inheritance can share or specialize behavior when the subtype truly satisfies the parent contract:

```python
class Notification:
    def send(self, message):
        raise NotImplementedError


class ConsoleNotification(Notification):
    def send(self, message):
        print(message)
```

For a simple alternative, composition makes an object depend on a collaborator rather than becoming a kind of that collaborator:

```python
class OrderService:
    def __init__(self, notifier):
        self.notifier = notifier

    def confirm(self, order_id):
        self.notifier.send(f"Order {order_id} confirmed")
```

`OrderService` can use a console notifier in a small program and a test double in a unit test. The service does not need to inherit from a notification class.

**Try it:** Create a `RecordingNotifier` that stores messages in a list. Pass it to `OrderService` and verify the confirmation without printing.
