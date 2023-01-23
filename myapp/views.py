from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from myapp.forms import LoginForm,RegistrationForm,PostsForm,UserProfileForm
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from myapp.models import Posts
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib import messages


# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"Signin required")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
decorators=[signin_required,never_cache]

class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials")
                return render(request,self.template_name,{"form":form})

@method_decorator(signin_required,name="dispatch")
class IndexView(ListView):
    template_name="index.html"
    form_class=PostsForm
    model=Posts
    success_url=reverse_lazy("index")
    context_object_name="post"
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Posts.objects.all()

# @method_decorator(signin_required,name="dispatch")
# class PostList(ListView):
#     model=Posts
#     template_name: str="index.html"
#     context_object_name="post"
#     def get_queryset(self):
#         return Posts.objects.all()

decorators
def likes_view(request,*args,**kwargs):
    post_id=kwargs.get("id")
    post=Posts.objects.get(id=post_id)
    post.likes.add(request.user)
    post.save()
    return redirect("index")

decorators
def add_comment(request,*args,**kwargs):
    posts_id=kwargs.get("id")
    post=Posts.objects.get(id=posts_id)
    cmnt=request.POST.get("add-comment")
    post.comments_set.create(comment=cmnt,user=request.user)
    messages.success(request,"Comment Updated")
    return redirect("index")

@method_decorator(signin_required,name="dispatch")
class CreatePostView(CreateView):
    template_name: str="createpost.html"
    model=Posts
    form_class=PostsForm
    success_url=reverse_lazy("index")
    context_object_name="post"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

def post_delete(request,*args,**kwargs):
    post_id=kwargs.get("id")
    Posts.objects.filter(id=post_id).delete()
    messages.success(request,"Post Deleted Successfully")
    return redirect("my-posts")


@signin_required
def signout(request,*args,**kwargs):
    logout(request)
    messages.success(request,"Logout Successfull")
    return redirect("signin")

@method_decorator(signin_required,name="dispatch")
class MyPostsView(ListView):
    model=Posts
    context_object_name="post"
    template_name="myposts.html"
    
    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user)

