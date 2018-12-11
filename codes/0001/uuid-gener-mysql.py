#生成200个激活码
import uuid
import pymysql
"""
UUID（Universally Unique IDentifier） 是128位的全局唯一标识符，通常由32字节的字符串表示。它可以保证时间和空间的唯一性，也称为 GUID（Globally Unique IDentifier）。

它通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的唯一性。
"""
def generater(num):
    ticket_list = []
    for i in range(0,num):
        ticket_list.append(str(uuid.uuid4()))
    return ticket_list

def mysql_connecter():
    db = pymysql.connect('104.225.238.182','sswu','sswu','test')
    cursor = db.cursor()
    return (db,cursor)

if __name__ == "__main__":
    # print(generater(2))
    db, cursor = mysql_connecter()
    # print(len(generater(20)))
    for ticket in generater(20):
        try:
            sql = "insert into uuid (uuid) values ('" + ticket +"')"
            # print(sql)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
    db.close()
    print('ok')