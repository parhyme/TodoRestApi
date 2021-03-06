from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class Todo(models.Model):
    text = models.CharField(max_length=200, null=True)
    isChecked = models.BooleanField(default=False)
    userId = models.IntegerField(null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.text
