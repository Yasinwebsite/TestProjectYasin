from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView,DetailView
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your views here.


def index(request):
    return HttpResponse("index")


# def post_list(request):
#     posts = Post.puplished.all()
#     paginator = Paginator(posts, 3)
#     page_number = request.GET.get('page', 1)
#
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     context = {
#         "posts": posts,
#     }
#     return render(request, "blog/list.html", context)

class PostListViews(ListView):
    paginate_by = 3
    template_name = 'blog/list.html'
    queryset = Post.puplished.all()
    context_object_name = 'posts'


# def post_detail(request, id):
    # post = get_object_or_404(Post, id=id)
    # context = {"post": post}
    # return render(request, "blog/detail.html", context)


class PostDetailViews(DetailView):
    model = Post
    template_name = 'blog/detail.html'


def addPost(request):
    if request.method == "POST":
        name = request.POST.get("title")
        des = request.POST.get("desc")

        slug = slugify(name) or "post"
        if Post.objects.filter(slug=slug).exists():
            slug = f"{slug}-{Post.objects.count() + 1}"

        user = request.user if request.user.is_authenticated else User.objects.first()
        
        Post.objects.create(
            title=name,
            des=des,
            slug=slug,
            users=user,
            status=Post.Status.PUBLISHED,
        )
        
        return redirect("blog:posts")
        


    return render(request, "blog/addPost.html", {})
