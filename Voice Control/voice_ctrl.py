"""
speech recognition for voice controlled applications
ref link:-https://www.youtube.com/watch?v=bYNDH9V-Lr4

"""




from subprocess import call
import speech_recognition as sr
import serial
import RPi.GPIO as GPIO      
import os, time
r= sr.Recognizer()
led_r=17
led=27
led_g=22

text = {}
text1 = {}
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led_g, GPIO.OUT)
GPIO.setup(led_r, GPIO.OUT)
GPIO.output(led_r , 0)
GPIO.output(led , 0)
GPIO.output(led_g , 0)

def listen1():
    with sr.Microphone(device_index = 0) as source:
        r.adjust_for_ambient_noise(source)
        print("Hi Afrid, I'm your assitant,how can i help you");
        audio = r.listen(source)
        print("got it");
    return audio
def voice(audio1):
    try:
        text1 = r.recognize_google(audio1) 
##         call('espeak '+text, shell=True)
        print ("you said: " + text1);
        return text1; 
    except sr.UnknownValueError: 
          #call(["espeak", "-s140  -ven+18 -z" , "Google Speech Recognition could not understand"])
        print("please Say Again")
        return "try again";
    except sr.RequestError as e: 
        print("I couldnt get you,repeat again")
        #return text1;
        return "try again";
        
def main(text):
    #print("Hi Afrid, I'm your assitant,how can i help you")
    audio1 = listen1() 
    text = voice(audio1)
    #text = {}
    if 'white on' in text:
        GPIO.output(led , 1)
          #call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching ON the Lights"])
        print ("white Lights turned on")
    elif 'white off' in text:
        GPIO.output(led , 0)
          #call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the Lights"])
        print ("white Lights turned Off")
    elif 'green light' in text:
        GPIO.output(led_g , 1)
          #call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the Lights"])
        print ("green Light turned On")
    elif 'green off' in text:
        GPIO.output(led_g , 0)
          #call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the Lights"])
        print ("green light turned off")
    elif 'red light' in text:
        GPIO.output(led_r, 1)
          #call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the Lights"])
        print ("red lights turned on")
    
    elif 'red off' or 'red light off' in text:
        GPIO.output(led_r, 0)
          #call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the Lights"])
        print ("red light turned off")
    #text = {}
if __name__ == '__main__':
    while(1):
        audio1 = listen1()
        text = voice(audio1)
        text = {}
        main(text)
        if text == 'hello':
            print("Hi your assitance")
            text = {}
         call(["espeak", "-s140  -ven+18 -z" ," Okay master, waiting for your command"])
            #main(text)
     else:
         
         call(["espeak", "-s140 -ven+18 -z" , " Please repeat"])
