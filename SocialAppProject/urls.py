"""SocialAppProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.SignUpView.as_view(),name="register"),
    path("",views.LoginView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    # path("home",views.PostList.as_view(),name="index"),
    path("logout",views.signout,name="signout"),
    path("posts/add",views.CreatePostView.as_view(),name="add-post"),
    # path("posts/<int:id>/comments/add",views.add_comment,name="add-comment"),
    path("myposts/all",views.MyPostsView.as_view(),name="my-posts"),
    path("posts/<int:id>/add-comment/add",views.add_comment,name="addcomment"),
    path("posts/<int:id>/likes",views.likes_view,name="add-likes"),
    path("myposts/<int:id>/delete",views.post_delete,name="post-delete"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
