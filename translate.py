import math
import urllib.parse
import requests
import json
import os
from html import unescape
from pathlib import Path

def translateApi(text, target_language,apiKey):
    msgToTranslate = text  
    requestTranslate = requests.get("https://translation.googleapis.com/language/translate/v2?key="+apiKey+"&q="+msgToTranslate+"&target="+str(target_language))
    translate = json.loads(requestTranslate.content)
    translate = translate['data']['translations'][0]['translatedText']       
    return unescape(translate)

text = str(input("\nInsert file path of text :\n"))
text = text.replace("\'","")[:-1]

lang = str(input("\nInsert target language  :\n"))

arrPath = text.split("/")
fileName = arrPath[len(arrPath)-1]
save_path = text.replace(fileName,"")
arrFile = fileName.split(".")
folderName = fileName.replace("."+(arrFile[len(arrFile)-1]),"")
save_path=save_path+folderName

fileNameTranslated = save_path+"_translated.txt"

os.system("touch "+fileNameTranslated)      

apiKey=""
p = Path(__file__).with_name('TRANSLATE_API_KEY')
api = open(p, 'r')
for l in api:
    apiKey=l


f = open(text, 'r')
paragraph = ""
p = ""
i=0
for line in f:
    lineP = list(line) 
    paragraph+=line
    i+=1
    if (len(lineP)>3):
        lineP = lineP[len(lineP)-3]
        if (lineP == "."):
            p = translateApi(paragraph,"pt",apiKey)
            os.system('clear')
            print ("Progress : "+str(round(((i/13205)*100),2))+"%\n")
            print (p)
            with open(fileNameTranslated, 'a') as arquivo:
                arquivo.write(p+"\n")           
            paragraph=""
os.system('clear')            
print ("100%\n")       
print (translateApi(paragraph,"pt",apiKey))       
with open(fileNameTranslated, 'a') as arquivo:
    arquivo.write(p)        


    




