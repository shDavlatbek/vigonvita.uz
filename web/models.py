from django.db import models
from django.utils.translation import gettext_lazy as _

class News(models.Model):
    image = models.ImageField(upload_to='news_images/', help_text=_("1:1 Nisbatdagi rasm yuklang"), verbose_name=_("Rasm"))
    
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    slug = models.SlugField(default="", verbose_name=_("Slug"))
    content = models.TextField(verbose_name=_("Matn"))
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    def __str__(self):
        return self.title


class Medicine(models.Model):
    image = models.ImageField(upload_to='medicine_images/', help_text=_("1:1 Nisbatdagi rasm yuklang"), verbose_name=_("Rasm"))
    name = models.CharField(max_length=200, verbose_name=_("Nomi"))
    description = models.TextField(verbose_name=_("Matn"))

    def __str__(self):
        return self.name