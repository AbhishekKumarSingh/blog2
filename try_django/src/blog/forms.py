from django import forms

from .models import BlogPost

class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
	# title = forms.CharField() to overrides the model behaviour it was textfield initialy
	# in models.py
	class Meta:
		model = BlogPost
		fields = ['title', 'slug', 'content']

	# adding custom validation. method name starts with
	# clean_<fieldname>
	def clean_title(self, *args, **kwargs):
		instance = self.instance
		title = self.cleaned_data['title']
		qs = BlogPost.objects.filter(title__iexact=title) # __iexact case insensitive
		
		if instance is not None:
			qs = qs.exclude(id=instance.id)
		if qs.exists():
			raise forms.ValidationError("This title has already been taken")

		return title