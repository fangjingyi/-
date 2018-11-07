# coding=utf-8
# -*- coding: cp936 -*-
import jieba
import jieba.posseg as pseg
import codecs
import re
import os
import time
import string
from nltk.probability import FreqDist

#处理实验数据 ： 将标签处理成one-hot形式  提取句子中的名词
#f是源文件 f1是转换后的文件 filelong是要转换的行数（按f中的行数算）
def changefile(f,f1,filelong):
    #将标签设计成one-hot形式
    def change(word):
        #标签
        law = ["history","military","baby","world","tech","game","society","sports","travel","car","food","entertainment","finance","fashion","discovery","story","regimen","essay"]
        new = ""
        for a in law:#替换标签
            if word == a:
                new += "1"
            else:
                new += "0"
        return new
    
    #提取名词
    def have(word):
        law = ["n","nr","nr1","nr2","nrj","nrf","ns","nsf","nt","nz","nl","ng"] #jieba分词中的所有名词类型
        law1 = ["a","ad","an","ag","al","v","vd","vn","vshi","vyou","vf","vx","vi","vl","vg"] #所有形容词和动词类型
        for a in law:
            if word == a:
                return True
        return False
    
    for a in range(filelong):
        words = pseg.cut(f.readline())  #分词
        i = 1
        for w in words:
            if i==1:
                f1.write(change(w.word)+" ")
            i = i + 1
            if have(w.flag):
                f1.write(w.word+" ")
        f1.write("\n") 
        
    f.close()
    f1.close()
    #end
