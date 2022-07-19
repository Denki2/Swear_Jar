import speech_recognition as sr
from pocketsphinx import LiveSpeech
import pynput
from pynput.keyboard import Key, Listener
import vlc
import pafy

mediaUrl = "https://www.youtube.com/watch?v=5UC4Le9jbQY&ab_channel=ComercialesenLikeM%C3%A9xico"
media = pafy.new(mediaUrl)
best = media.getbest()
player = vlc.MediaPlayer(best.url)


def stopMusic():
    listenState = False
    def on_press(key):

        try:
            print('alphanumeric key {0} pressed'.format(key.char))
         
        except AttributeError:
            print('special key {0} pressed'.format(key))
              
    def on_release(key):
                     
        print('{0} released'.format(key))
        if key == Key.esc:
            player.stop()
            return False

  
  
    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
        return



speech = LiveSpeech(lm = False, kws='keyphrase.list', dic = "keyphrase.dic")
for phrase in speech:
    print(phrase)
    player.play()
    stopMusic()
    




  
  

    


