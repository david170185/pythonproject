import db연결.mysql_bbs.bbs_dao as db

id = input('수정할 아이디를 입력하세요')
tel = input('수정할 전화번호를 입력하세요')

db.update(id, tel)
