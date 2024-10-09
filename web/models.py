from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class News(models.Model):
    image = models.ImageField(upload_to='assets/images/news_images/', help_text=_("1:1 Nisbatdagi rasm yuklang"), verbose_name=_("Rasm"))
    
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    slug = models.SlugField(default="", verbose_name=_("Qisqa link"))
    content = models.TextField(verbose_name=_("Matn"))
    views = models.IntegerField(default=0, verbose_name=_("Ko'rishlar soni"))
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = _("Yangiliklar")
        verbose_name_plural = _("Yangiliklar")

class Medicine(models.Model):
    image = models.ImageField(upload_to='assets/images/medicine_images/', help_text=_("1:1 Nisbatdagi rasm yuklang"), verbose_name=_("Rasm"))
    name = models.CharField(max_length=200, verbose_name=_("Nomi"))
    description = models.TextField(verbose_name=_("Matn"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Dorilar")
        verbose_name_plural = _("Dorilar")