from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('document_chat',views.document_chat)
]