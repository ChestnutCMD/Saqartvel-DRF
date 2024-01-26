from django.urls import path

from api.views import *

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('category/<slug:slug>/', CategorySlugView.as_view()),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view()),

    path('subcategory/', SubcategoryListView.as_view()),
    path('subcategory/create/', SubcategoryCreateView.as_view()),
    path('subcategory/<int:pk>/', SubcategoryDetailView.as_view()),
    path('subcategory/<slug:slug>/', SubcategorySlugView.as_view()),
    path('subcategory/<int:pk>/update/', SubcategoryUpdateView.as_view()),
    path('subcategory/<int:pk>/delete/', SubcategoryDeleteView.as_view()),

    path('venue/', VenueListView.as_view()),
    path('venue/create/', VenueCreateView.as_view()),
    path('venue/<int:pk>/', VenueDetailView.as_view()),
    path('venue/<slug:slug>/', VenueSlugView.as_view()),
    path('venue/<int:pk>/update/', VenueUpdateView.as_view()),
    path('venue/<int:pk>/delete/', VenueDeleteView.as_view()),
    ]
