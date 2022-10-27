#!/usr/bin/python
# -*-coding:utf-8-*-    
  
#===============================================================================  
# 目录对比工具(包含子目录 )，并列出
# 1、A比B多了哪些文件  
# 2、B比A多了哪些文件  
# 3、二者相同的文件: md5比较
#===============================================================================  

import sys
import os
import time
import difflib
import hashlib


def getFileMd5(filename):
    if not os.path.isfile(filename):
        print('file not exist: ' + filename)
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def getAllFiles(path):
    flist=[]
    for root, dirs , fs in os.walk(path):
        for f in fs:
            f_fullpath = os.path.join(root, f)
            f_relativepath = f_fullpath[len(path):]
            flist.append(f_relativepath)
    return flist

def dirCompare(apath,bpath):
    afiles = getAllFiles(apath)
    bfiles = getAllFiles(bpath)

    setA = set(afiles)
    setB = set(bfiles)

    commonfiles = setA & setB  # 处理共有文件

    for f in sorted(commonfiles):
        amd=getFileMd5(apath+'/'+f)
        bmd=getFileMd5(bpath+'/'+f)
        if amd != bmd:  
            print ("dif file: %s" %(f))

    # 处理仅出现在一个目录中的文件
    onlyFiles = setA ^ setB
    onlyInA = []
    onlyInB = []
    for of in onlyFiles:
        if of in afiles:
            onlyInA.append(of)
        elif of in bfiles:
            onlyInB.append(of)
            
    if len(onlyInA) > 0:
        print ('-' * 20,"only in ", apath, '-' * 20)
        for of in sorted(onlyInA):
            print (of)
            
    if len(onlyInB) > 0:
        print ('-' * 20,"only in ", bpath, '-' * 20)
        for of in sorted(onlyInB):
            print (of)
            
node = {
    "a" : "10.131.121.236",
    "b" : "10.131.122.10",
    "c" : "10.131.122.11",
    "d" : "10.131.122.6",
    "e" : "10.131.122.8",
    "f" : "10.131.122.9",
    "g" : "10.131.129.199",
    "h" : "10.131.129.202",
    "i" : "10.131.130.42",
    "j" : "10.131.228.66",
    "k" : "10.188.53.83",
    "l" : "10.188.54.19",
    "m" : "10.188.64.221",
    "n" : "10.188.64.96",
    "o" : "10.188.64.98",
}
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        node1, node2 = sys.argv[1:3]
        aPath = os.getcwd()+'/' + node[node1]
        bPath = os.getcwd()+'/' + node[node2]
        dirCompare(aPath, bPath)
    else:
        keys = node.keys()
        for (a,b) in [(x,y) for x in keys for y in keys]:
            if a != b:
                a_path = os.getcwd()+'/' + node[a]
                b_path = os.getcwd()+'/' + node[b]
                print(a,b)
                dirCompare(a_path, b_path)
        
    print("\ndone!")

