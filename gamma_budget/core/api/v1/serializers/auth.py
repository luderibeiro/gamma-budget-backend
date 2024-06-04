from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    """
    Serializer for user authentication.

    Validates email and password fields.

    Attributes:
    ----------
        email (EmailField): The email field for user authentication.
        password (CharField): The password field for user authentication.
    """

    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)

    def validate(self, data):
        """
        Validate email and password.

        Args:
        ----
            data (dict): The input data.

        Returns:
        -------
            dict: The validated data.

        Raises:
        ------
            serializers.ValidationError: If email and password are not provided.
        """
        if data.get("email", None) is not None and data.get("password", None) is not None:
            return data

        raise serializers.ValidationError("Define email and password.")
