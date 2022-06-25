from gttS import gTTS 
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="kranthi is good boy",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print('@@@@@@@sound is playing')