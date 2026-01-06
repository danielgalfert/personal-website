from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return ["home", "projects_index", "about", "cv", "contact"]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        from .views import PROJECTS
        return PROJECTS

    def location(self, obj):
        return f"/projects/{obj['slug']}/"
