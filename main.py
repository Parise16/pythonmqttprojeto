import paho.mqtt.client as mqtt

def ao_conectar(client, userdata, flags, rc)
     print("Nos conectamos com o seguinte codigo de resoltado()".forma(str(rc)))

def ao_receber(client,userdata, msg)
    print("() --- ()" .format(msg.topic, str(msg.payload)))
