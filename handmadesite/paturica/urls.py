from django.urls import path
from paturica.views import home, register_message, detail

urlpatterns = [
    path('', home, name='home-page'),
    path('register_message/', register_message, name='register-message'),
    path('detail/<int:pic_id>', detail, name='object-detail')
]
