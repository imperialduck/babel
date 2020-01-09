from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext as _
from .utils import get_century

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True, verbose_name=_("Prénom"),)
    last_name = models.CharField(max_length=30, verbose_name=_("Nom de famille"),)
    name = models.CharField(max_length=61, editable=False)
    century_birth = models.IntegerField(null=True, blank=True, editable=False, verbose_name=_("Siècle"),)
    date_birth = models.DateField(null=True, blank=True, verbose_name=_("Date de naissance"),)
    place_birth = models.CharField(max_length=50, blank=True, verbose_name=_("Lieu de naissance"),)

    date_died = models.DateField(null=True, blank=True, verbose_name=_("Date de décès"),)
    place_died = models.CharField(max_length=50, blank=True, verbose_name=_("Lieu de décès"),)

    content = models.TextField(blank=True, verbose_name=_("Contenu"),)
    image_url = models.URLField(null=True, blank=True, verbose_name=_("Adresse de l'image"),)
    image_file = models.ImageField(null=True, blank=True, verbose_name=_("Fichier image"),)

    class Meta:
        ordering = ['last_name']

    def clean(self):
        get_century(self.date_birth)

    def __str__(self):
        if self.first_name:
            return f"{self.last_name} {self.first_name}"
        else:
            return self.last_name


class Dewey(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField()
    bg_color = models.CharField(max_length=7, default="*")
    text_color = models.CharField(max_length=7, default="*")

    BG_COLOR_CHOICES = [
        ("#000000", "black"),  # Black 000
        ("#8B4513", "maroon"),  # Maroon 100
        ("#FF0000", "red"),  # Red 200
        ("#FF4500", "orange"),  # Orange 300
        ("#FFFF00", "yellow"),  # Yellow 400
        ("#32CD32", "green"),  # Green 500
        ("#1E90FF", "blue"),  # Blue 600
        ("#8B008B", "purple"),  # Purple 700
        ("#A9A9A9", "grey"),  # Grey 800
        ("#FFFFFF", "white"),  # White 900
    ]

    TEXT_COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
    ]

    class Meta:
        ordering = ["number"]

    def __str__(self):
        if self.number == 0:
            return f"000 - {self.name}"
        else:
            return f"{self.number} - {self.name}"

    def colored_number(self):
        for i in range(0, len(self.BG_COLOR_CHOICES)):
            if str(self.number)[:1] == str(i):
                print('0******************')
                self.bg_color = self.BG_COLOR_CHOICES[i][0]
            if str(self.number)[:1] == '0' or str(self.number)[:1] == '1' or str(self.number)[:1] == '2' or str(self.number)[:1] == '3' or str(self.number)[:1] == '7':
                self.text_color = self.TEXT_COLOR_CHOICES[0][0]
            elif str(self.number)[:1] == '9':
                self.text_color = self.TEXT_COLOR_CHOICES[1][0]
        return format_html(
            '<span style="background-color: {}; color: {}; display: inline-block; min-width: 50px;">&nbsp;{}&nbsp;</span>',
            self.bg_color,
            self.text_color,
            self.name,
        )


class Publication(models.Model):
    TYPE_PUBLICATION_CHOICES = [
        ("B", "Livre"),
        ("M", "Musique"),
        ("F", "Film"),
        ("_", "Autre"),
    ]

    name = models.CharField(max_length=61, verbose_name=_("Libellé"),)
    reference = models.CharField(max_length=61, editable=False, verbose_name=_("Référence"),)
    type_publication = models.CharField(max_length=1, choices=TYPE_PUBLICATION_CHOICES, default="B", verbose_name=_("Type de publication"),)
    genre = models.CharField(max_length=50, verbose_name=_("Genre"),)

    author = models.ForeignKey(Author, models.PROTECT, null=True, verbose_name=_("Auteur"),)
    dewey_number = models.ForeignKey(Dewey, models.PROTECT, null=True, verbose_name=_("Nombre Dewey"),)

    date_publication = models.DateField(null=True, blank=True, verbose_name=_("Date de publication"),)
    label_editor = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Label / Editeur"),)
    isbn = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("ISBN"),)

    nb_track_pages = models.IntegerField(null=True, blank=True, verbose_name=_("Nombre de pistes / pages"),)
    content = models.TextField(null=True, blank=True, verbose_name=_("Contenu"),)
    image_url = models.URLField(null=True, blank=True, verbose_name=_("Adresse de l'image"),)
    image_file = models.ImageField(null=True, blank=True, verbose_name=_("Fichier image"),)

    def __str__(self):
        return self.name 

    def clean(self):
        if self.dewey_number and self.author:
            if self.dewey_number.number == 0:
                self.reference = f"000.{self.author.last_name[:3].upper()}.{self.pk}"
            else:
                self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = f"ENATTENTE.{self.pk}"
