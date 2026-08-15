from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Script(models.Model):
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True) # مثل: phone-lookup
    description = models.TextField()
    code = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='scripts')
    github_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title