from pymysql import connect


# 创建索引
# create index title_index on test_index(title(10));

def main():
    #创建Connection连接
    conn = connect(host="127.0.0.1",database="jing_dong",user="root",password="19951023chen",charset="utf8")
    #获得cursor对象
    cursor = conn.cursor()
    #插入十万条数据
    for i in range(100000):
        cursor.execute("insert into test_index values ('ha-%d')" % i)
        #提交事务
    conn.commit()
if __name__ == '__main__':
    main()