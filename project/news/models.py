from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='default name')
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('MainText')
    date = models.DateTimeField('Data published')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    # Table name in admin panel
    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
