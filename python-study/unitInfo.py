# Object 는 모든 객체의 상위 객체이므로
# py3 버전부터 클래스 괄호에 명시해줘도 되고 안해줘도 됨
# module화


class Unit():
    # Unit 이라는 공통 클래스로
    # 병사들(subclass,인스턴스)이 가져야할 유닛 공통사항
    # Unit 의 속성을 초기화 해줌
    # ex) 병사의 랭크 , 크기 , 생명력
    def __init__(self, rank, size, life):
        self.name = self.__class__.__name__
        # 매개변수가 없지만 부모 클래스에서 상속해주는
        # name 이라는걸 알 수 있다.
        self.rank = rank
        self.size = size
        self.life = life
    # 인스턴스(병사)들이 가질 속성들

    def show_status(self):
        print("이름 %s" % self.name)
        print("등급 %s" % self.rank)
        print("사이즈 %s" % self.size)
        print("라이프 %s" % self.life)

# 이제부터 병사 생성을 위한 정보
# 공통정보를 가진 고블린 종족을 생성


class Goblin(Unit):
    def __init__(self, rank, size, life, weaphon):
        # weaphon 매개변수는 고블린 클래스만이 갖는 인스턴스변수
        super().__init__(rank, size, life)
        self.weaphone = weaphon
    # 더 추가할 내용이 없으면 안적어도 됨
    # 부모 클래스를 상속받아서 쓸 수 있으니까

    def show_status(self):
        super().show_status()
        print("무기 %s" % self.weaphone)
    pass


class human(Unit):
    def __init__(self, rank, size, life):
        super().__init__(rank, size, life)
    pass


Goblin_1 = Goblin("병사", "Small", "100", "Wood")
Human_1 = human("병사", "big", "250")
