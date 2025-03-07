from django.shortcuts import redirect
from django.utils.translation import activate


def set_language(request):
    language_code = request.GET.get('language')
    activate(language_code)
    return redirect(request.META.get('HTTP_REFERER'))
