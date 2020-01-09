from django.contrib import admin
from django.utils.translation import gettext as _
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
    autocomplete_fields = ("author",)

    fieldsets = (
        (_("Référence"), {
            # 'readonly_fields': ('reference'),
            'fields': (('dewey_number', 'isbn'), ('type_publication', 'reference')),
        }),
        (_("Publication"), {
            'fields': ('name', 'author', 'label_editor'),
        }),
        (_("Détails"), {
            'classes': ('collapse',),
            'fields': (('content', 'nb_track_pages'),('image_url', 'image_file')),
        }),
    )


class DeweyAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "name",
        "colored_number"
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "date_birth",
        "century_birth",
    )

    readonly_fields = ("century_birth"),
    search_fields = ("last_name", "first_name",)
    list_filter = ("century_birth", )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Dewey, DeweyAdmin)
admin.site.register(Publication, PublicationAdmin)
