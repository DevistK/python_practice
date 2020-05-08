from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Fcuser
# Create your views here.

def register(request) :
  # views에서 로직을 만들때 메서드에 request를 무조건 받게 되있다.
  # request로 요청을 하기 때문에

  # 템플릿에서 form 요청 방식이 GET 이거나 POST일때
  # form 데이터를 전달하게된다.
  if request.method == 'GET' :
    return render(request, 'register.html')
  elif request.method == 'POST' :
    # POST로 요청할때 form 안에 있는 데이터를 받아 올 수 있도록
    # 각 input의 name 값을 입력해준다 .
    # 즉 name = key 값이 되는것이다.
    username = request.POST.get('username', None)
    useremail = request.POST.get('useremail', None)
    password = request.POST.get('password', None)
    re_password= request.POST.get('re-password', None)

    # key 값을 받아 왔으니 넘어갈 데이터를 받아줄 클래스 모델을 가져온다.
    # Models 에서 가져온 클래스(테이블) Fcuser의 클래스 변수에
    # 방금 POST에서 가져온 name(key) 를 변수에 할당한다.
    res_data = {}
    if not (username and password and re_password and useremail) :
      res_data['error'] = "모든 값을 입력하지 않았습니다."
    elif password != re_password :
      res_data['error'] = "비밀번호가 일치하지 않습니다."
    else :
      fcuser = Fcuser(
        # models 에서 생성한 테이블 클래스를 불러와서 필드 변수에 사용자로부터 받은 값을 할당해준다.
        username = username,
        useremail = useremail,
        password = make_password(password)
      )


    # 테이블에 데이터를 저장한다.
      fcuser.save()

    # rennder 가 POST 값을 가진 templates을 요청하면
    # url로 전송된다.
    return render(request, 'register.html', res_data)