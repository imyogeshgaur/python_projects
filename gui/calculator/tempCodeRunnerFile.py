import gtts,os
from gtts import gTTS
tts=gTTS("Hi,this is yogesh gaur and i start working on text to speech from today",lang='en',slow=True)
tts.save("into.mp3")
os.system("intro.mp3")
os.remove("into.mp3")
