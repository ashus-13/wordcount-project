from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordcount = fulltext.split()
	worddictonary={}
	for word in wordcount:
		if word in worddictonary:
			worddictonary[word]+=1
		else:
			worddictonary[word]	=1
	return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordcount),'wordcount':worddictonary})

def about(request):
	return render(request, 'about.html')	
