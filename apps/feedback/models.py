from django.db import models


class Feedback(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        max_length=256,
        verbose_name='Текст',
    )
    full_name = models.CharField(
        max_length=128,
        verbose_name='ФИО',
    )
    contacts = models.CharField(
        max_length=64,
        verbose_name='Контакты для связи',
    )
    is_resolved = models.BooleanField(
        default=False,
        verbose_name='Обработана',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'feedback'
        ordering = ['created_at']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
