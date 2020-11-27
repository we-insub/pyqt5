from gtts import gTTS
import pyglet

text = " 안녕 하세요. 오늘은 2020년 11월 24일 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("helloEN.mp3")

mp3File = pyglet.media.load("helloen.mp3")
mp3File.play()
pyglet.app.run()