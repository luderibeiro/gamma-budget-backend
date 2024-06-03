from budget.models.categories import IncomingCategory, RevenueCategory
from rest_framework import serializers


class IncomingCategoryListSerializer(serializers.ModelSerializer):
    """
    Serializer for the IncomingCategory model.

    This serializer handles the conversion of IncomingCategory instances into native
    Python datatypes, and supports all fields of the model.

    Attributes:
    ----------
    Meta : class
        A nested class that defines the model and fields for the serializer.
    """

    class Meta:
        """
        Meta options for IncomingCategoryListSerializer.

        Attributes:
        ----------
        model : IncomingCategory
            The model that the serializer is associated with.
        fields : str
            A string indicating that all fields of the model should be included in the
            serialization.
        """

        model = IncomingCategory
        fields = "__all__"


class RevenueCategoryListSerializer(serializers.ModelSerializer):
    """
    Serializer for the RevenueCategory model.

    This serializer handles the conversion of RevenueCategory instances into native
    Python datatypes, and supports all fields of the model.

    Attributes:
    ----------
    Meta : class
        A nested class that defines the model and fields for the serializer.
    """

    class Meta:
        """
        Meta options for RevenueCategoryListSerializer.

        Attributes:
        ----------
        model : RevenueCategory
            The model that the serializer is associated with.
        fields : str
            A string indicating that all fields of the model should be included in the
            serialization.
        """

        model = RevenueCategory
        fields = "__all__"
