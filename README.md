# FUFARM Home Assistant
Home Assistant Hydroponics setup using Docker.

## Adding MQTT users
sudo chown root:root mosquitto/config/mqttuser
./mosquitto/mosquitto_cmd.sh passwd -b  /mosquitto/config/mqttuser hamqtt 'UbT4Rn3oY7!S9L'
