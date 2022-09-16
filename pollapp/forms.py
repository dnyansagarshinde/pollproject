from django import forms
from .models import PollModel

class PollForm(forms.ModelForm):
	class Meta:
		model = PollModel
		fields = ["qts","op1","op2","op3"]
		widgets = {"qts":forms.Textarea(attrs={"rows":4,"cols":30})}