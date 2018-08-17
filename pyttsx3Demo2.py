import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
voices = engine.getProperty('voices')
print(voices)
for voice in voices:
    print(voice.name)
    engine.setProperty('voice', voice.id)
    engine.say('我最近喜欢听周杰伦的个')
    engine.runAndWait()