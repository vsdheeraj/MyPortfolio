from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field  

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    github_url = models.URLField(
        "GitHub repository URL",
        max_length=500,
        null=True,
        blank=True,
        help_text="Optional. Example: https://github.com/username/repo",
    )
    body = CKEditor5Field(config_name='extends')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        # Generate slug if not set
        if self.slug is None or self.slug.strip() == "":
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = f"{slugify(self.headline)}-{count}"
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
        

