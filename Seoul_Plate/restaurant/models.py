from django.db import models


class Restaurant(models.Model):
    # help_text 사용 가능
    # null=False 이어야 할거 같음
    # TextField 필요 없음
    rest_name = models.CharField(default=None, help_text='식당 이름', max_length=200)
    rest_star = models.FloatField(null=True, default=None, help_text='별점')
    rest_address = models.CharField(null=True, default=None, help_text='주소', max_length=200)
    rest_phone_number = models.CharField(null=True, default=None, help_text='전화번호', max_length=200)
    rest_food = models.CharField(null=True, default=None, help_text='음식 종류', max_length=200)
    # 가격
    rest_sale = models.CharField(null=True, default=None, help_text='가격', max_length=200)
    # 영업 시간
    rest_time = models.CharField(null=True, default=None, help_text='영업 시간', max_length=200)
    # 쉬는 시간
    rest_break_time = models.CharField(null=True, default=None, help_text='쉬는 시간', max_length=200)
    # 북마크 개수
    # PositiveInt
    rest_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.rest_name
