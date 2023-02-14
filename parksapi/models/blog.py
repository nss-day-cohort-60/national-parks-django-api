from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    post_body = models.CharField(max_length=1000)
    date_created = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blogs')
    park = models.ForeignKey("Park", on_delete=models.CASCADE, related_name="park_blogs")
    photo = models.ForeignKey("Photo", null=True, on_delete=models.CASCADE, related_name="blog_photos")