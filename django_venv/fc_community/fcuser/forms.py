from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': '아이디를 입력해주세요.'},
        max_length=32,
        label="사용자이름"
    )
    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'},
        widget=forms.PasswordInput,
        label="비밀번호"
    )

    def clean(self):
        # clean 메서드는 각 필드마다 값이 비어있는지 (clean) 확인한다.
        # 즉 유효성 검사를 위해 값을 저장하고 유지한다.

        cleaned_data = super().clean()  # clean 을 호출하여 값이 있는지 없는지 확인한다.
        username = cleaned_data.get('username')  # 값이 있으면 값을 가져와서 변수에 할당한다.
        password = cleaned_data.get('password')

        if username and password:
            # 이 모델안에 있는 username을 가져온다. 그리고 POST로 전송한 입력값이 모델안에 존재한다는 가정하에
            fcuser = Fcuser.objects.get(username=username)
            # 패스워드를 검사하는데 첫번째 인자로 전송한 데이터, 두번째 인자로 모델안에 있는 패스워드를 검사한다.
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else:
                # 일치하는 경우
                self.user_id = fcuser.id
                # self  > 이 로그인 폼 클래스의 변수임 , fcuser 모델의 id를 할당함
                # 바깥에서 사용할 수 있는 상태가 된것이다.
