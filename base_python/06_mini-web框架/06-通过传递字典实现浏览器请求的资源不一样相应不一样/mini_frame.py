
def index():
	return "这是主页"

def login():
	return "这是登录页面"
def application(env,start_response):
	start_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
	file_name = env['PATH_INFO'] #(PATH_INFO:/index.py)
	if file_name == "/index.py":
		return index()
	elif file_name == "/login.py":
		return login()
	else:
		return "hello world 我爱你哦中国香港!中国澳门!中国台湾!"