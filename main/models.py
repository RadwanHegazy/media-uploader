from typing import Any
from django.db import models
from users.models import User


class File (models.Model) : 
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    file_data = models.TextField(editable=False)
    uuid = models.UUIDField()

    def __str__(self) : 
        return f"{self.name}"
    