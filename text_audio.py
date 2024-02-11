from gtts import gTTS
import os
file=open("file1.txt", "r")
output=gTTS(text=file.read(),lang= "bn", slow=False )
output.save("output.mp3")
file.close()
os.system("start output.mp3")