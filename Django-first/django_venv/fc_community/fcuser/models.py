from django.db import models

# Create your models here.
# 하나의 클래스로 데이터를 정의 하는데 
# 클래스 하나가 테이블 하나를 정의한다.
# 그래서 인스턴스변수가 아닌 클래스 변수로 필드를 정의하는것이다.

# Model 데이터 정의가 되면 상태를 반영해줘야하는 makemigrations를 명령한다
# 최종적으로 저장이 되면 migrate로 실제 DB를 생성
class Fcuser(models.Model) :
  username = models.CharField(max_length=32, verbose_name='사용자명')

  useremail = models.EmailField(max_length=130, verbose_name='사용자이메일')

  password = models.CharField(max_length=64, verbose_name='비밀번호')

  registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

  # str 함수로 클래스 문자열을 반환한다.
  def __str__(self) :
    return self.username

  class Meta :
    db_table = 'Fastcampus_fcuser'
    verbose_name = "언어 리스트"
    verbose_name_plural = '언어 리스트'