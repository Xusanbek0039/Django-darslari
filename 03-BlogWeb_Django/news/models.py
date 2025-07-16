from django.db import models  # Django model klasslari uchun
from django.utils.html import format_html  # (ixtiyoriy) admin panelda rasmni ko‘rsatish uchun

# Post nomli model (jadval) yaratilmoqda
class Post(models.Model):
    title = models.CharField(
        max_length=150
    )  # Sarlavha uchun - 150 belgigacha matn

    text = models.TextField()  # Asosiy matn uchun - katta hajmdagi matn

    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True
    )  # Rasm uchun - media/post_images/ ichiga saqlanadi, majburiy emas

    def __str__(self):
        return self.title  # Obyekt matni sifatida sarlavha chiqadi

    # (ixtiyoriy) Admin panelda rasmni ko‘rsatish uchun
    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" width="100"/>', self.image.url)
        return "Rasm yo'q"

    image_tag.short_description = 'Rasm'
