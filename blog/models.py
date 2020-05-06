from django.db import models

class Blog(models.Model):
    content = models.CharField('本文', max_length=140)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:10]