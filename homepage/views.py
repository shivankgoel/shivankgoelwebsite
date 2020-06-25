from django.shortcuts import render
import requests
import json
import random
from homepage.data import *
from homepage import models
from blog import models as blog_models
from django.db.models import Count

# def get_recent_ids(next_page_token = ''):
# 	myparams = {
# 	'key' : 'AIzaSyCODNQTCCNjEOQD4rq6Wrsm6yutO_oCx5M',
# 	'part' : 'contentDetails,id',
# 	'pageToken' : next_page_token,
# 	'playlistId' : 'PLK5n_RNeFvWTkq1YNFGZIYuhUuqvFW6LY'
# 	}
# 	r = requests.get('https://www.googleapis.com/youtube/v3/playlistItems', params = myparams)
# 	return json.loads(r.text)
#
# def get_recent_ids_all():
# 	ids  = []
# 	r = get_recent_ids()
# 	if 'items' in r:
# 		for item in r['items']:
# 			ids.append(item['contentDetails']['videoId'])
# 	while 'nextPageToken' in r:
# 		r = get_recent_ids(r['nextPageToken'])
# 		for item in r['items']:
# 			ids.append(item['contentDetails']['videoId'])
# 	ids.reverse()
# 	return ids[:3]
#
#
# def get_insta_posts(uname):
# 	r = requests.get('https://www.instagram.com/'+uname+'/?__a=1')
# 	obj = json.loads(r.text)
# 	shortcodes = []
# 	for x in obj['graphql']['user']['edge_owner_to_timeline_media']['edges']:
# 		if len(shortcodes) >= 5:
# 			break
# 		shortcodes.append(x['node']['shortcode'])
# 	return shortcodes
#
# def get_insta_posts_all():
# 	s1 = get_insta_posts('techlife_with_shivank')
# 	s2 = get_insta_posts('goel.sh')
# 	s = []
# 	for i in range(len(s1)):
# 		s.append(s1[i])
# 		s.append(s2[i])
# 	return s


def get_youtube_ids():
	return models.YoutubeLinks.objects.all().order_by('-createdAt')


# Create your views here.
def index(request):
	articles = blog_models.Article.objects.all().order_by('-createdAt')
	tags = blog_models.Tag.objects.all().annotate(a_count=Count('article')).order_by('-a_count')
	latest_articles = articles[0:3]
	context = {
	 'playlist_ids' : get_youtube_ids(),
	'jobs' : get_timeline(),
	'teachingjobs' : get_ta_experience(),
	'cornellresearch' : get_cornell_research(),
	'iitresearch' : get_iit_research(),
	"latest_articles" : latest_articles,
	"tags" : tags,
	}
	response = render(request, 'homepage/index.html', context)
	return response

def academic(request):
	context = {
	'schools' : get_education_background(),
	'teachingjobs' : get_ta_experience(),
	}
	response = render(request, 'homepage/academic.html', context)
	return response

def experience(request):
	context = {
	'jobs' : get_experience(),
	}
	response = render(request, 'homepage/experience.html', context)
	return response

def publicspeaking(request):
	events = models.PublicSpeakingEvents.objects.all().order_by('-date')
	context = {
	 'events' : events,
	}
	response = render(request, 'homepage/publicspeaking.html', context)
	return response

def tech_pe_charcha(request):
	tpc_events = models.TechPeCharchaEpisodes.objects.all().order_by('-date')
	context = {
	 'events' : tpc_events,
	}
	response = render(request, 'homepage/tech_pe_charcha.html', context)
	return response

def contact(request):
	context = {
	}
	response = render(request, 'homepage/contact.html', context)
	return response

def calendar(request):
	context = {
	}
	response = render(request, 'homepage/calendar.html', context)
	return response


def reading(request):
	books = models.Book.objects.all().order_by('-rating')
	context = {
	 'books' : books,
	}
	response = render(request, 'homepage/reading.html', context)
	return response
