# FUFARM Home Assistant

Home Assistant Hydroponics setup using Docker.

## Add MQTT user

sudo chown root:root mosquitto/config/mqttuser
./mosquitto/mosquitto_cmd.sh passwd -b /mosquitto/config/mqttuser hamqtt 'UbT4Rn3oY7!S9L'

## Add MQTT Integration in HA

Settings -> Devices and Services -> Add Integration -> MQTT -> MQTT:
Broker: mosquitto
Port: 1883
Username: <User Added to MQTT in Step 1>
Password: <Password Added to MQTT in Step 1>

## Add Tasmota Integration

Settings -> Devices and Services -> Add Integration -> Tasmota

### Configure Tasmota Devices connect to MQTT with:

Configure -> Configure Module -> Module Type
=> Sonoff Pow R2

Configuration -> Configure Other
=> Set the "Device Name" and "Friendly Name 1" to (e.g. FPlug1)

Configuration -> Configure MQTT
MQTT Settings:
Client: FPlug1
Host: 192.168.5.1
User: hamqtt
password: UbT4Rn3oY7!S9L
Topic: fplug1

## Notes on setting up a VM

https://community.home-assistant.io/t/guide-home-assistant-on-apple-silicon-mac-using-ha-os-aarch64-image/444785

Site can be accessed at: http://homeassistant.local:8123/
