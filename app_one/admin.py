from django.contrib import admin
from .models import JobPost, Location, Author, Skill


class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "date", "salary", "slug", "description")
    list_filter = ("date", "salary", "expiry")
    search_fields = ("title",)
    search_help_text = "Write in your query and hit enter!"
    # fields = (("title", "description"), "salary", "expiry")
    # exclude = ("slug",)
    fieldsets = (
        ("Basic Information", {"fields": ("title", "description")}),
        (
            "More Information",
            {
                "fields": (
                    ("salary", "expiry"),
                    # "slug",
                    "location",
                    "author",
                    "skills",
                ),
                # "classes": ("collapse",),
            },
        ),
    )


# Register your models here.
admin.site.register(JobPost, JobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)
