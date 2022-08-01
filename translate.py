import urllib.parse
import requests
import json
import os
from html import unescape

def translateApi(text, target_language):
    msgToTranslate = text  
    requestTranslate = requests.get("https://translation.googleapis.com/language/translate/v2?key=AIzaSyDi6uUSONVafQJOKx3XQ_xeBMqW2_rO1vI&q="+msgToTranslate+"&target="+str(target_language))
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
            p = translateApi(paragraph,"pt")
            os.system('clear')
            print ("Progress : "+str((i/13205)*100)+"%\n")
            print (p)
            with open(fileNameTranslated, 'a') as arquivo:
                arquivo.write(p+"\n")        
            paragraph=""
print ("100%\n")       
print (p)       
with open(fileNameTranslated, 'a') as arquivo:
    arquivo.write(p)        


    




