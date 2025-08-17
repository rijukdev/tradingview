from django.urls import path, include
from signals import views as signals

urlpatterns = [
    path('signals/', signals.SignalAPI.as_view()),
    path('signals/<int:pk>/', signals.SignalDetailsAPI.as_view()),

    path('signals/delete/', signals.SignalDeleteAPI.as_view()),
    path('signals/delete/<int:pk>/', signals.SignalDetailsDeleteAPI.as_view()),
]
