from django.urls import path
from blog.views import AboutView

urlpatterns = [
    path("", AboutView.as_view()),
]