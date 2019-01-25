# -* encoding:utf-8 *-
import pymysql
import traceback


def connectdb():
    print("正在连接服务器.....")
    db = pymysql.connect(
        host="34.235.86.20",
        port=3306,
        user="sokamgrdev",
        password="sokamgr@Pwd",
        charset="utf8mb4",
        db="sokadb"
     #   cursorclass=pymysql.cursors.DictCursor
    )
    print("连接服务器成功")
    return db


def selectdb(db):
    cursor = db.cursor()
    sql = "select * from article WHERE id = '%d'"%(102)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            print ("查询结束，数据库无数据")
        else:
            for row in result:
                print row
                id = row[0]
                title = row[1]
                content = row[2]
                small_cover = row[3]
                create_time = row[9]
                print "id:%d,title:%s,content:%s,small_cover:%s,create_time:( %s)" \
                      %(id,title,content,small_cover,create_time)
    except:
        print ("查询数据失败")
        #traceback.print_exc()
        raise
    else:
        print("查询数据成功")

def deletedb(db):
    cursor = db.cursor()
    sql = "delete from article WHERE id = '%d'" % (102)
    try:
        cursor.execute('delete from article  WHERE  id = 102')
        db.commit()
    except:
        print("删除数据失败")
        db.rollback()
        traceback.print_exc()
    else:
        print("删除数据成功")

def insertdb(db):
    cursor = db.cursor()
    sql = "insert into tag(id,name,status_flag) VALUES ('%d','%s','%d')" %(6,'测试6',0)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print ("新增数据失败")
        db.rollback()
        traceback.print_exc()
    else:
        print ("新增数据成功")

# 批量插入数据
def batchdb(db):
    cursor = db.cursor()
    values = [7,'测试7',0]
    for i in range(8, 12):
        y = '测试'+str(i)
        z = '测试'+str(i-1)
        values = [i if x == i-1 else x for x in values]
       # print values
        values = [y if h == z else h for h in values]
        print values
        cursor.execute("insert into tag(id,name,status_flag) VALUES (%s,%s,%s)",[str(x) for x in values])
        db.commit()

def updatedb(db):
    cursor = db.cursor()
    sql = "update tag set name = '%s'  WHERE id = '%d'" %('测试1',1)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print ("更新数据失败")
        db.rollback()
        traceback.print_exc()
    else:
        print("更新数据库成功")
def closedb(db):
    db.close()


def main():
    db = connectdb()
    selectdb(db)
    #deletedb(db)
    #insertdb(db)
    #updatedb(db)
    #batchdb(db)
    closedb(db)
    print("关闭数据库成功")


if __name__ == "__main__":
    main()


