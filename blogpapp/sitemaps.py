from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post
class StaticViewSitemap(Sitemap):
    def items(self):
        return Post.objects.all()