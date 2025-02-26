from django.db import models


class LibraryBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['author'] 
        indexes = [
            models.Index(fields=['isbn']),
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author}"
