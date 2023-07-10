from django.urls import path
from . import views

urlpatterns = [
    # The dashboard page
    path("order/", views.order_coffee, name="order"),
]
