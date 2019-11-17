# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from index.models import *
from django.core.mail import send_mail, EmailMessage 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	context = {}
	journals = Journal.objects.all()[:7]
	top_editors = TopEditor.objects.all()
	featured_articles = FeaturedArticle.objects.all()
	memberin = MemberIn.objects.all()
	context = {
		'top_editors' : top_editors,
		'featured_articles' : featured_articles,
		'journals' : journals,
		'memberin' : memberin
	}
	return render(request, 'index/index.html', context )

def error(request):
	return render(request, 'index/error.html', {})

def about_us(request):
	context = {}
	top_editors = TopEditor.objects.all()
	journals = Journal.objects.all()
	context = {
		'top_editors' : top_editors,
		'journals' : journals
	}
	return render(request, 'index/about_us.html', context)

def contact_us(request):
	context = {}
	top_editors = TopEditor.objects.all()
	journals = Journal.objects.all()
	context = {
		'top_editors' : top_editors,
		'journals' : journals
	}
	return render(request, 'index/contact_us.html', context)

def submitManuscript(request):
	context = {}
	top_editors = TopEditor.objects.all()
	journals = Journal.objects.all()
	context = {
		'top_editors' : top_editors,
		'journals' : journals,
	}
	return render(request, 'index/submitManuscript.html', context)

def journals(request):
	context = {}
	top_editors = TopEditor.objects.all()
	journals = Journal.objects.all()
	context = {
		'top_editors' : top_editors,
		'journals' : journals
	}
	return render(request, 'index/journals.html', context)

def journal_details(request, url):
 	context = {}
 	journals = Journal.objects.all()
 	journal = Journal.objects.get(journal_url = url)
 	volumes = Volume.objects.filter(journal_id = journal.id).order_by('-volume_year')
 	editors = Editor.objects.filter(journal_id = journal.id)
 	articles = []
 	for volume in volumes:
 		for article in Article.objects.filter(volume=volume):
 			articles.append(article)
 	articles = list(articles[:10])
 	context = {
 		'journal' 	: journal,
 		'volumes' 	: volumes,
 		'articles'	: articles,
 		'top_editors'	: editors,
 		'journals'	: journals
 	}
 	return render(request, 'index/journal_details.html', context)

def volume_articles(request, url, vol, issue):
	context = {}
	journal = Journal.objects.get(journal_url = url)
	journals = Journal.objects.all()
	top_editors = TopEditor.objects.all()
	volume = Volume.objects.get(journal=journal, volume_name=vol, issue_name=issue)
	volume_name = volume
	issue_name = volume.issue_name
	articles = Article.objects.filter(volume=volume)
	context = {
		'volume_name' 	: volume_name,
		'issue_name' 	: issue_name,
		'articles'		: articles,
		'journal'		: journal,
		'top_editors'	: top_editors,
		'journals'		: journals,
	}
	return render(request, 'index/volume_articles.html', context)

def author_guidelines(request):
	context = {}
	top_editors = TopEditor.objects.all()
	journals = Journal.objects.all()
	context = {
		'top_editors' : top_editors,
		'journals' : journals
	}
	return render(request, 'index/author_guidelines.html', context)


def publication_ethics(request):
	context = {}
	top_editors = TopEditor.objects.all()
	journals = Journal.objects.all()
	context = {
		'top_editors' : top_editors,
		'journals' : journals
	}
	return render(request, 'index/publication_ethics.html', context)

def processing_fees(request):
	context = {}
	top_editors = TopEditor.objects.all()
	journals = Journal.objects.all()
	journal_fees = JournalFee.objects.all()
	context = {
		'top_editors' : top_editors,
		'journals' : journals,
		'journal_fees' : journal_fees
	}
	return render(request, 'index/processing_fees.html', context)


def submitManuscript(request):
	journals = Journal.objects.all()
	context = {
		'journals' : journals
	}
	if request.POST:
		data = request.POST
		file = request.FILES['file']
		subject = 'Manuscript Submission'
		message = '------Personal Details------' + '\n\n' + 'Name : ' + data['title'] + ' ' + data['first'] + ' ' + data['last'] + '\n' + 'University : ' + data['university'] + '\n' + 'Address : ' + data['address'] + '\n' + 'Email : ' + data['email'] + '\n' + 'Phone : ' + data['phone'] + '\n\n' + '------Document Details------' + '\n\n' + 'Journal : ' + data['journal'] + '\n'	+ 'Artile Type : ' + data['article-type'] + '\n' + 'Manuscript Title : ' + data['manuscript-title'] + '\n' + 'Abstract : ' + data['abstract'] + '\n'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['submit.gajrc@gmail.com',]
		email = EmailMessage( subject, message, email_from, recipient_list )
		email.attach(file.name, file.read(), file.content_type)
		email.send()
		return render(request, 'index/submitted.html', {})
	return render(request, 'index/submitManuscript.html', context)

def submitted(request):
	return render(request, 'index/submitted.html', {})
