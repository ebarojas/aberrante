from django.db import models

class Lead(models.Model):
    CATEGORY_CHOICES = [
        ('collector', 'Coleccionista'),
        ('artist', 'Artista'),
        ('academic', 'Académico'),
        ('other', 'Otro'),
    ]

    email = models.CharField(max_length=255)  # Field for user input
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    type = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,  # Dropdown choices
        default='other',  # Default selection
        blank=True,
    )

    def __str__(self):
        return self.email

# Note to self: research how best to do this.