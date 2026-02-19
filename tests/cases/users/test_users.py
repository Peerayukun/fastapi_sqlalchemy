from tests import BaseTestCase
from app.users.repository import UserRepository

class TestUserAPI(BaseTestCase):

    def test_create_user(self):
        response = self.client.post(
            "/users",
            json={
                "username": "john",
                "email": "john@example.com"
            }
        )

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["username"], "john")

    def test_list_users(self):
        repo = UserRepository(self.db)

        repo.create(
            username="alice",
            email="alice@example.com"
        )

        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data["users"]), 1)
        self.assertEqual(data["users"][0]["username"], "alice")