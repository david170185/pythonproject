import pymysql #art+Enter
#DAO 역할 모듈 : CRUD(DML)

#정형데이터 => mysql, oracle, sqlite3(관계형 데이터베이스 관리 시스템, RDBMS)

def create2(data): #create2 vo 추가
    con = pymysql.connect(host = 'localhost', port = 3366, db = 'shop', user = 'root', password = '1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into bbs values (%s, %s, %s, %s)' #''' 따옴표 3개 사용시 여러줄 삽입 가능
    result = cur.execute(sql, data)
    print('처리 결과', result, '개')

    con.commit()
    con.close()

def read(): #read 1 = sql에 지정한거 가져오기
    # 1. mysql과 연결
    con = pymysql.connect(host='localhost', port=3366, db='shop', user='root', password='1234')
    print(con.get_host_info())

    # 2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    # 3. sql문을 만들어서 전송함.
    sql = "select * from bbs where id = 'com'"
    cur.execute(sql)

    row = cur.fetchone()
    # cur.fetchall() : 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany() : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(row)
    print(type(row))
    print(row[0]) #indexing

    con.close()

def update(id, tel):
    #1. mysql과 연결
    con = pymysql.connect(host='localhost', port=3366, db='shop', user='root', password='1234')
    print(con.get_host_info())

    #2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    # #3. sql문을 만들어서 전송함.
    # sql = "update member set tel = %s where id = %s"
    # cur.execute(sql, (tel, id)) #tuple로 넣어주어야 한다.

    #3-1. sql문을 만들어서 전송함.
    data = (tel, id)
    sql = "update bbs set tel = %s where id = %s"
    cur.execute(sql, data) #tuple로 넣어주어야 한다.

    #4. auto-commit이 안된다. 수동으로 반영시켜야 한다.
    con.commit()
    con.close()