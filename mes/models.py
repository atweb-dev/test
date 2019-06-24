from django.db import models

# Create your models here.


class Mesa(models.Model):
    sender = models.EmailField()
    message = models.CharField(max_length=250, help_text="message")

    class Meta:
        ordering = ["sender", "message"]

    def __str__(self):
        return self.message
