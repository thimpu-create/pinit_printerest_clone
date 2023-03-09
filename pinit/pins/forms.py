from django import forms
from . models import Pin,Board

class CreatePinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['board','title','description','link','file']

    
    def __init__(self, user,*args, **kwargs):
        super(CreatePinForm, self).__init__(*args, **kwargs)
        self.fields['board'].queryset = Board.objects.filter(User_id = user.id)
        self.fields['title'].widget.attrs['placeholder'] = 'Add a Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Tell everyone what your pin is about..'
        self.fields['link'].widget.attrs['placeholder'] = 'Add a destination link'
        for visible in self.visible_fields():
            if visible.name == 'description':
                visible.field.widget.attrs['class'] = 'description-input border form-control'
            elif visible.name == 'board':
                visible.field.widget.attrs['class'] = 'board-input border form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control border rounded-pill'