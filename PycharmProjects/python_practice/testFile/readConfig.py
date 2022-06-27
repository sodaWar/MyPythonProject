# encoding:utf-8
import configparser

cf = configparser.ConfigParser()
cf.read("config.ini")                                                                   #读取配置文件

def getDatabase(name):
    name = cf.get("DATABASE",name)
    print(name)

getDatabase("DATABASE")