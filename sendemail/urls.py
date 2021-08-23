from django.urls import path
from .views import ContactView, ContactSuccessView

app_name = 'sendemail'


urlpatterns = [
     path('', ContactView.as_view(), name="contact"),
     path('success/', ContactSuccessView.as_view(), name="success"),
]