from django.db import models

class BlogPost(models.Model):
    # auto generated primary key for each record 
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, default=f'Title', max_length=30)
    content = models.TextField(blank=True, default=f'Content')
