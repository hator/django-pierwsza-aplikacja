from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post, Comment


def post_list(request):
    posts = Post.objects.order_by("date")
    context = {"posts": posts}
    return render(request, "blog/posts_list.html", context)


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "blog/post_details.html", context)


def add_comment(request, post_id):
    comment = Comment(post_id=post_id, content=request.POST["content"])
    comment.save()
    return redirect(f"/posts/{post_id}")