# home-assistant
Farm controlled with Home Assistant


## Adding MQTT users
sudo chown root:root mosquitto/config/mqttuser
./mosquitto/mosquitto_cmd.sh passwd -b  /mosquitto/config/mqttuser homeassistant "1234567890"