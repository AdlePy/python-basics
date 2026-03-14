from unittest import TestCase, mock
from db_helper import get_user_by_username, User
from random import choices
from string import ascii_lowercase


class DbHelperTestcase(TestCase):
    @mock.patch("db_helper.get_session", autospec=True)
    def test_get_user_by_username(self, mocked_get_session):
        username = "".join(choices(ascii_lowercase, k=8))
        user = User(username)
        print(f"created user: {user}")

        user_ = get_user_by_username(username)
        print(f"user_: {user_}")
        mocked_get_session.assert_called_once_with()
