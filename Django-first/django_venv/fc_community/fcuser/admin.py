from django.contrib import admin
from .models import Fcuser # DB를 받아와야 해서 모델을 불러오는것

# FcuserAdmin 클래스가 상속받은 ammin.ModelAdmin으로 
# Admin 에 관련된 기능을 쓸 수 있다.
class FcuserAdmin(admin.ModelAdmin) :
  list_display = ('username', 'useremail', 'password') 
  # list_dispaly 로 페이지에 나타나는 필드를 제어 한다.
  pass

# admin 사이트에 등록할 모델  , 옵션
admin.site.register(Fcuser,FcuserAdmin)
