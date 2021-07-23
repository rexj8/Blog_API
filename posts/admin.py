from django.contrib import admin

from .models import Post

# Enables POST Section on /admin portal
admin.site.register(Post)

