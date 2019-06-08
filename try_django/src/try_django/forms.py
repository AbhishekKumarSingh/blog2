from django import forms


class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea)

	# adding custom validation. method name starts with
	# clean_<fieldname>
	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data['email']

		if email.endswith('.edu'):
			raise forms.ValidationError("We don't accept .edu emails.")

		return email