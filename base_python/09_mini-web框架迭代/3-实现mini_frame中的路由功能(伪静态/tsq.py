from pymysql import connect
#数据库
conn = connect(host="localhost",port=3306,user='root',password='19951023chen',database='douban',charset='utf8')
#获得cursor对象
cs = conn.cursor()
sql = 'select * from movie250;'
cs.execute(sql)
stock_infos = cs.fetchall()
print(str(stock_infos))
cs.close()
conn.close()