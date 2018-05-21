# _*_ coding:utf-8 _*_
import os
import urllib.request


def download_image(img_url, path):
    try:
        print(path)
        if os.path.exists(path):
            pass  # 如果该文件存在，则跳过执行保存操作，这方便中断爬虫之后再重新启动
        else:
            urllib.request.urlretrieve(img_url, path)  # 根据传进来的url下载图片并保存在设定的文件夹中
    except Exception:
        pass  # 出现某个错误或异常则跳过不影响整个程序的继续运行
def new_download(img_url,path):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(img_url, path)

