from django.urls import path
from .views import *

urlpatterns = [
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("profile/edit/", UserProfileEditView.as_view(), name="user_profile_edit"),
]
