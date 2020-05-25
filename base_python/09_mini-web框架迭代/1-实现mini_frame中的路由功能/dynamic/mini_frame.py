import re

def index():
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()
    return content

def login():
    with open("./templates/post.html",encoding="utf-8") as f:
        return f.read()


URL_FUNC_DICT = {
    "/index.py":index,
    "/login.py":login
}


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
    func = URL_FUNC_DICT[file_name]
    return func()