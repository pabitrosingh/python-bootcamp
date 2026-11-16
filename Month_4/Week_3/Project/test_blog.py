import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from Month_4.Week_3.Project.blog import create_app


class BlogApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temporary_directory.name) / "blog.db"
        self.client = TestClient(create_app(self.database_path))
        self.client.__enter__()

    def tearDown(self) -> None:
        self.client.__exit__(None, None, None)
        self.temporary_directory.cleanup()

    def test_create_list_update_and_delete_post(self):
        created = self.client.post(
            "/posts", json={"title": "First post", "body": "Hello, SQLite"}
        )
        self.assertEqual(created.status_code, 201)
        self.assertEqual(created.json()["title"], "First post")
        post_id = created.json()["id"]

        updated = self.client.put(
            f"/posts/{post_id}",
            json={"title": "Updated post", "body": "Edited body"},
        )
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.json()["body"], "Edited body")
        self.assertEqual(len(self.client.get("/posts").json()), 1)

        deleted = self.client.delete(f"/posts/{post_id}")
        self.assertEqual(deleted.status_code, 204)
        self.assertEqual(self.client.get(f"/posts/{post_id}").status_code, 404)

    def test_post_persists_between_app_instances(self):
        self.client.post("/posts", json={"title": "Persistent", "body": "Stored"})
        self.client.__exit__(None, None, None)
        self.client = TestClient(create_app(self.database_path))
        self.client.__enter__()

        posts = self.client.get("/posts").json()

        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]["title"], "Persistent")

    def test_title_validation_and_missing_post(self):
        response = self.client.post("/posts", json={"title": " ", "body": "body"})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            self.client.put(
                "/posts/42", json={"title": "Missing", "body": "No post"}
            ).status_code,
            404,
        )
        self.assertEqual(self.client.delete("/posts/42").status_code, 404)


if __name__ == "__main__":
    unittest.main()
