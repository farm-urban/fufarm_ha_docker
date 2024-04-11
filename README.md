# FUFARM Home Assistant
Home Assistant Hydroponics setup using Docker.

## Adding MQTT users
sudo chown root:root mosquitto/config/mqttuser
./mosquitto/mosquitto_cmd.sh passwd -b  /mosquitto/config/mqttuser homeassistant "1234567890"
