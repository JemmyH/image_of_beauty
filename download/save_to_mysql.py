# _*_ coding:utf-8 _*_

import pymysql

conn = pymysql.Connect(host="127.0.0.1", port=3306, user="hujiaming", passwd="123456", db="xgyw_cc", charset="utf8")
cur = conn.cursor()
start_url = "http://www.xgyw.cc"
little_item_sql = "insert into little_item values"

def combine_insert_sql(table_name, id, name, url):
    insert_big_sql = "insert into {0} values".format(table_name)
    for i in range(0, len(id)):
        url[i] = start_url + url[i]
        insert_big_sql += '({0},"{1}","{2}"),'.format(id[i], name[i], url[i])
    print(insert_big_sql)
    # cur.execute(insert_big_sql[:-1])

def get_one_little_item(id, p_id, name, url):
    global little_item_sql
    little_item_sql += "({0},{1},'{2}','{3}'),".format(id, p_id, name, url)
    print(little_item_sql)

def print_little_item_sql():
    print(little_item_sql)


def save():
    conn.commit()