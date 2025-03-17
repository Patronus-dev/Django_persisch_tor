from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image


class Place(models.Model):
    CATEGORY_GROUP = [
        ('food & drink', 'Food & Drink'),
        ('medical', 'Medical'),
        ('technical', 'Technical'),
        ('store', 'Store'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other')
    ]

    GERMAN_CITIES = (
        ("Berlin", "Berlin"),
        ("Hamburg", "Hamburg"),
        ("München", "München"),
        ("Köln", "Köln"),
        ("Frankfurt am Main", "Frankfurt am Main"),
        ("Stuttgart", "Stuttgart"),
        ("Düsseldorf", "Düsseldorf"),
        ("Dortmund", "Dortmund"),
        ("Essen", "Essen"),
        ("Leipzig", "Leipzig"),
        ("Bremen", "Bremen"),
        ("Dresden", "Dresden"),
        ("Hannover", "Hannover"),
        ("Nürnberg", "Nürnberg"),
        ("Duisburg", "Duisburg"),
        ("Bochum", "Bochum"),
        ("Wuppertal", "Wuppertal"),
        ("Bielefeld", "Bielefeld"),
        ("Bonn", "Bonn"),
        ("Münster", "Münster"),
        ("Karlsruhe", "Karlsruhe"),
        ("Mannheim", "Mannheim"),
        ("Augsburg", "Augsburg"),
        ("Wiesbaden", "Wiesbaden"),
        ("Mönchengladbach", "Mönchengladbach"),
        ("Gelsenkirchen", "Gelsenkirchen"),
        ("Braunschweig", "Braunschweig"),
        ("Chemnitz", "Chemnitz"),
        ("Kiel", "Kiel"),
        ("Aachen", "Aachen"),
        ("Halle (Saale)", "Halle (Saale)"),
        ("Magdeburg", "Magdeburg"),
        ("Freiburg im Breisgau", "Freiburg im Breisgau"),
        ("Krefeld", "Krefeld"),
        ("Lübeck", "Lübeck"),
        ("Oberhausen", "Oberhausen"),
        ("Erfurt", "Erfurt"),
        ("Mainz", "Mainz"),
        ("Rostock", "Rostock"),
        ("Kassel", "Kassel"),
        ("Hagen", "Hagen"),
        ("Hamm", "Hamm"),
        ("Saarbrücken", "Saarbrücken"),
        ("Mülheim an der Ruhr", "Mülheim an der Ruhr"),
        ("Potsdam", "Potsdam"),
        ("Ludwigshafen am Rhein", "Ludwigshafen am Rhein"),
        ("Oldenburg", "Oldenburg"),
        ("Leverkusen", "Leverkusen"),
        ("Osnabrück", "Osnabrück"),
        ("Solingen", "Solingen"),
        ("Heidelberg", "Heidelberg"),
        ("Herne", "Herne"),
        ("Neuss", "Neuss"),
        ("Darmstadt", "Darmstadt"),
        ("Paderborn", "Paderborn"),
        ("Regensburg", "Regensburg"),
        ("Ingolstadt", "Ingolstadt"),
        ("Würzburg", "Würzburg"),
        ("Fürth", "Fürth"),
        ("Wolfsburg", "Wolfsburg"),
        ("Offenbach am Main", "Offenbach am Main"),
        ("Ulm", "Ulm"),
        ("Heilbronn", "Heilbronn"),
        ("Pforzheim", "Pforzheim"),
        ("Göttingen", "Göttingen"),
        ("Bottrop", "Bottrop"),
        ("Trier", "Trier"),
        ("Recklinghausen", "Recklinghausen"),
        ("Reutlingen", "Reutlingen"),
        ("Bremerhaven", "Bremerhaven"),
        ("Koblenz", "Koblenz"),
        ("Bergisch Gladbach", "Bergisch Gladbach"),
        ("Jena", "Jena"),
        ("Remscheid", "Remscheid"),
        ("Erlangen", "Erlangen"),
        ("Moers", "Moers"),
        ("Siegen", "Siegen"),
        ("Hildesheim", "Hildesheim"),
        ("Salzgitter", "Salzgitter"),
    )

    title = models.CharField(max_length=250, unique=True, verbose_name="Name of the place", blank=False, null=False,
                             help_text="Enter the name of the place.")
    category = models.CharField(max_length=100, choices=CATEGORY_GROUP, blank=False, null=False,
                                verbose_name="Category", help_text="Select the category of the place.")
    city = models.CharField(max_length=100, choices=GERMAN_CITIES, blank=False, null=False, default='Berlin')
    address = models.CharField(max_length=500, verbose_name="Address", blank=False, null=False,
                               help_text="Enter the address of the place.")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone number",
                                    help_text="Enter the phone number of the place.")
    website = models.URLField(max_length=200, blank=True, null=True, verbose_name="Website",
                              help_text="Enter the website of the place.")
    description = models.TextField(blank=False, null=False, verbose_name="Description",
                                   help_text="Write a description of the place.")

    image_main = models.ImageField(upload_to='places/', null=True, blank=True, verbose_name="Main Image",
                                   help_text="Upload an main image of the place or service.")
    image2 = models.ImageField(upload_to='places/', null=True, blank=True, verbose_name="Image2",
                               help_text="Upload an image 2 of the place or service.")
    image3 = models.ImageField(upload_to='places/', null=True, blank=True, verbose_name="Image3",
                               help_text="Upload an image 3 of the place or service.")
    image4 = models.ImageField(upload_to='places/', null=True, blank=True, verbose_name="Image4",
                               help_text="Upload an image 4 of the place or service.")
    image5 = models.ImageField(upload_to='places/', null=True, blank=True, verbose_name="Image5",
                               help_text="Upload an image 5 of the place or service.")

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    datetime_updated = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('place_detail', args=[self.id])

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"

    def save(self, *args, **kwargs):
        # برای هر فیلد تصویر تغییر اندازه بده
        if self.image_main:
            self.image_main = self.resize_image(self.image_main)
        if self.image2:
            self.image2 = self.resize_image(self.image2)
        if self.image3:
            self.image3 = self.resize_image(self.image3)
        if self.image4:
            self.image4 = self.resize_image(self.image4)
        if self.image5:
            self.image5 = self.resize_image(self.image5)

        # ذخیره‌سازی تغییرات
        super(Place, self).save(*args, **kwargs)

    def resize_image(self, image):
        """تغییر اندازه تصویر به 720x720 پیکسل"""
        img = Image.open(image)
        img = img.convert('RGB')  # برای جلوگیری از مشکلات فرمت
        img = img.resize((720, 720), Image.Resampling.LANCZOS)  # تغییر به LANCZOS

        # ذخیره کردن تصویر تغییر اندازه داده شده
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumb_io.seek(0)

        # بازسازی فایل تصویر تغییر اندازه داده شده
        return InMemoryUploadedFile(thumb_io, None, image.name, 'image/jpeg', thumb_io.tell(), None)


class Comment(models.Model):
    USER_OPINIONS = [
        ('perfect', 'Perfect'),
        ('good', 'Good'),
        ('weak', 'Weak')
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500, blank=False, null=False, verbose_name="Description",
                            help_text="Write your comment here.")
    opinion = models.CharField(max_length=50, choices=USER_OPINIONS, blank=False, null=False)
