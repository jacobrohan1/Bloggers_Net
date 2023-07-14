from django.shortcuts import render,redirect, get_object_or_404
from homepage.models import Blogpost
from .forms import BlogpostForm



def home(request):
    return render(request, 'home.html')

def feeds(request):
    return render(request, 'feeds.html')

def create_blog_post(request):
    # print('HELLO')
    if request.method == 'POST':
        # print('before saving')
        form = BlogpostForm(request.POST)
        # print('not valid')
        if form.is_valid():
            # print('valid')
            blog_post = form.save(commit= False)
            blog_post.user = request.user
            blog_post.save()
            return redirect('view_blogs')
    else:
        form= BlogpostForm()
        
    return render(request, 'feeds.html', {'forms' : form}) 

def view_blogs(request):
    blog_post = Blogpost.objects.all() # retrieves all the blogs from the database
    return render(request,'view_blogs.html', {'blog_posts': blog_post})



def view_blog_post(request, pk):
    blog_post = get_object_or_404(Blogpost, pk=pk)
    return render(request, 'view_blog_post.html', {'blog_post': blog_post})

        