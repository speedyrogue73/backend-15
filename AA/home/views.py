from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Comment
from .forms import CreatePostForm, PostCommentForm, PostCommentReplyForm
from django.utils.text import slugify
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        posts = Post.objects.filter(is_published=True)
        return render(request, 'home/index.html', {'posts': posts})


class DetailView(View):
    def get(self, request, post_slug):
        post = Post.objects.get(slug=post_slug, is_published=True)
        comments = Comment.objects.filter(post=post, is_reply=False)
        form = PostCommentForm()
        reply_form = PostCommentReplyForm()
        post.view_count += 1
        post.save()
        return render(request, 'home/detail.html', {'post': post, 'comments': comments, 'form': form, 'reply_form': reply_form})

    def post(self, request, post_slug):
        post = Post.objects.get(slug=post_slug, is_published=True)
        form = PostCommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                post=post,
                body=form.cleaned_data['body'],
            )
            messages.success(request, 'Comment created successfully', 'success')
            return redirect('home:detail', post_slug)
        messages.error(request, 'Comment not created successfully', 'danger')
        return redirect('home:detail', post_slug)


class CreatePostView(View):
    def get(self, request):
        form = CreatePostForm()
        return render(request, 'home/create.html', {'form': form})

    def post(self, request):
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                slug=slugify(form.cleaned_data['title']),
                body=form.cleaned_data['body'],
                poster=request.FILES['poster'],
                is_published=True,
            )
            messages.success(request, 'Post created successfully', 'success')
            return redirect('home:home')
        return render(request, 'home/create.html', {'form': form})


class ReplyView(View):
    def post(self, request, post_slug, comment_id):
        post = Post.objects.get(slug=post_slug, is_published=True)
        comment = Comment.objects.get(pk=comment_id)
        form = PostCommentReplyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            reply = Comment.objects.create(
                user=request.user,
                post=post,
                body=cd['body'],
                reply=comment,
                is_reply=True
            )
            messages.success(request, 'Comment created successfully', 'success')
            return redirect('home:detail', post_slug)
        messages.error(request, 'Comment not created successfully', 'danger')
        return redirect('home:detail', post_slug)


class RemoveCommentView(View):
    def get(self, request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        if request.user.is_authenticated and request.user == comment.post.user:
            comment.delete()
            messages.success(request, 'Comment deleted successfully', 'success')
            return redirect('home:home')
        messages.error(request, 'Comment not deleted successfully', 'danger')
        return redirect('home:home')
