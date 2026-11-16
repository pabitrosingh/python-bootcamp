import unittest

from fastapi.testclient import TestClient

from Month_4.Week_2.Project.task_api import create_app


class TaskApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(create_app())

    def tearDown(self) -> None:
        self.client.close()

    def test_create_list_filter_update_and_delete_task(self):
        created = self.client.post(
            "/tasks", json={"title": "  Write tests  ", "description": "API"}
        )
        self.assertEqual(created.status_code, 201)
        self.assertEqual(
            created.json(),
            {
                "id": 1,
                "title": "Write tests",
                "description": "API",
                "completed": False,
            },
        )

        updated = self.client.patch("/tasks/1", json={"completed": True})
        self.assertEqual(updated.status_code, 200)
        self.assertTrue(updated.json()["completed"])
        self.assertEqual(self.client.get("/tasks?completed=true").json(), [updated.json()])
        self.assertEqual(self.client.get("/tasks?completed=false").json(), [])

        deleted = self.client.delete("/tasks/1")
        self.assertEqual(deleted.status_code, 204)
        self.assertEqual(self.client.get("/tasks/1").status_code, 404)

    def test_validation_rejects_blank_title_and_empty_patch(self):
        response = self.client.post("/tasks", json={"title": "  "})
        self.assertEqual(response.status_code, 422)

        self.client.post("/tasks", json={"title": "Valid"})
        response = self.client.patch("/tasks/1", json={})
        self.assertEqual(response.status_code, 422)

    def test_missing_task_returns_404_for_read_update_and_delete(self):
        self.assertEqual(self.client.get("/tasks/99").status_code, 404)
        self.assertEqual(
            self.client.patch("/tasks/99", json={"completed": True}).status_code,
            404,
        )
        self.assertEqual(self.client.delete("/tasks/99").status_code, 404)

    def test_null_fields_are_not_accepted_in_patch(self):
        self.client.post("/tasks", json={"title": "Valid"})
        response = self.client.patch("/tasks/1", json={"title": None})
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
