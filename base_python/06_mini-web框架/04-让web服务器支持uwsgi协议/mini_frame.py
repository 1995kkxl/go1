def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
	return "hello world 我爱你哦中国香港!中国澳门!中国台湾!"