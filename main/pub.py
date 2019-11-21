import network
from umqttsimple import MQTTClient 
import machine 
import time 
from machine import Pin as mduPin

qLED = mduPin(2, mduPin.OUT)
qLED.value(0)

def sub_cb(topic, msg): 
   print(msg) 
wlan = network.WLAN(network.STA_IF) 
wlan.active(True)
wlan.connect('VSRND-2G4','0000100001efg')



while not wlan.isconnected():  
    machine.idle() 
print("Connected to Wifi\n") 

client = MQTTClient("device", "io.adafruit.com",user="lky_94",
password="1d49b4f20a16476d993e137e96143e20", port=1883) 
client.set_callback(sub_cb) 
client.connect()
#client.subscribe(topic="lky_94/feeds/switch")

"""
while True:
     
    print("Sending ON") 
    client.publish(topic="lky_94/feeds/switch", msg="ON")
    time.sleep(1) 
    qLED.value(1)
    print("Sending OFF") 
    client.publish(topic="lky_94/feeds/switch", msg="OFF")
    qLED.value(0)
    time.sleep(1) 
"""

"""
while True :
      if client.publish(topic="lky_94/feeds/switch",msg="ON"):
        qled.value(1)
      elif client.publish(topic="lky_94/feeds/switch",msg="OFF"):
        qled.value(0)
"""
        
def Led ():
    client.subscribe(topic="lky_94/feeds/switch")
    if (client.subscribe(topic="lky_94/feeds/switch")).decode("utf-8") == 'ON':
         qLED.value(1)
         print('on')
    elif (client.subscribe(topic="lky_94/feeds/switch")).decode("utf-8") == 'OF':
         qLED.value(0)
         print('off')

while True:

 Led()
    