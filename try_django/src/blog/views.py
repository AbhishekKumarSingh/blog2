from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm

# calling by id in url
# def blog_post_detail(request, post_id):
# 	#obj = BlogPost.objects.get(id=post_id)
# 	obj = get_object_or_404(BlogPost, id=post_id)
# 	template = 'blog_post_detail.html'
# 	context = {'object': obj}
# 	return render(request, template, context)


# calling by slug in the url
# def blog_post_detail(request, post_slug):
# 	#obj = BlogPost.objects.get(id=post_id)
# 	obj = get_object_or_404(BlogPost, slug=post_slug)
# 	template = 'blog_post_detail.html'
# 	context = {'object': obj}
# 	return render(request, template, context)


def blog_post_list_view(request):
	# list of objects
	# could be search
	qs = BlogPost.objects.all()
	template = 'blog/list.html'
	context = {'object_list': qs}
	return render(request, template, context)

def blog_post_detail_view(request, post_slug):
	# about 1 object
	obj = get_object_or_404(BlogPost, slug=post_slug)
	template = 'blog/detail.html'
	context = {'object': obj}
	return render(request, template, context)

#@login_required(login_url="/login")
@ staff_member_required
#@login_required
def blog_post_create_view(request):
	# create objects, use form
	#form = BlogPostForm(request.POST or None)
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		#obj = BlogPost.objects.create(**form.cleaned_data)
		#form.save() # create an object and saves it to db
		# manupulate data
		obj = form.save(commit=False) # not actually saving data
		obj.user = request.user
		# obj.title = form.cleaned_data['title'] + 'my_title'
		obj.save()

		form = BlogPostModelForm()
	template = 'blog/form.html'
	context = {
		'form': form,
		'title': "Create Your Blog Post"}
	return render(request, template, context)

def blog_post_update_view(request, post_slug):
	obj = get_object_or_404(BlogPost, slug=post_slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		print(form.cleaned_data)
		form.save()
		return redirect(f'/blog/{post_slug}')
		#form = BlogPostModelForm()
	template = 'blog/form.html'
	context = {'form': form, "title": f"Update {obj.title}"}
	return render(request, template, context)

def blog_post_delete_view(request, post_slug):
	obj = get_object_or_404(BlogPost, slug=post_slug)
	if request.method == 'POST':
		obj.delete()
		return redirect('/blog')
	template = 'blog/delete.html'
	context = {'object': obj, 'form': None}
	return render(request, template, context)