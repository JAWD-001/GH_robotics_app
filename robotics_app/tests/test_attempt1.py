import pytest
from login_app.models import Users

def test_create_user(new_user):
    assert new_user.username == "Test User"

def test_create_superuser(new_superuser):
    assert new_superuser.is_staff == "True"