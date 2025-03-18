from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("Enter your name.")
    )

    phone_number = PhoneNumberField(
        region="DE",
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Phone Number"),
        help_text=_("Enter your phone number.")
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("E-Mail"),
        help_text=_("Enter your Email address.")
    )

    profile_pic = models.ImageField(
        upload_to="profile_pics/",
        default="accounts/profile_default.jpg",
        null=True,
        blank=True,
        verbose_name=_("Profile photo")
    )

    # ارجاع به مدل 'Place' که در اپلیکیشن دیگری به نام 'places' است
    # favorite_places = models.ManyToManyField("places.Place", blank=True, verbose_name=_("Favorite Places"))
    # reported_places = models.ManyToManyField("places.Place", related_name="reports", blank=True, verbose_name=_("Reported Places"))

    total_reports = models.IntegerField(
        default=0,
        verbose_name=_("Total Reports")
    )
    total_reviews = models.IntegerField(
        default=0,
        verbose_name=_("Total Reviews")
    )
    is_banned = models.BooleanField(
        default=False,
        verbose_name=_("Is Banned?")
    )

    # اضافه کردن related_name برای جلوگیری از تداخل در 'groups' و 'user_permissions'
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True,
        verbose_name=_("Groups")
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True,
        verbose_name=_("User Permissions")
    )

    def __str__(self):
        return self.username
