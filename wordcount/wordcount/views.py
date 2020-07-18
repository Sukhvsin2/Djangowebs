from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html',{'dic':'Here the concatination of dictionary is performed.'})

#def contact(request):
#	return HttpResponse("<h1>Contact Us</h1><br>This is contack us page.")

def count(request):
	data = request.GET['fulltextarea']
	words = data.split()
	words_len = len(words)
	char_len = len(data)

	word_dic = {}
	for word in words:
		if word in word_dic:
			word_dic[word] += 1
		else:
			word_dic[word] = 1
	sorted_list = sorted(word_dic.items(),key = operator.itemgetter(1),reverse = True)
	return render(request,'count.html',{'text':data,'words_len':words_len,'char_len':char_len,'word_dic':sorted_list})

def about(request):
	return render(request,'about.html')