import re

'''
URL_FUNC_DICT = {
    "/index.py":index,
    "/login.py":login
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

@route("/index.py")
def index():
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()
    return content

@route("/movie.py")
def login():
    with open("./templates/movie.html",encoding="utf-8") as f:
        return f.read()




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
    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        return URL_FUNC_DICT[file_name]()

    except Exception as ret:
        return "产生异常...%s" % str(ret)