from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

from server.settings import EMAIL_HOST_USER
from mail.models import Subscriber

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    cat = models.ForeignKey('Category', verbose_name='Кателогия', on_delete=models.CASCADE)
    date_creation = models.DateField('Дата создания', auto_now_add=True)
    date_last_modifed = models.DateTimeField('Время последнего изменения', auto_now=True)
    preview = models.ImageField('Превью', upload_to='images/')
    image = models.ImageField('Изображение', upload_to='images/')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return f'{self.title} | {self.cat}'

@receiver(post_save, sender=Post)
def create_post(sender, instance, created, **kwargs):
    if created:
        html_content = f"""
        <h1>На сайте blog-light была добавлена новая статья</h1>
        <a href="http://localhost:3000/posts/${instance.id}">
            <h2>{instance.title}</h2>
        </a>
        <p>Категория: <mark>{instance.cat}</mark></p>
        """
        text_content =f"""
        На сайте blog-light была добавлена новая статья \n
        {instance.title} \n
        http://localhost:3000/posts/${instance.id} \n
        Категория: {instance.cat}
        """

        subscribers = Subscriber.objects.all()
        subscribers = [subscribe.email for subscribe in subscribers]

        mail = EmailMultiAlternatives('Новая статья', text_content, EMAIL_HOST_USER, subscribers)
        mail.attach_alternative(html_content, 'text/html')
        mail.send()
        

class Category(models.Model):
    name = models.CharField('Название категории', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name
