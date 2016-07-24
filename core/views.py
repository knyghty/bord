from django.views import generic


class HomeView(generic.TemplateView):
    """Home page."""

    # TODO: For now we just show a different template, but in future we need to do some logic:
    # If user is not logged in, we just show the template with links to login and register.
    # Otherwise:
    # If user is rekt, redirect to rekt page.
    # Redirect to the page the user was last on. We need to track this somehow. User flags?

    def get_template_names(self):
        """If not logged in, show the login/register menu, otherwise the colour test."""
        if self.request.user.is_authenticated():
            return 'core/home_logged_in.html'
        return 'core/home_not_logged_in.html'
