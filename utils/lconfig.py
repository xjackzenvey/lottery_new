'''
文件：lconfig.py
功能：这个文件只有一个config类，是utils.py包的一个依赖项
        只是不想写一个文件里罢了
'''

#Config类,包含了utils中init_data返回的数据,别无作用
class Config:
    def __init__(self,photo_path:str,port:int,debug:bool):
        self.photo_path=photo_path
        self.launch_port=port
        self.debug=debug