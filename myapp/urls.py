from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="index"),
    path('login/',views.login_user , name="login"),
    path('home/' , views.home , name="home"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_user , name="logout"),
    path('profile/',views.profile, name="profile"),
    path('about/', views.about , name="about"),
    path('post/', views.post , name="post"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('edit/<int:user_id>', views.edit, name="edit"),
    path('delete_account' , views.delete_account , name="delete_account"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name = 'change_password.html'))m
    path('password/', views.PasswordsChangeView.as_view(template_name = 'change_password.html')),
    path('password_success', views.password_success , name="password_success")
]