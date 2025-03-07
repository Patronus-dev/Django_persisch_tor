from django.db import models


class Place(models.Model):
    CATEGORY_GROUP = [
        ('restaurant', 'Restaurant'),
        ('store', 'Store'),
        ('cafe', 'Cafe'),
        ('service', 'Service'),
        ('other', 'Other')
    ]

    name = models.CharField(max_length=255, unique=True, verbose_name="Name of the place",
                            help_text="Enter the name of the place.")
    category = models.CharField(max_length=100, choices=CATEGORY_GROUP, verbose_name="Category",
                                help_text="Select the category of the place.")
    address = models.CharField(max_length=500, verbose_name="Address",
                               help_text="Enter the address of the place.")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone number",
                                    help_text="Enter the phone number of the place.")
    website = models.URLField(max_length=200, blank=True, null=True, verbose_name="Website",
                              help_text="Enter the website of the place.")
    description = models.TextField(blank=True, null=True, verbose_name="Description",
                                   help_text="Write a description of the place.")
    image = models.ImageField(upload_to='places/', null=True, blank=True, verbose_name="Place Image",
                              help_text="Upload an image of the place.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"
