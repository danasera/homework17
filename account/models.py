
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.mail import send_mail
from django.utils.crypto import get_random_string



class UserManager(BaseUserManager):
    # чтобы не дублировать код при создании юзера и админа
    def _create(self, email, password, name, **extra_fields):
        if not email:
            raise ValueError('Email не может быть пустым')
        email = self.normalize_email(email)   # нормализует email
        user = self.model(email=email, name=name, **extra_fields)   # создаётся пользователь
        user.set_password(password)    # устанавливает шифрованный файл
        user.save()   # обнавляет объект в БД
        return user

    # создаёт обычного пользователя
    def create_user(self, email, password, name, **extra_fields):
        extra_fields.setdefault('is_staff', False)  # устанавливаются значения по умолчанию
        extra_fields.setdefault('is_active', False)
        return self._create(email, password, name, **extra_fields)

    # содаёт админ
    def create_superuser(self, email, password, name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create(email, password, name, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField('Электронная почта', primary_key=True)
    name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    is_active = models.BooleanField('Активный?', default=False)
    is_staff = models.BooleanField('Админ?', default=False)
    activation_code = models.CharField('Код активации', max_length=8, blank=True)


    objects = UserManager()


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff


    def create_activation_code(self):
        self.activation_code = get_random_string(8)
        self.save()


    def send_activation_mail(self):

        message = f'Ваш код активации: {self.activation_code}'
        send_mail('Активация аккаунта', 'test@test.com', [self.email])
