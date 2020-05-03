# 파일을 불러와서 거기서 쓰거나 읽어올 수 있지만 
# 없는 파일을 만드는것도 가능하다.
with open('./read/Write.txt', 'w') as f :
    f.write("HI!")

from random import randint 
# 파일을 쓰기모드로 하고 random 텍스트파일을 생성해준다.
with open('./read/random.txt', 'w') as f :
  for i in range(7) :
    # 6자리의 숫자를 써줄건데 write는 문자열만 쓸 수 있으므로 문자열로 변환해준다.
    # 0~50까지의 난수가 랜덤 문자열로 파일에 쓰여진다.
    f.write(str(randint(0,50)))
    f.write("\n")


with open('./read/text.txt', 'a') as f :
  lists = ["1\n", "2\n", "3\n"]
  f.writelines(lists)