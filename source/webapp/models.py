from django.contrib.auth import get_user_model
from django.db import models

class Photo(models.Model):
    photo = models.ImageField(null=False, blank=False, upload_to='user_pics', verbose_name='Фото')
    sign = models.CharField(max_length=200, null=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, verbose_name="Автор")


    def __str__(self):
        return "{}. {}".format(self.photo, self.sign)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
#
#
class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='add_favorite', verbose_name='Пользователь')
    photo = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE,
                                related_name='favorites', verbose_name='Избранное')

    def __str__(self):
        return f'{self.user.username} - {self.photo.photo}'

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

