import random
import time

from paho.mqtt import client as mqtt_client

broker = 'm16.cloudmqtt.com'
port = 15372
topic = 'outTopic'
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'dwvkqzpd'
password = 'uEzJFy5rb_Ra'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected to Mqtt Broker!')
        else:
            print('ailed to connect, return code %d\n', rc)
    
    #connecting to client id
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while(True):
        time.sleep(1)
        msg = f'messages: {msg_count}'
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f'Send {msg} to topic {topic}')
        else:
            print(f'failed to send message to topic {topic}')
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()


            
