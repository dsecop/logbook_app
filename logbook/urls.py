from django.urls import path
from logbook.views import HomePageView

app_name = 'logbook'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
]
