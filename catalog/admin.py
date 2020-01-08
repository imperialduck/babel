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

    radio_fields = {"type_publication": admin.HORIZONTAL}
    readonly_fields = ("reference",)

    fieldsets = (
        ("Référence", {
            # 'readonly_fields': ('reference'),
            'fields': (('dewey_number', 'isbn'), ('type_publication', 'reference')),
        }),
        ("Publication", {
            'fields': ('name', 'author', 'label_editor'),
        }),
        ("Details", {
            'classes': ('collapse',),
            'fields': (('content', 'nb_track_pages'),('image_url', 'image_file')),
        }),
    )


class DeweyAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "name",
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "date_birth",
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Dewey, DeweyAdmin)
admin.site.register(Publication, PublicationAdmin)
