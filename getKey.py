import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

def getKeys(text):
    word_list=[]
    address_list=[]
    muzuTan=takeMuzuTan()
    muzuTans=""
    for i in muzuTan:
        muzuLen=len(i)
        muzuTans+=f'[{i}]'+"{"+str(muzuLen)+'}|'
    findText=muzuTans+rf'[\u30A1-\u30FC]+|[\u0026\uFF06\u0041-\u005A\u0061-\u007A]+'
    result = re.finditer(findText, text)

    for i in result:
        word_list.append(i.group())
        address_list.append(i.start())
        address_list.append(i.end())
    
    address_list=sorted(address_list)

    return text,word_list,address_list

def findMean(word):
    try:
        word=word.encode('utf-8')
        uni=""
        for i in word:
            t=str(hex(i))
            t=t.replace("0x","%")
            uni+=t
        uni=uni.replace("a","A")
        uni=uni.replace("b","B")
        uni=uni.replace("c","C")
        uni=uni.replace("d","d")
        uni=uni.replace("e","E")
        uni=uni.replace("f","F")

        html = urlopen(f"https://kotobank.jp/word/{uni}")
        data = html.read()
        html = data.decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')

        text = soup.find(class_="description")

        txt=""
        a=0
        for i in list(text.text):
            if i=="。":
                a=1
            if a==0:
                txt+=i
            else:
                txt+="。"
                break
        txt=txt.replace(" ","")
        txt=txt.replace("(","")
        txt=txt.replace(")","")
        txt=txt.replace("\n","")
        return txt
    except:
        return "意味は見つかりませんでした"

def pushMean(words):
    means=[]
    for i in words:
        means.append(findMean(i))
    return means

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def takeMuzuTan():
    firebase()
    db = firestore.client()

    docs = db.collection("dic").stream()

    muzuTan=[]
    for doc in docs:
        muzuTan.append(doc.to_dict()["word"])

    return muzuTan

def firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate('sendic-643c7-firebase-adminsdk-siek8-d4f11b1edd.json')
        firebase_admin.initialize_app(cred)