from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from records.models import Post 

from django.http import HttpResponse



class PostListView(ListView):

	model = Post


class PostDetailView(DetailView):

	model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'slug', 'image', 'content']




class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'slug', 'image', 'content']
    template_name_suffix = '_update_form'

class PostDelete(DeleteView):
	model = Post
	success_url = reverse_lazy('records:list_posts')











	
def example(request):
	# return HttpResponse("Hello World!")
	context = {
		"name":"Art"
	}
	return render(request, "mywebpage.html", context)
