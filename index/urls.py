# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('submitManuscript/', views.submitManuscript , name="submitManuscript"),
    path('journals/', views.journals , name="journals"),
    path('about_us/', views.about_us, name="about_us"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('journal_details/<str:url>', views.journal_details , name="journal_details"),
    path('journal_details/<str:url>/<str:vol>/<str:issue>', views.volume_articles , name="volume_articles"),
    path('author_guidelines/', views.author_guidelines , name="author_guidelines"),
    path('publication-ethics/', views.publication_ethics, name='publication_ethics'),
    path('processing_fees/', views.processing_fees , name="processing_fees"),
    path('error', views.error, name='error'),
    path('submitted', views.submitted, name='submitted'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)