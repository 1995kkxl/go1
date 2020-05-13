import multiprocessing
import os


def copy_file(q, file_name, old_folder_name, new_folder_name):
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 拷贝完成，向队列中写入一个消息，表示已经完成
    q.put(file_name)


def main():
    # 1\获取用户要copy的文件夹的名字
    old_folder_name = input("请你输入需要copy的文件夹的名字:")
    # 2\创建一个新文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    # 3\获取文件夹内所有文件的名字， listdir()
    file_names = os.listdir(old_folder_name)
    # 4\创建进程池
    po = multiprocessing.Pool(5)

    # 5\创建一个队列
    q = multiprocessing.Manager().Queue()  # 注意进程池创建队列使用Manager而不是直接创建

    # 6\向进程池里面添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    po.close()
    # po.join()
    all_file_num = len(file_names)
    copy_complete = 0
    while True:
        file_name = q.get()
        copy_complete += 1
        # print("已经完成{}文件的复制".format(file_name))
        # print("拷贝的进度为：%.2f%%" % (copy_complete*100 / all_file_num),end="") # end=“”表示不换行
        print("\r拷贝的进度为：%.2f%%" % (copy_complete * 100 / all_file_num), end="")  # \r表示打印回到当前行首，覆盖第一次的数据

        if (copy_complete >= all_file_num):
            break


if __name__ == "__main__":
    main()