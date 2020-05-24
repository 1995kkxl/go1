with open("./web_server.conf") as f:
    conf1 = f.read()
    conf = eval(conf1)
    print(conf)