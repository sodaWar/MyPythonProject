#!/usr/bin/env python
# encoding:utf-8
import requests
import json
import MySQLdb
import datetime
import config

if __name__ == '__main__':
    import sys

    id = 50811508
    # url = 'https://api.allfootballapp.com/data/match/50781797/phrase?version=200&platform=iOS&app='
    url = 'https://api.allfootballapp.com/data/match/' + str(id) + '/phrase?version=200&platform=iOS&app='
    time = datetime.datetime.now()        #当前时间
    config.env = sys.argv[1]                 #获取系统客户端输入值
    connection = MySQLdb.connect(
        host=config.config['env'][config.env]['host'],
        port=3306, user=config.config['env'][config.env]['user'], password=config.config['env'][config.env]['passwd'],
        db=config.config['env'][config.env]['db']
    )            #打开数据库连接，需要用户输入是为了适应不同的环境，连接不同的数据库，如开发、测试、线上的数据库
    sql = 'INSERT IGNORE INTO match_phrase (match_id, time, type, title, content, updateTime, createTime) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    cursor = connection.cursor()        # 获取操作游标
    rsp = requests.get(url)     #获取请求网址的数据
    data = rsp.text        #将数据保存在txt文件中
    jsonData = json.loads(data)          #将该json编码的字符串转换成python对象（python数据结构）
    mianData = jsonData['data']          #将抓取下来的接口中所有的数据做筛选，只要其中data模块中的数据，网页元素有<head>、<data>、<html>等许多分块。
    phrase = mianData['phrase']
    for i in range(phrase.__len__())[::-1]:
        temp = phrase[i]
        # print temp;
        params = [id, temp['time'], temp['type'], temp['title'], temp['content'], str(time), str(time)]
        cursor.execute(sql, params)       #执行SQL语句
    connection.commit()          #提交到数据库执行
    connection.close()          #关闭数据库连接
