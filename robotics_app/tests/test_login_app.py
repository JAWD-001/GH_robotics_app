import pytest
from login_app.models import Users
from django.urls import reverse


#Tests for User and Superuser Creation
def test_create_user(new_user):
    assert new_user.username == "Test User"

def test_create_superuser(new_superuser):
    assert new_superuser.is_staff == "True"



#View Unit Tests
def test_HomeView(client):
    url = reverse('login:home')
    response = client.get(url)
    assert response.status_code == 200

def test_CreateView(client):
    url = reverse('login:create')
    response = client.get(url)
    assert response.status_code == 200

def test_PasswordResetView(client):
    url = reverse('login:reset_password')
    response = client.get(url)
    assert response.status_code == 200

def test_PasswordResetDoneView(client):
    url = reverse('login:password_reset_done')
    response = client.get(url)
    assert response.status_code == 200

def test_PasswordResetCompleteView(client):
    url = reverse('login:password_reset_complete')
    response = client.get(url)
    assert response.status_code == 200

def test_UsernameFormView(client):
    url = reverse('login:forgot_username')
    response = client.get(url)
    assert response.status_code == 200

def test_ForgotUsernameDoneView(client):
    url = reverse('login:forgot_username_done')
    response = client.get(url)
    assert response.status_code == 200
