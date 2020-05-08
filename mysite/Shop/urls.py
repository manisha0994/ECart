from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("productView/", views.productView, name="ProductView"),
    path("CheckOut/", views.CheckOut, name="CheckOut"),
]