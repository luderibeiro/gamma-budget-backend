from django.contrib.auth import authenticate
from oauth2_provider.oauth2_validators import OAuth2Validator


class GammaBudgetOAuth2Validator(OAuth2Validator):
    """
    Custom OAuth2 validator for Gamma Budget application.

    This validator extends the OAuth2Validator provided by OAuth Toolkit.

    Attributes:
    ----------
        None
    """

    def validate_user(self, username, password, client, request, *args, **kwargs):
        """
        Validate the user credentials.

        Args:
        ----
            username (str): The username (email) of the user.
            password (str): The password of the user.
            client: The OAuth2 client.
            request: The request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
        -------
            bool: True if the user credentials are valid and the user is active, False otherwise.
        """
        user = None
        if user is None:
            user = authenticate(email=username, password=password)
        if user is not None and user.is_active:
            request.user = user
            return True

        return False
