import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name, img_url):
	req = urllib.request.urlopen(img_url)

	img_content =req.read()

	with open(img_name,"wb") as f:
		f.write(img_content)

def main():
	gevent.joinall([
		gevent.spawn(downloader,"1.jpg","https://wx4.sinaimg.cn/mw690/bde8475dly1g4l8p5hthyj22c02c0hdu.jpg"),
		gevent.spawn(downloader,"2.jpg","https://wx2.sinaimg.cn/mw690/bde8475dly1g4l8p5zexuj22c02c0kjm.jpg")
		])




if __name__ == '__main__':
	main()