from django.shortcuts import render, redirect
from index.models import Journal, Volume, Article, TopEditor, FeaturedArticle, Editor, JournalFee

# Create your views here.
def index(request):
	context = {}
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	featured_articles = FeaturedArticle.objects.all()
	context = {
		'top_editors' : top_editors,
		'featured_articles' : featured_articles,
		'journals' : journals
	}
	return render(request, 'index/index.html', context )
def error(request):
	return render(request, 'index/error.html', {})
def about_us(request):
    return render(request, 'index/about_us.html', {})

def contact_us(request):
    return render(request, 'index/contact_us.html', {})

def submitManuscript(request):
    return render(request, 'index/submitManuscript.html', {})

def journals(request):
	context = {}
	journals = Journal.objects.all()
	context['journals'] = journals
	return render(request, 'index/journals.html', context)

def journal_details(request, id):
 	context = {}
 	journal_id = id
 	journals = Journal.objects.all()
 	journal = Journal.objects.get(id = journal_id)
 	volumes = Volume.objects.filter(journal_id = journal_id).order_by('-volume_year')
 	editors = Editor.objects.filter(journal_id=journal_id)
 	articles = []

 	for volume in volumes:
 		for article in Article.objects.filter(volume=volume):
 			articles.append(article)
 	articles = list(articles[:10])
 	context = {
 		'journal' 	: journal,
 		'volumes' 	: volumes,
 		'articles'	: articles,
 		'editors'	: editors,
 		'journals'	: journals
 	}
 	return render(request, 'index/journal_details.html', context)

def volume_articles(request, id, vol, issue):
	context = {}
	journal = Journal.objects.get(id=id)
	volume = Volume.objects.get(journal=journal, volume_name=vol, issue_name=issue)
	volume_name = volume
	issue_name = volume.issue_name
	articles = Article.objects.filter(volume=volume)
	context = {
		'volume_name' 	: volume_name,
		'issue_name' 	: issue_name,
		'articles'		: articles,
		'journal'		: journal
	}
	return render(request, 'index/volume_articles.html', context)

def author_guidelines(request):
	return render(request, 'index/author_guidelines.html', {})

def processing_fees(request):
	journal_fees = JournalFee.objects.all()
	return render(request, 'index/processing_fees.html', {'journal_fees': journal_fees})
