from django import forms

from .models import Comment, Place


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_rating', 'text',)


class PlaceFilterForm(forms.Form):
    city = forms.ChoiceField(
        choices=[('', 'انتخاب شهر')] + [(city, city) for city in Place.objects.values_list('city', flat=True).distinct()],
        required=False,
        label='شهر'
    )
    category = forms.ChoiceField(
        choices=[('', 'انتخاب دسته‌بندی')] + [(category, category) for category in Place.objects.values_list('category', flat=True).distinct()],
        required=False,
        label='دسته‌بندی'
    )


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title',
                  'category',
                  'city',
                  'address',
                  'phone_number',
                  'website',
                  'description',
                  'image_main',
                  'image2',
                  'image3',
                  'image4',
                  'image5',
                  ]
