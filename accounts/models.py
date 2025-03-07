from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name",
                            help_text="Enter your name."
                            )
    phone_number = PhoneNumberField(region="DE", max_length=15, unique=True, null=False, blank=False,
                                    verbose_name="Phone Number",
                                    help_text="Enter your phone number."
                                    )
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="E-Mail",
                              help_text="Enter your Email address."
                              )
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name="Profile photo")

    # ارجاع به مدل 'Place' که در اپلیکیشن دیگری به نام 'places' است
    favorite_places = models.ManyToManyField('places.Place', blank=True)  # مکان‌های موردعلاقه کاربر
    reported_places = models.ManyToManyField('places.Place', related_name='reports',
                                             blank=True)  # مکان‌هایی که ریپورت کرده

    total_reports = models.IntegerField(default=0)  # تعداد ریپورت‌هایی که داده
    total_reviews = models.IntegerField(default=0)  # تعداد نظراتی که گذاشته
    is_banned = models.BooleanField(default=False)  # آیا حساب مسدود شده؟

    date_joined = models.DateTimeField(auto_now_add=True)  # تاریخ عضویت
    last_login = models.DateTimeField(auto_now=True)  # آخرین ورود به سایت

    # اضافه کردن related_name برای جلوگیری از تداخل در 'groups' و 'user_permissions' در صورت نیاز
    groups = models.ManyToManyField('auth.Group', related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_permissions', blank=True)

