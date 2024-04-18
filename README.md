# FUFARM Home Assistant
Home Assistant Hydroponics setup using Docker.

## Add MQTT user
sudo chown root:root mosquitto/config/mqttuser
./mosquitto/mosquitto_cmd.sh passwd -b  /mosquitto/config/mqttuser hamqtt 'UbT4Rn3oY7!S9L'

## Add MQTT Integration in HA
Settings -> Devices and Services -> Add Integration -> MQTT -> MQTT:
Broker: mosquitto
Port: 1883
Username: <User Added to MQTT in Step 1>
Password: <Password Added to MQTT in Step 1>


## To add Tasmota Devices connect to MQTT with:
Set the DeviceName and Friendly Name to (e.g. Plug1)
MQTT Settings:
host: 192.168.5.1
user: hamqtt
password: UbT4Rn3oY7!S9L
