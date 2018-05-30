# _*_ coding:utf-8 _*_

from qiniu import Auth
from qiniu import BucketManager, build_batch_stat

access_key = 'xxxxxxxxxxxx'
secret_key = 'xxxxxxxxxxxx'
q = Auth(access_key, secret_key)
bucket = BucketManager(q)
bucket_name = 'xgyw'
# url = 'http://xgyw.tpzy5.com/uploadfile/201805/8/60222523906.jpg'
# key = '001.jpg'
# ret, info = bucket.fetch(url, bucket_name, key)
# print(info)
# assert ret['key'] == key


def upload_image(url):
    key = url[42:]
    ret, info = bucket.fetch(url, bucket_name, key)
    print(info)
    assert ret['key'] == key


def check(key):
    ops = build_batch_stat(bucket_name, key)
    ret, info = bucket.batch(ops)
    print(info)
# if __name__ == '__main__':
    # upload_image('http://www.xgyw.cc/uploadfile/201804/7/52114822289.jpg')
