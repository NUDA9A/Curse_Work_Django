from django.db import models

from config.settings import AUTH_USER_MODEL

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(max_length=300, verbose_name="Содержимое")
    image = models.ImageField(upload_to='blogs/', verbose_name="Изображение", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    view_count = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="Владелец", **NULLABLE)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
