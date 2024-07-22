from django.db import models
import uuid

# Create your models here.

class LinkSubmission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.link

class ScrapedData(models.Model):
    link_submission = models.ForeignKey(LinkSubmission, on_delete=models.CASCADE, related_name='scraped_data')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=200, blank=False)
    value = models.CharField(max_length=500, blank=False)


    def __str__(self):
        return str(self.id)