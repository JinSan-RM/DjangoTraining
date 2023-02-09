from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['b_title','b_author','b_content']

        labels = {
            'b_title' : '글 제목',
            'b_author' : '글 작성자',
            'b_content' : '글 내용'
        }

        widgets = {
            'b_title' : forms.TextInput(
                attrs={
                    'class':'form-control w-50',
                    'placeholder':'글 제목을 입력하세요',
                }
            ),
            'b_author' : forms.TextInput(
                attrs={
                    'class':'form-control w-25',
                    'placeholder':'글 작성자를 입력하세요',
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class' : 'form-control w-75',
                    'placeholder':'글 작성자를 입력하세요',
                }
            )
        }

class BoardDetailForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'

        labels = {
            'b_title' : '글 제목',
            'b_author' : '글 작성자',
            'b_content' : '글 내용',
            'b_comment_count': '댓글 개수',
            'b_like_count' : '좋아요 개수'
        }
        widgets = {
            'b_title' : forms.TextInput(
                attrs={
                    'class':'form-control w-50',
                }
            ),
            'b_author' : forms.TextInput(
                attrs={
                    'class':'form-control w-25',
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class' : 'form-control w-75',

                }
            ),
            'b_comment_count':forms.TextInput(
                attrs={
                    'class':'form-control w-25',
                }
            ),
            'b_like_count':forms.TimeInput(
                attrs={
                    'class':'form-control w-25',
                }
            )

        }
    
    def show_board_detail(self):
        fields = list(BoardDetailForm().base_fields)
        for field in fields:
            self.fields[field].widget.attrs.update({
                'readonly' : 'readonly'
            })

    def show_board_update(self):
        self.fields['b_like_count'].widget.attrs.update({
            'readonly' : 'readonly'
        })
        self.fields['b_comment_count'].widget.attrs.update({
            'readonly' : 'readonly'
        })