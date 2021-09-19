from django.db import models


from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

User = get_user_model()

RATING_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    text = models.TextField('Текст')
    rating = models.IntegerField('Оценка', choices=RATING_CHOICES)

    class Meta:
        verbose_name = 'Рассмотрение'
        verbose_name_plural = 'Рассмотрения'