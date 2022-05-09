# -2020-05-03-

## 파이썬에서 데이터베이스

*  *  *   *  *  
[파이썬 SQLite 공식문서](https://docs.python.org/ko/3/library/sqlite3.html)

- DB 연동
파이썬에는 자체적으로 내장하고 있는 sqlite 모듈이 있다.
그래서 기본적으로 sqlite 프로그램 하나만 설치해주면 매우 간편히 사용가능하다.

```{.python}
import sqlite3
```

똑같이 모듈을 불러와서 사용하면 되는데 이때 DB에 접속을 해줘야한다.

```{.python}
con = sqlite3.connect('db경로/file.db')
c = con.cursor()
```

db는 COMMIT 을 해주지 않으면 실제로 데이터가 저장되지 않는다.
con.commit() 을 해주면 커밋되어 데이터가 저장된다.

수동으로 커밋을 해도 되지만
sqlite3.connect('db경로/file.db', isolation_level=None)
처음에 접속할때 isolation_level을 None 으로 지정해 줄 수 있다.
이건 커밋을 자동으로 해주기 때문에 일일이 커밋을 해줄 필요가 없다.

con 변수에 할당한 sqlite3.connect() 는 해당 경로에 있는 db에 접속한다는 것이다.

만약 없는 db 파일이라면 db파일 생성과 동시에 접속이 가능한것이다.
(내 피셜)

con.cursor()는 커서라는 객체를 가지고 있는데 이 커서는
한마디로 해당 DB에 상호작용을 할 수 있게 해주는 역할을 한다 보면 되겠다.

- DB TABLE 생성 및 데이터 삽입

```{.python}

c.execute("CREATE TABLE userInfo(id INTGER PRYMARY KEY , name text, age text, address text )")

c.execute("INSERT INTO userInfo(id, name, age, address) VALUSE(1, 'Kim', '25', 'Incheon')")

```

간단하게 테이블을 생성하고 컬럼 리스트를 만들어 데이터를 삽입해보았다.

여기서 execute란 실행하는 함수이다.
프로그램에서 exe 를 생각하면 이해가 가는것 같다.

잘 살펴보면 execute 함수 안에는 꽤나 긴 문자열이 나열해 있는데,
CREATE TABLE 테이블명 = 테이블을 생성한다.

userInfo 테이블명 안의 문자열들은 생성할 테이블의 컬럼 리스트 들이다.
컬럼리스트는 type을 지정해 줄 수 있다.

sql 에서 지정된 type 들이 몇가지 있다.

- 숫자형 TINYINT, INT, FLOAT.
- 문자형 CHAR, VARCHAR, TEXT, ENUM.
- 날짜형 DATE, DATETIME, TIMESTAMP.

이정도가 되겠다.

여기서 첫번째 컬럼리스트에 지정한 PRYMARY KEY는
중복이 안되는 고유 값이다.

아래의 INSERT INTO userInfo 는 해당 테이블에 데이터를 삽입한다는 뜻
VALUSE() 이안에 삽입할 데이터를 적는다.
데이터의 갯수는 컬럼리스트와 동일해야 매핑 가능함

### 매번 이렇게 하나씩 생성해주면

😅😅😅 생각만 해도 불편하다..

그럼 복수의 데이터를 삽입할때는 어떻게 해야하는가

execute 대신 executemany 를 사용하면 된다.
executemany로 여러 데이터를 삽입할 수 있다.

```{.python}
datalist = (
    (2, 'Kim', '25', 'Incheon'),
    (3, 'Kim', '25', 'Incheon'),
    (4, 'Kim', '25', 'Incheon'),
    (5, 'Kim', '25', 'Incheon')
    )
inserts = "INSERT INTO userInfo(id, name, age, address) VALUSE(?,?,?,?)"
c.executemany(inserts, datalist)
```

이렇게 써주면 테이블에 여러개의 데이터가 삽입이 된다.
여기서 나는 inserts 안에 sql문을 작성했고 VALUSE 부분을 보면
직접 데이터를 넣지 않고 ? 로 치환할 수 있다.

그럼 executemany의 두번째 인자로 들어온 datalist가
VALUSE 에 차례대로 매핑이 되면서 데이터가 삽입 되게 되는것이다.
튜플 > 튜플 형태로 데이터로  넣는데 리스트로 넣을 수 도 있다.

물론 넣어야하는 데이터가 변수에 들어있어도 위의 ? 로 치환해
데이터 삽입이 가능하다.

예를들면
(5, 'Kim', '25', timedata ) 이렇게도 가능

마지막으로 db에 접속했으면 종료도 해야한다.

con.close()
이렇게 종료해주면 db 접속이 종료된다.

어디서 비슷한걸 본적이 있는데

```{.python}

f = open('file', 'w')
    f.write("Hello World")
f.close()

```

파일 읽고 쓰는데에서도 쓰인다.
