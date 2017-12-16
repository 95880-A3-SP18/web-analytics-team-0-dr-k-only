from django.db import models


class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)

    def __str__(self):
        return self.item_text
