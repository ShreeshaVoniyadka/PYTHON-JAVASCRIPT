import os
from gtts import gTTS
language='en'
file=input("enter the file to read: ")
fn=open(file+".txt","r")
exe=fn.read()
myobj=gTTS(text=exe,lang=language,slow=False)
myobj.save("words.mp3")
os.system("start words.mp3")