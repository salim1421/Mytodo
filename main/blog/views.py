from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Post, Category


def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        p_like = get_object_or_404(Post, id=self.request.user.id)
        total_likes = p_like.total_likes()
        liked = True
        if p_like.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context
    

class CategoryView(ListView):
    template_name = 'blog/categories.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        context = {
            'cat': self.kwargs['category'],
            'item': Post.objects.filter(category__category_name=self.kwargs['category'])
        }
        return context
    

def category_list(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return context
