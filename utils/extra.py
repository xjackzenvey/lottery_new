'''
文件:extra.py
功能：给utils提供一些额外的功能，使其简洁化。
'''

import glob
import random

'''
函数：getPhotoList
参数：照片存储的绝对路径
返回值：所有照片的列表
功能：预加载照片列表，避免重复查找，提升效率
'''

def getPhotoList(photo_path:str)->list:
    files=glob.glob(photo_path+"/*")
    for file in files:
        file=file.split("\\")[-1]
    return files


'''
函数：searchPhoto
参数：人名，照片列表
返回值：找到返回照片文件名，否则返回None
功能：查找照片
'''

def searchPhoto(person:str,photo_files:list)->str:
    avaliable=[]
    for file in photo_files:
        if person in file:
            avaliable.append(file)
    if len(avaliable)==0:
        return None
    return random.choice(avaliable)