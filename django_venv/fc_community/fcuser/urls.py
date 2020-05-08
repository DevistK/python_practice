from django.urls import path
from . import views
urlpatterns = [
  path('register/', views.register, name="register"),
]

# path 의 name은 마음대로 정해줘도 됨
# 단 프로젝트의 url에서 admin은 실제 admin 정보를 담고 있기 때문에 바꾸면 안된다.