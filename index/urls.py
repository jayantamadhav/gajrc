from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitManuscript/', views.submitManuscript , name="submitManuscript"),
    path('journals/', views.journals , name="journals"),
    path('about_us/', views.about_us, name="about_us"),
    path('journal_details/<int:id>', views.journal_details , name="journal_details"),
    path('journal_details/<int:id>/<str:vol>/<str:issue>', views.volume_articles , name="volume_articles"),
    path('author_guidelines/', views.author_guidelines , name="author_guidelines"),
    path('processing_fees/', views.processing_fees , name="processing_fees"),
]