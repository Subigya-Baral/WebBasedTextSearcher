from django.shortcuts import render
from django.http import HttpResponse
import textract
import PyPDF2
import os
file_list={}
global searchtext
def has_text_word(filename,content, text):
	if text in filename:
		print("Found in: "+filename)
		return True
	if text in content:
		print("Found in content")
		return True
	return False
def search_text(folder,search_text):
	for root, dirs, files in os.walk(folder, topdown=False):
		for name in files:
			try:
				if name.endswith(('.txt', '.docx', '.pptx', '.xlsx')):
					fileContent = textract.process(os.path.join(root,name))
					parsedFile = fileContent.decode('utf-8')
					if has_text_word(name,parsedFile,search_text):
						print("Adding file: "+os.path.join(root,name))
						file_list[name]=os.path.join(root,name)
			except Exception:
				 print("Error on file: "+name)
def doc2string(path,file):
   fileContent = ""
   if file.endswith(('.txt', '.docx', '.pptx', '.xlsx')):
       fileContent = textract.process(path)
       parsedFile = fileContent.decode('utf-8')
       return parsedFile

def open_file(path, filename):
	text=""
	lines=doc2string(path,filename)
	l1 = lines.partition(searchtext)
	for l in l1:
		if l != searchtext:
			text=text+l
		else:
			text=text+'<span style="background-color: #ff0000">'+l+'</span>'
	return text
def index(request):
	return render(request, "TextSearcher/index.html",{'title':"Welcome People!", 'description':'Let\'s search for the text on your directory'})
def about(request):
	global searchtext
	table=''
	dir_search=request.POST['search_directory']
	searchtext=request.POST['search_text']
	search_text(dir_search,searchtext)
	return render(request,"TextSearcher/about.html",{'content':file_list,'title':'Files with content',})
def file(request):
	filename= request.GET.get('file')
	html=open_file(file_list[filename], filename)
	return render(request,"TextSearcher/file.html",{'content':html,'title':'File Content',})