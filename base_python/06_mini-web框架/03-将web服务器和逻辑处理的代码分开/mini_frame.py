import time
def login():
	return "welcone to our website %s " % time.ctime()

def register():
	return "welcone to our website 这个是注册页面 %s " % time.ctime()

def profile():
	return "welcone to our website 这是profile页面 %s " % time.ctime()

def application(file_name):
	if file_name == "/login.py":
		return login()
	elif file_name == "/register.py":
		return register()
	else:
		return "not fond you page...."