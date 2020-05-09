from pymysql import connect

class JD(object):
    def __init__(self):
        #1. Connection连接
        self.conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='19951023chen',charset='utf8')
        #2. 获得Cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        #关闭
        self.cursor.close()
        self.conn.close()

    def execute_sql(self,sql):
        #执行sql
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        '''显示所有商品'''
        # 执行sql语句，并返回影响的行数；查询一条数据
        sql = 'select * from goods;'
        self.execute_sql(sql)



    def show_cates(self):
        '''显示所有商品'''
        sql = 'select name from goods_cates;'
        self.execute_sql(sql)

    def show_brands(self):
        '''显示所有商品'''
        sql = 'select name from goods_brands;'
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("-------京东------")
        print("1：所有的商品")
        print("2.所有商品的分类")
        print("3.所有商品品牌分类")
        print("Q或者q退出程序")
        num = input("请输入功能相对应的序号： ")
        return num
    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                #查询所有商品
                self.show_all_items()
            elif num == "2":
                #查询分类
                self.show_cates()
            elif num == "3":
                #查询品牌分类
                self.show_brands()
            elif num == "q" or num == "Q":
                #退出
                break
            else:
                print("输入有误，请重新输入。。。")


def main():
    #1. 创建一个京东商城对象
    jd = JD()

    #2.嗲用这个对象的run 方法，让其运行
    jd.run()
if __name__ == '__main__':
    main()