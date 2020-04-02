import subprocess
from gtts import gTTS
from playsound import playsound
import os

mytext = "Welcome to our Grocery Store."

language = 'en'

myobj = gTTS(text=mytext, lang=language)

myobj.save("welcome.mp3")
playsound('welcome.mp3')
#os.system("rm -rf welcome.mp3")
#subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

