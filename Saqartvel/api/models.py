from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from slugify import slugify


# Create your models here.
class User(AbstractUser):
    ROLE = [("admin", "Administrator"), ("user", "User")]

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    role = models.CharField(choices=ROLE, default="user", max_length=13)


class BaseModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.title))
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Category(BaseModel):
    icon = models.CharField(max_length=8, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(BaseModel):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    # url = models.CharField(max_length=255, blank=True)
    #
    # def save(self, *args, **kwargs):
    #     self.url = 'https://res.cloudinary.com/dk2ncioda/image/upload/v1/media/images/' + str(self.image.name)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Venue(BaseModel):
    description = models.CharField(max_length=2000, null=True)
    telephone = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=2000)
    rating = models.FloatField(null=True)
    images = models.ManyToManyField(Image, blank=True)
    address = models.CharField(max_length=2000, null=True)
    subcategory = models.ForeignKey(Subcategory, related_name='subcategory', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'
