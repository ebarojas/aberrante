from django.db import models

class Lead(models.Model):
    email = models.CharField(max_length=255)  # Field for user input
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    # What else should i add

    def __str__(self):
        return self.email

# Note to self: research how best to do this.