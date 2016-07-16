from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model. No changes to attributes over the default."""

    def get_short_name(self):
        """Return the user's username."""
        return self.username

    def get_long_name(self):
        """Return the user's username."""
        return self.username
