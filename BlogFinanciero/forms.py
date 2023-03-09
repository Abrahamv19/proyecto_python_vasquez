from django import forms
from BlogFinanciero.models import Post_bloguero, Post_lector, Post_temas

class TemasForm(forms.ModelForm):
    class Meta:
        model = Post_temas
        fields = '__all__'

class BloguerosForm(forms.ModelForm):
    class Meta:
        model = Post_bloguero
        fields = '__all__'

class LectoresForm(forms.ModelForm):
    class Meta:
        model = Post_lector
        fields = '__all__'
