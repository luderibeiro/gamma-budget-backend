from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)

    def validate(self, data):
        """
        Check that has phone number or email and password data.
        """
        if data.get("email", None) != None and data.get("password", None) != None:
            return data

        raise serializers.ValidationError("Define email and password.")
