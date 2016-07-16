"""Tests for the User model."""

from django.contrib.auth import get_user_model

import pytest


@pytest.fixture(scope='module')
def user():
    """Create a user to test with."""
    return get_user_model().objects.create_user(username='Test', password='correcthorsebatterystaple')


@pytest.mark.django_db
def test_get_short_name(user):
    """Test a user's short name is their username."""
    assert user.get_short_name() == 'Test'


@pytest.mark.django_db
def test_get_long_name(user):
    """Test a user's long name is their username."""
    assert user.get_long_name() == 'Test'
