from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from records.models import Post 

from django.http import HttpResponse



class PostListView(ListView):

	model = Post


class PostDetailView(DetailView):

	model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'slug', 'image', 'content']


from django.views.generic.edit import UpdateView


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'slug', 'image', 'content']
    template_name_suffix = '_update_form'













	
def example(request):
	# return HttpResponse("Hello World!")
	context = {
		"name":"Art"
	}
	return render(request, "mywebpage.html", context)
