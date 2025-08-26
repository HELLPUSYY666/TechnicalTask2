from django.db import models


class User(models.Model):
    """
    Пример модели для пользователей в ERP.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
