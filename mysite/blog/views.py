from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Article,Category,Tag
from operator import itemgetter 
from django.db.models import Q
from django.core.paginator import Paginator
import math
def get_top_tag(n):
	tag_list_obj = Tag.objects.all()
	tag_list_kw = {}
	for tag in tag_list_obj:
		tag_list_kw[tag.id] = tag.article_set.count()
	tag_list_tuple = sorted(tag_list_kw.iteritems(),key=itemgetter(1),reverse=True)[:n]

	tag_list = []

	for tag_tuple in tag_list_tuple:
		tag_list.append(Tag.objects.get(id=tag_tuple[0]))

	return tag_list

def index(req):
	category_list = Category.objects.all()
	tag_list = get_top_tag(10)
	article_list = Article.objects.all()[:4]
	hot_list = Article.objects.all().order_by('-click_num')[:8]
	recommend_list = Article.objects.filter(is_recommend = True)
	return render_to_response('index.html',{'category_list':category_list,'article_list':article_list,'hot_list':hot_list,'recommend_list':recommend_list,'tag_list':tag_list})

def article(req,id):
	category_list = Category.objects.all()
	tag_list = get_top_tag(10)
	hot_list = Article.objects.all().order_by('-click_num')[:8]
	recommend_list = Article.objects.filter(is_recommend = True)
	article=Article.objects.get(id=id)
	article.click_num=article.click_num+1
	article.save()
	return render_to_response('article.html',{'category_list':category_list,'article':article,'hot_list':hot_list,'recommend_list':recommend_list,'tag_list':tag_list})

def articles(req,page):
	category_list = Category.objects.all()
	tag_list = get_top_tag(10)
	hot_list = Article.objects.all().order_by('-click_num')[:8]
	recommend_list = Article.objects.filter(is_recommend = True)

	show_num = 4.0
	articles = Article.objects.all()
	paginator = Paginator(articles,show_num)
	article_list = paginator.page(page)
	total_page_num = int(math.ceil(Article.objects.count()/show_num))
	total_page = [x for x in range(0,total_page_num)]

	return render_to_response('articles.html',{'cnt_page':int(page),'total_page':total_page,'article_list':article_list,'category_list':category_list,'hot_list':hot_list,'recommend_list':recommend_list,'tag_list':tag_list})

def tag(req,id,page):
	category_list = Category.objects.all()
	tag_list = get_top_tag(10)
	hot_list = Article.objects.all().order_by('-click_num')[:8]
	recommend_list = Article.objects.filter(is_recommend = True)

	show_num = 4.0
	tag_obj=Tag.objects.get(id=id)
	articles = tag_obj.article_set.all()
	paginator = Paginator(articles,show_num)
	article_list = paginator.page(page)
	total_page_num = int(math.ceil(tag_obj.article_set.count()/show_num))
	total_page = [x for x in range(0,total_page_num)]
	tagname = Tag.objects.get(id=id).name
	return render_to_response('tag.html',{'tagname':tagname,'tagid':id,'cnt_page':int(page),'total_page':total_page,'article_list':article_list,'category_list':category_list,'hot_list':hot_list,'recommend_list':recommend_list,'tag_list':tag_list})

def search(req,keyword,page):
	category_list = Category.objects.all()
	tag_list = get_top_tag(10)
	hot_list = Article.objects.all().order_by('-click_num')[:8]
	recommend_list = Article.objects.filter(is_recommend = True)

	show_num = 4.0
	articles = Article.objects.filter(Q(content__contains=keyword) | Q(title__contains=keyword))
	paginator = Paginator(articles,show_num)
	article_list = paginator.page(page)
	total_page_num = int(math.ceil(articles.count()/show_num))
	total_page = [x for x in range(0,total_page_num)]
	return render_to_response('search.html',{'keyword':keyword,'cnt_page':int(page),'total_page':total_page,'article_list':article_list,'category_list':category_list,'hot_list':hot_list,'recommend_list':recommend_list,'tag_list':tag_list})


def category(req,id,page):
	category_list = Category.objects.all()
	tag_list = get_top_tag(10)
	hot_list = Article.objects.all().order_by('-click_num')[:8]
	recommend_list = Article.objects.filter(is_recommend = True)

	show_num = 4.0
	category_obj=Category.objects.get(id=id)
	articles = category_obj.article_set.all()
	paginator = Paginator(articles,show_num)
	article_list = paginator.page(page)
	total_page_num = int(math.ceil(category_obj.article_set.count()/show_num))
	total_page = [x for x in range(0,total_page_num)]
	categoryname = Category.objects.get(id=id).name
	return render_to_response('category.html',{'categoryname':categoryname,'categoryid':id,'cnt_page':int(page),'total_page':total_page,'article_list':article_list,'category_list':category_list,'hot_list':hot_list,'recommend_list':recommend_list,'tag_list':tag_list})

def about(req):
	return render_to_response('about.html',{})