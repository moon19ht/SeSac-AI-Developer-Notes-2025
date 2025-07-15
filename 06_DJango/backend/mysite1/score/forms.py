from django import forms 
from .models import Score # form태그와 model 클래스 연동 

class ScoreForm(forms.ModelForm):
    # 내부클래스 
    # 클래스 안에 클래스를 만들어서 사용하는 것 
    class Meta:
        model = Score 
        fields =['name', 'kor', 'eng', 'mat']
        labels = {
            'name':"이름",
            'kor':'국어',
            'eng':'영어',
            'mat':'수학',
        }
