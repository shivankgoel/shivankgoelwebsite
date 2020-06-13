from django.urls import path
from blog import views

urlpatterns = [
	path('article/<int:pk>', views.Article.as_view(), name ='get_blog_article_pk'),
	path('article/<slug:slug>', views.Article.as_view(), name ='get_blog_article_slug'),
	path('author/<int:pk>', views.Author.as_view(), name ='get_blog_author_pk'),
	path('author/<slug:slug>', views.Author.as_view(), name ='get_blog_author_slug'),
	path('tag/<int:pk>', views.Tag.as_view(), name ='get_blog_tag_pk'),
	path('tag/<slug:slug>', views.Tag.as_view(), name ='get_blog_tag_slug'),
	path('article', views.createarticle, name ='create_blog_article'),
	path('all_articles', views.all_articles, name ='all_articles'),
	path('comment/', views.Comment.as_view(), name ='comment'),
	path('article/<int:pk>/comment/<int:pk2>/delete', views.DeleteComment.as_view(), name ='deletecomment'),
	path('article/<int:pk>/like', views.Like.as_view(), name ='like'),
	path('article/<int:pk>/dislike', views.Dislike.as_view(), name ='dislike'),
	path('', views.index, name ='blogindex'),
]
