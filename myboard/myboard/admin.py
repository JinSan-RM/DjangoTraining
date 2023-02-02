from django.contrib import admin
from .models import myboard        # 우리가 정의한 모델을 import

admin.site.register(myboard)