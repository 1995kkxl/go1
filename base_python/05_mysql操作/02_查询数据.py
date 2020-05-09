from pymysql import connect

class JD(object):
    def __init__(self):
        pass

    def show_all_items(self):
        '''显示所有商品'''
        # 创建connection连接
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='19951023chen',
                       charset='utf8')
        # 获得Cursor对象
        cursor = conn.cursor()
        # 执行sql语句，并返回影响的行数；查询一条数据
        sql = 'select * from goods;'
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)

        cursor.close()
        conn.close()

    def show_cates(self):
        '''显示所有商品'''
        # 创建connection连接
        conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='19951023chen',
                       charset='utf8')
        # 获得Cursor对象
        cursor = conn.cursor()
        # 执行sql语句，并返回影响的行数；查询一条数据
        sql = 'select name from goods_cates;'
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)

        cursor.close()
        conn.close()

    def run(self):
        while True:
            print("-------京东------")
            print("1：所有的商品")
            print("2.所有商品的分类")
            print("3.所有商品品牌分类")
            num = input("请输入功能相对应的序号： ")

            if num == "1":
                #查询所有商品
                self.show_all_items()
            elif num == "2":
                #查询分类
                pass
            elif num == "3":
                #查询品牌分类
                pass
            else:
                print("输入有误，请重新输入。。。")


def main():
    #1. 创建一个京东商城对象
    JD()

    #2.嗲用这个对象的run 方法，让其运行
    JD.run()
if __name__ == '__main__':
    main()