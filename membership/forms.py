from django import forms
from membership.models import Review


class ReviewForm(forms.ModelForm):
    class Meta :
        model = Review
        fields =['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': '상품 만족도에 대한 후기를 남겨주세요.(최소 10자 이상 입력해주세요.)',
                                             'class':'form-control',
                                             'name' : 'review',
                                             'cols' : '30',
                                             'rows' : '7' }),
        }

