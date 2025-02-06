Todo:

- dbase structure
- off white theme

Srces:
- https://patorjk.com/software/taag/#p=display&f=Ogre&t=aberrante

from django.db import models
from django.contrib.auth.models import AbstractUser

## Extend Django's built-in User model to handle both artists and collectors
class User(AbstractUser):
    USER_TYPES = [
        ('artist', 'Artist'),
        ('collector', 'Collector'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

# Artist profile (extends User)
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist_profile')
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Artwork details
class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='artworks/')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Collector profile (extends User)
class Collector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='collector_profile')
    preferences = models.JSONField(blank=True, null=True)  # Stores preferred styles, artists, etc.
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Many-to-Many relationship for favorites (Collectors can favorite Artists or Artworks)
class Favorite(models.Model):
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name='favorites')
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, blank=True, null=True, related_name='favorited_by')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name='favorited_by')

    class Meta:
        unique_together = ('collector', 'artwork', 'artist')  # Prevent duplicate favorites

# Sales table for tracking purchases
class Sale(models.Model):
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name='purchases')
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='sold_artworks')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.collector.user.username} bought {self.artwork.title}"

# Notifications for updates about favorited artists
class Notification(models.Model):
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE, related_name='notifications')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.collector.user.username}"