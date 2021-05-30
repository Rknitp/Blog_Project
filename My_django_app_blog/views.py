from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView

                                  )

from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin#139 #143
'''here we are defining a function which will
take request as an argument and within this funcn
 we r simply going to return what we
 want the user to see when they are sent to this route
 '''
'''
This is the syntax when we are not calling
 our templates.
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
def about(request):
    return HttpResponse('<h1>Blog About</h1>')
'''
#syntax when we are using our templates
'''
#These are used when we are directly aking the input from user not from database table
Display_item = [
    {
        'author' : 'Premchand',
        'title' : 'Godan',
        'content' : 'Indian Culture',
        'date' : '2-12-1902'
    },
    {
        'author': 'Dinkar',
        'title': 'KarmBhumi',
        'content': 'Life-Style',
        'date': '2-2-1932'
    }
]
'''
def home(request):
    context = {
        'posts': Post.objects.all() #This says that we are taking the input from the database table
    }
    return render(request, 'My_django_app_blog/home.html', context)


class PostListView(ListView):#120
    model = Post
    template_name = 'My_django_app_blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    ordering = ['-date_posted'] #- sign to shows order from new to old
    paginate_by = 5

class UserPostListView(ListView):#120
    model = Post
    template_name = 'My_django_app_blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    #ordering = ['-date_posted'] #- sign to shows order from new to old
    paginate_by = 5

    def get_queryset(self):#161
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):#120
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):#132 #139
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



#140
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):#132 #139 #143
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #144
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):#120
    model = Post
    success_url = '/'

    def test_func(self): #144
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

def about(request):
    return render(request,'My_django_app_blog/about.html',{'title':'About'})