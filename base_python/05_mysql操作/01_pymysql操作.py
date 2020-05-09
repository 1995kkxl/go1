from pymysql import *

def main():
    #创建connection连接
    #conn = connect(host='localhost',user='root',password='19951023chen',database='jing_dong',charset='utf8')
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='19951023chen', charset='utf8')
    #获得Cursor对象
    cs1 = conn.cursor()
    #执行sql语句，并返回影响的行数；查询一条数据
    sql = 'select * from goods'
    count = cs1.execute(sql)
    #打印
    print("查询到%d调数据" % count)

    for i in range(count):
        #获取查询的结果
        result = cs1.fetchone()
        #打印
        print(result)

    #关闭cursor对象
    cs1.close()
    conn.close()
if __name__ == '__main__':
    main()