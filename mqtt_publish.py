import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
sensor=Adafruit_DHT.DHT11
pin=4
#print('Started Sensing....')
mqttBroker="mqtt.eclipseprojects.io"
client=mqtt.Client("Temperature_OFFICE")
client.connect(mqttBroker)
while(True):

    humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)

    #print('Sensing the environment...')

    print('temperature={0:0.1f}C'.format(temperature))

    r=temperature

    client.publish("TEMPERATURE",r)

    #print("Just published "+str(r) + " to topic TEMPERATURE ")

    time.sleep(2)
