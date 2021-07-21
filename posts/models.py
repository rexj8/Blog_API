from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add field is saved as the current timestamp when a row is first added to the database,
    # and is therefore perfect for tracking when it was created.

    updated_at = models.DateTimeField(auto_now=True)
    # auto_now fields are updated to the current timestamp every time an object is saved
    # and are therefore perfect for tracking when an object was last modified

    print(title)
    print(content)
    print(created_at)
    print(updated_at)

    def __str__(self):
        print(self.title)
        return self.title