# Serialization
# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes
# that can then be easily rendered into JSON, XML or other content types.

# Serializers also provide deserialization, allowing parsed data to be converted back into complex types,
# after first validating the incoming data.

from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post

        print(model)

# ----------------------------------------------------------------------------------------------------------------------------------------------

# ModelSerializer ->
# The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class
# with fields that correspond to the Model fields.

# The ModelSerializer class is the same as a regular Serializer class, except that:

# - It will automatically generate a set of fields for you, based on the model.
# - It will automatically generate validators for the serializer, such as unique_together validators.
# - It includes simple default implementations of .create() and .update().

# SYNTAX

# class SerializerName(serializers.ModelSerializer):
# 	class Meta:
# 		model = <ModelName>
# 		fields = <List of Fields>

# ----------------------------------------------------------------------------------------------------------------------------------------------

# META CLASS -> Model Meta is basically the inner class of your model class.

# Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name and lot of other options.
# It’s completely optional to add Meta class in your model.
