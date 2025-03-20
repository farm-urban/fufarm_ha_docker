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

NB: If device won't attach to FUsensors, attach to main wifi and then login with: ssh fu@100.116.249.80 -L 3333:192.168.55.119:80
http://localhost:333

Configure -> Configure Module -> Module Type
=> Sonoff Pow R2

Configuration -> Configure Other
=> Set the "Device Name" and "Friendly Name 1" to (e.g. FPlug1)

Configuration -> Configure MQTT
MQTT Settings:
Client: Plug1
Host: 192.168.8.100
User: hamqtt
password: UbT4Rn3oY7!S9L
Topic: plug1

## Add Tapo Webcam Integration

1. Download [Tapo App](https://play.google.com/store/apps/details?id=com.tplink.iot&pcampaignid=web_share)
2. Turn on cam (reset with pin if necessary) and connect to hotspot TAPO_CAM_XXXX with phone
3. Setup cam and connect it to the farm wifi hotspot
4. Give the camera a fixed IP in the AP or Raspberry Pi.
5. Create a camera account in the app: **Camera Settings > Advanced Settings > Camera Account**
6. Ensure the [Tapo HA custom component](https://github.com/JurajNyiri/HomeAssistant-Tapo-Control) is installed.
7. In Home Assistant go to: **Settings -> Devices & Services -> +Integration** select **Tapo: Cameras Control**
8. Add the camera with the IP address selected in 4.
9. Add the account details from 4.
10. Add the cloud password for the master Tapo account.

## Notes on setting up a VM

https://community.home-assistant.io/t/guide-home-assistant-on-apple-silicon-mac-using-ha-os-aarch64-image/444785

Site can be accessed at: http://homeassistant.local:8123/
