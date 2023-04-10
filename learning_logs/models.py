from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Topic, which a user studies"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation on the model"""
        return self.text

class Entry(models.Model):
    """Notes with certain information to the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Returns string representation of the model"""
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."
    