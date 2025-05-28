from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='home_images/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Домашняя страница"
        verbose_name_plural = "Домашние страницы"

class Testimonial(models.Model):
    name = models.CharField(max_length=100, default='Аноним', verbose_name="Имя")
    position = models.CharField(max_length=100, verbose_name="Должность")
    content = models.TextField(verbose_name="Отзыв")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост блога"
        verbose_name_plural = "Посты блога"

class Contact(models.Model):
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name="Страна")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес")

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
