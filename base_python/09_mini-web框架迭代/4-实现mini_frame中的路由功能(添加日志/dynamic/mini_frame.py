import logging
import regex as re
from pymysql import connect
'''
URL_FUNC_DICT = {
    "/index.html":index,
    "/login.html":login
}

'''

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        #URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args,**kwargs):
            return call_func(*args,**kwargs)
        return call_func
    return set_func

@route("/index.html")
def index():
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()
    return content

@route("/movie.html")
def login():
    with open("./templates/movie.html",encoding="utf-8") as f:
        content =  f.read()

    #数据库
    conn = connect(host="localhost", port=3306, user='root', password='19951023chen', database='douban', charset='utf8')
    # 获得cursor对象
    cs = conn.cursor()
    sql = 'select * from movie250;'
    cs.execute(sql)
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """
        <td>%s</td>
        <td><img src="%s" width="60" height="90"></td>
        <td>
        <a href="%s" target="_blank">
        {{ m%s }} </a>
        </td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td><input type="button" value="修改" id="toAdd" name="toAdd" systemidvalue=""></td>
        </tr>
    
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],line_info[2],line_info[1],line_info[3],line_info[4],line_info[5],line_info[6],line_info[7],line_info[8])


    #content = re.sub(r"\{%content%\}",str(stock_infos), content)
    content = re.sub(r"\{%content%\}",html, content)

    return content

def application(env,start_response):
    start_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
    file_name = env['PATH_INFO'] #(PATH_INFO:/index.py)

    '''
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return "hello world 我爱你哦中国香港!中国澳门!中国台湾!"
    '''
    logging.basicConfig(level=logging.INFO,file_name='./log.txt',filemode='a',format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s')
    logging.info("访问的是，%s" % file_name)


    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        return URL_FUNC_DICT[file_name]()

    except Exception as ret:
        logging.info("产生异常%s" % ret)
        return "产生异常...%s" % str(ret)