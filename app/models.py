from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='тема',
        help_text='тема вашего текста')

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(
        max_length=200,
        verbose_name='имя')

    def __str__(self):
        return self.full_name


class Note(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='имя')
    summary = models.TextField(
        verbose_name='текст')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='тема')
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        verbose_name='автор')
    created_at = models.DateTimeField(
        auto_now_add=True)
    photo = models.ImageField(
        upload_to='media/images/posts',
        verbose_name='картинки',
        help_text='вдохновляющие картины',
        null=True,
        blank=True
    )
    song = models.FileField(
        verbose_name='Звук',
        upload_to='media/song/posts',
        help_text='музыка',
        null=True,
        blank=True
    )
    video = models.FileField(
        verbose_name='Видео',
        upload_to='media/videos/posts',
        null=True,
        blank=True
    )
