'''
文件：main.py
功能：提供抽奖小程序的后端
框架：flask
'''

from flask import Flask,render_template,redirect,url_for,jsonify
from utils.utils import read_person_name,config,rand_get_person,openBrowser
import threading

main_app=Flask(__name__,static_url_path="",static_folder="templates",template_folder="templates") #配置Flask实例
name_data=read_person_name("name.txt") #获取姓名

#下面开始写后端路由与API接口

@main_app.route("/")
def getin():
    return redirect(url_for("index"))

@main_app.route("/index")   #起始页路由
def index():
    return render_template("index.html")

@main_app.route("/lottery")  #抽奖页路由
def lottery():
    return render_template("new.html")

@main_app.route("/getone")  #抽人的API，返回一个json数据
def getone():
    return jsonify(rand_get_person(name_data))  #以json形式返回消息至前端


#启动！！
threading.Thread(target=openBrowser).start()
main_app.run(host="0.0.0.0",port=config.launch_port,debug=config.debug)