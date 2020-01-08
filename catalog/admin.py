from django.contrib import admin
from .models import Author, Dewey, Publication

# Register your models here.


class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "reference",
        "type_publication",
        "genre",
        "author",
        "dewey_number",
        "date_publication",
        "label_editor",
    )

    fieldsets = (
        (None, {
            'fields': ('',)
        }),
    )


admin.site.register(Author)
admin.site.register(Dewey)
admin.site.register(Publication, PublicationAdmin)
