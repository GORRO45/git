import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)
import time
leds = [10, 9, 11, 5, 6, 13, 19, 26]
names = [0, 1, 2, 3, 4, 5, 6, 7]


def decToBinList(decNumber):
    result=[]
    while decNumber:
        result.append(decNumber %2)
        decNumber=decNumber//2
    if len(result) < 8:
        for i in range(7-len(result)):
            result.append(0)
        result.append(0)
#    result.reverse()
    
    return(result)
def lightNumber(number):
    s = decToBinList(number)
    s.reverse()
   
    for i in range(8):
        GPIO.setup(leds[i],GPIO.OUT)
        GPIO.output(leds[i],0)

   
    for i in range(len(s)):
        if s[i]>0: 
            GPIO.setup(leds[i],GPIO.OUT)
            GPIO.output(leds[i],1)


#while True:
#    n=int(input())
#    if n==-1:
#        break
#    print(n*33/2550)
#    lightNumber(n)
GPIO.setwarnings(False)
def dac_data(d):
    for i in range(0,8):
        for k in range(8):
            GPIO.setup(leds[k],GPIO.OUT)
      
        GPIO.output(leds[i],d[i])
def abc():
    for j in range(0,2**8):
        dac_data(decToBinList(j))
        time.sleep(0.001)
        GPIO.setup(4,GPIO.IN)
        if GPIO.input(4)==0:
            print(j,j*33/2550)
            break 
    return(j)
while True:
    abc()

