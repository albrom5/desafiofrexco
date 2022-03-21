from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth_date = models.DateField()

    def generate_random_password(self):
        password = User.objects.make_random_password()
        return self.set_password(password)

    def save(self, *args, **kwargs):
        if not self.password:
            password = self.generate_random_password()
            self.set_password(password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
