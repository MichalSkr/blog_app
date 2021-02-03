from django.forms import ModelForm
from .models import Article


class WriterArticleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(WriterArticleForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['readonly'] = True

    class Meta:
        model = Article
        fields = ['title', 'content', 'status', 'written_by']
        exclude = ('written_by',)
