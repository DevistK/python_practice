# 101
# 사용자로부터 입력받은 문자열을 두 번 출력하라.
# print(input() * 2)

# 102
# 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# a = input()
# a = int(a)
# b = a + 10
# print(b)

# 103
# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# a = input()
# a = int(a)
# if a % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# 104
# 사용자로부터 값을 입력받은 후 해당 값에 +20을 더한 값을 출력하라. 단 값의 범위는 0~255로 가정한다. 255를 초과하는 경우 255를 출력해야 한다.
# a = int(input())
# a = a + 20
# if a > 255:
#     print(255)
# else:
#     print(a)

# 105
# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 값의 범위는 0~255이다. 0보다 작은 값이되는 경우 0을 출력해야 한다.

# a = int(input())
# a = a - 20
# if a < 0:
#     print(0)
# else:
#     print(a)

# 106
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# time = input()
# if time[3:] == "00" :
#   print("정각 입니다")
# else :
#   print("정각이 아닙니다.")

# 107
#사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = ["사과", "포도", "홍시"]
# likeFruit =  input("좋아하는 과일은?")
# if likeFruit in fruit :
#   print("정답입니다.")
# else :
#   print("오답입니다.")

# 108
# 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# inlist = input()
# if inlist in warn_investment_list :
#   print("투자 경고 종목입니다")
# else :
#   print("투자 경고 종목이 아닙니다")

# 109
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# myseason = input("제가 가장 좋아하는 계절은 :")
# if myseason in fruit.key() : default 값은 key만 보여준다.
#   print("좋아하는 계절은 {} 입니다.".format(myseason))
# else : 
#   print("목록에 없습니다.")

# 110
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# myfruit = input("제가 가장 좋아하는 과일은 :")
# if myfruit in fruit.values() :
#   print("좋아하는 과일은 %s 입니다." % myfruit)
# else :
#   print("목록에 없습니다.")