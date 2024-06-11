'''
文件：utils.py
功能：为后端主程序提供其他功能
'''

import random
import webbrowser

import yaml
import os
import utils.extra
import utils.lconfig
from  urllib import request
import time

'''
函数：init_data
参数：配置文件路径（*.yaml)
功能：预加载图片数据
返回值类型：list
'''

def init_data(config_filepath:str)->utils.lconfig.Config:
    #开始读取配置文件
    try:
        with open(os.path.abspath(config_filepath),"r",encoding="utf-8") as f:   #这里转换成绝对路径
            config_data=yaml.load(stream=f,Loader=yaml.FullLoader)
            config=utils.lconfig.Config(config_data["photo_path"],config_data["launchPort"],config_data["debug"])
            return config
    except Exception as e:
        print("read config file error:"+str(e))
        return None

config=init_data("config.yaml")
photos=utils.extra.getPhotoList(config.photo_path)

'''
函数：read_person_name
参数：每行包含一个名字的文件的路径
功能：为main提供姓名
返回值类型：list
'''

def read_person_name(filename:str)->list:
    namelist=[]
    result=[]
    with open(filename,"r",encoding="utf-8") as f:
        namelist=f.readlines()
    for name in namelist:
        result.append(name.strip("\n"))
    return result



'''
函数：rand_get_person
参数：名字列表(list类型)
功能：得到一个人的数据并以dict形式返回
返回值类型：dict
'''

def rand_get_person(namelist:list)->dict:
    _person=random.choice(namelist)  #得到一个人
    _photo=utils.extra.searchPhoto(_person,photos)
    if _photo==None:
        _photo="/assets/default.jpg"         #如果没找到图片就用默认头像
    else:
        _photo="/assets/"+_photo.split("\\")[-1]
    return {"person":_person,"has_photo":True,"photo":_photo}


'''
函数：openBrowser
参数：无
功能：在后端服务成功启动后打开浏览器（前端）
返回值类型：none
'''

def openBrowser()->None:
    while True:
        try:
            request.urlopen("http://127.0.0.1:"+str(config.launch_port))           #尝试访问后端
            break
        except Exception as e:
            time.sleep(0.3)          #等待后重试
    webbrowser.open("http://127.0.0.1:"+str(config.launch_port))           #循环结束，打开后端