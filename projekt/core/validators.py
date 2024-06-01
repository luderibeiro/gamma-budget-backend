from django.contrib.auth import authenticate
from oauth2_provider.oauth2_validators import OAuth2Validator


class GammaBudgetOAuth2Validator(OAuth2Validator):
    def validate_user(self, username, password, client, request, *args, **kwargs):
        """
        Check username and password correspond to a valid and active User
        """
        user = None
        if user is None:
            user = authenticate(email=username, password=password)
        if user is not None and user.is_active:
            request.user = user
            return True

        return False
