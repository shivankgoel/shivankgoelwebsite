from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blog import models
from django.views.generic import(
    DetailView,
    CreateView,
)
from django.db.models import Count
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from blog import forms
from django.shortcuts import redirect
from django.views.generic.detail import SingleObjectMixin
from cbprojects import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    articles = models.Article.objects.all().order_by('-createdAt')
    top_article = articles[0]
    latest_articles = articles[1:5]
    # tech_articles = models.Article.objects.filter(tags__name__contains='Tech')[:3]
    # business_articles = models.Article.objects.filter(tags__name__contains='Business')[:3]
    # health_articles = models.Article.objects.filter(tags__name__contains='Health')[:3]
    tags = models.Tag.objects.all().annotate(a_count=Count('article')).order_by('-a_count')
    toptags = tags[:3]
    context = {
    "top_article" : top_article,
    "latest_articles" : latest_articles,
    "tags" : tags,
    "toptags" : toptags
    }
    response = render(request, 'blog/index.html', context)
    return response

def all_articles(request):
    tags = models.Tag.objects.all().annotate(a_count=Count('article')).order_by('-a_count')
    page = int(request.GET.get('page'))
    results_per_page = 4
    articles = models.Article.objects.all().order_by('-createdAt')
    paginator = Paginator(articles, results_per_page)
    if page < 1:
        page = 1
    if page > paginator.num_pages:
        page = paginator.num_pages
    posts = paginator.page(page)
    context = {
    "all_articles" : posts,
    "has_next" : posts.has_next(),
    "page" : page,
    "next_page" : page+1,
    "prev_page" : page-1,
    "numpages" : paginator.num_pages,
    "tags" : tags,
    }
    response = render(request, 'blog/all_articles.html', context)
    return response

class Article(DetailView):
    model = models.Article
    template_name = 'blog/article.html'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        authorized = self.request.user.is_authenticated
        if 'pk' in self.kwargs:
            article = self.model.objects.get(pk = self.kwargs['pk'])
        else:
            print("BKJBJKBKJBKJBJKB")
            article = self.model.objects.get(slug = self.kwargs['slug'])
        if authorized:
            num_results = models.Like.objects.filter(user = self.request.user, article = article).count()
        else:
            num_results = 0
        text = self.request.GET.get('text', '')
        data['comment_form'] = forms.CommentForm(initial={'content': text})
        data['already_liked'] = num_results
        data['authorized'] = authorized
        return data

class Author(DetailView):
    model = models.Author
    template_name = 'blog/author.html'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True


class Comment(View):
    def post(self, request):
        next = request.POST.get('next', '/')
        text = request.POST.get('content')
        if not self.request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, next))
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = models.Article.objects.get(pk = request.POST['article_pk'])
            comment.save()
        return HttpResponseRedirect(next)

class DeleteComment(View):
    def post(self, request, pk, pk2):
        next = request.POST.get('next', '/')
        article = models.Article.objects.get(pk = pk)
        comment = models.Comment.objects.get(pk = pk2).delete()
        return HttpResponseRedirect(next)


class Like(View):
    model = models.Article

    def post(self, request, pk):
        next = request.POST.get('next', '/')
        if not self.request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, next))
        article = self.model.objects.get(pk = pk)
        models.Like.objects.create(article = article, user = request.user)
        return HttpResponse(204)


class Dislike(View):
    model = models.Article

    def post(self, request, pk):
        article = self.model.objects.get(pk = pk)
        models.Like.objects.get(article = article, user = request.user).delete()
        return HttpResponse(204)



class Tag(DetailView):
    model = models.Tag
    template_name = 'blog/tag.html'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

def get_tag_by_name(request, *args, **kwargs):
    object = models.Tag.objects.filter(name=kwargs['name'])[0]
    context = {
    'object' : object,
    }
    response = render(request, 'blog/tag.html', context)
    return response


def createarticle(request):
    authors = models.Author.objects.all()
    context = {
    "authors" : authors
    }

    if request.method == "POST":
        article_data = {
            "title" : request.POST['title'],
            "content" : request.POST['content'],
        }
        article = models.Article.objects.create(**article_data);
        for author_id in request.POST['authors']:
            myauthor = models.Author.objects.get(pk = author_id)
            article.authors.add(myauthor)
        context["success"]  = True


    response = render(request, 'blog/createarticle.html', context)
    return response
