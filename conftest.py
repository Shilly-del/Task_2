import pytest
from apios.user import User


@pytest.fixture()
def user():

    user = User()
    user.register_user()
    yield user

    user.clear()


@pytest.fixture(scope='class')
def user():

    user = User()
    user.register_user()
    yield user

    user.clear()


@pytest.fixture(scope='class')
def user_class():

    user = User()
    user.register_user()
    user.logout()
    yield user

    user.clear()
