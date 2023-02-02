from django.contrib import admin    # admin을 위해서 만들어준 라이브러리
from .models import Myboard         # 우리가 정의한 모델을 import

admin.site.register(Myboard)

