from django.db import models


class PageCrawl(models.Model):
    page_id = models.AutoField(primary_key=True)
    page_url = models.CharField(max_length=250)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.info


class SearchItem(models.Model):
    price = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    pic = models.CharField(max_length=250)

    def __str__(self):
        return self.title