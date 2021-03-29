import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
import math

leds = [10, 9, 11, 5, 6, 13, 19, 26]
names = [0, 1, 2, 3, 4, 5, 6, 7]

def lightUp(ledNumber,period):
    GPIO.setup(ledNumber,GPIO.OUT)
    GPIO.output(ledNumber,1)
    time.sleep(period)
    GPIO.setup(ledNumber,GPIO.OUT)
    GPIO.output(ledNumber,0)


def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        blinkCount -= 1
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)

def runningLight(count,period):
    while count!=0:
        count-=1
        for i in range(8):
            lightUp(leds[i],period)
        time.sleep(period)

def smertb(ledNumber,period):
    GPIO.setup(ledNumber,GPIO.OUT)
    GPIO.output(ledNumber,0)
    time.sleep(period)
    GPIO.output(ledNumber,1)

def runningDark(count,period):
    for i in range(8):
        GPIO.setup(leds[i],GPIO.OUT)
        GPIO.output(leds[i],1)
    for i in range(count):
        for i in range(8):
            smertb(leds[i],period)
        time.sleep(period)
    for i in range(8):
        GPIO.setup(leds[i],GPIO.OUT)
        GPIO.output(leds[i],0)

def decToBinList(decNumber):
    result=[]
    while decNumber:
        result.append(decNumber %2)
        decNumber=decNumber//2
    if len(result) < 8:
        for i in range(7-len(result)):
            result.append(0)
        result.append(0)
    result.reverse()
    print(result)
    return(result)

def lightNumber(number):
    s = decToBinList(number)
    s.reverse()
    print(s)
    for i in range(8):
        GPIO.setup(leds[i],GPIO.OUT)
        GPIO.output(leds[i],0)

   
    for i in range(len(s)):
        if s[i]>0: 
            GPIO.setup(leds[i],GPIO.OUT)
            GPIO.output(leds[i],1)
   
def chastokol(t):
    while t>0:
        for i in range(0,255):
            lightNumber(i)
            time.sleep(0.01)
        for h in range(0,255):
            lightNumber(255-h)
            time.sleep(0.01)
        t-=1        


#GPIO.cleanup()
#lightUp(25,4)
#blink(20, 5, 0.3)
#runningLight(3, 0.1)1

#runningDark(3, 0.1)
#decToBinList(31)
#while True:
#    n=int(input())
#    if n ==-1:
#        break
 #   lightNumber(n)
#f=int(input())
#chastokol(f)

def sinus(time,per,obn):
  
    t=round(time/obn)
    b=per/obn
    raz=b/255
    l=[]
    for i in range(t):
        r=255*round(math.sin(math.pi*i/b))
        l.append(r)
        lightNumber(r)
        time.sleep(1/obn)


time=int(input())
per=int(input())
obn=int(input())
sinus(time,per,obn)
