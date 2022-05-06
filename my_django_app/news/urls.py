from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.news_home, name='news_home'),
    path('create',views.create, name='create'),
    path('<int:pk>',views.NewDetailView.as_view(),name='news-detail'),
    path('<int:pk>/update',views.NewUpdateView.as_view(),name='news-update'),
    path('<int:pk>/delete',views.NewDeleteView.as_view(),name='news-delete'),
    path('quram/<int:pk>',views.QuramView.as_view(),name='quram'),
    path('qundylyq/<int:pk>',views.QundylyqView.as_view(),name='qundylyq'),
    path('post/<slug:post_slug>',views.show_post,name='post'),
    path('tags',views.index),
    path('login',views.loginPage,name='login'),
    path('register',views.registerPage,name='register'),
    path('logout',views.logoutUser,name='logout'),
    path('user/',views.userPage,name='user-page'),
    path('send/', views.send_message),
    path('client/', views.clientPage, name="client-page")
]