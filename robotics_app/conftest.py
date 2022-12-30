import pytest
from login_app.models import Users

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
            username: str,
            password: str = None,
            first_name: str = "testfirstname",
            last_name: str = "testlastname",
            email: str = "test.user@testemail.com",
            grad_year: int = 2002,
            is_staff: str = False,
            is_superuser: str = False,
            is_active: str = True,
    ):
        user = Users.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            grad_year=grad_year,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active
        )
        return user
    return create_app_user

@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory('Test User')

@pytest.fixture
def new_superuser(db, new_user_factory):
    return new_user_factory('Test User', is_staff='True')