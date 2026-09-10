# FUFARM Home Assistant

Home Assistant Hydroponics setup using Docker.

## Add Edenic Integration
Clone the [fufarm_ha_edenic[(https://github.com/farm-urban/fufarm_ha_edenic) repository.

Link the custom_components/edenic_bluelab directory into the Home Assistant custom_components directory and edit the docker-compose.yml file.

Add the Integration in Home Assistant.

## Add ESPHome integration
See the [fufar_esphome](https://github.com/farm-urban/fufarm_esphome) repository.

## Add Tapo Webcam Integration

1. Download [Tapo App](https://play.google.com/store/apps/details?id=com.tplink.iot&pcampaignid=web_share)
2. Turn on cam (reset with pin if necessary) and connect to hotspot TAPO_CAM_XXXX with phone
3. Setup cam and connect it to the farm wifi hotspot
4. Give the camera a fixed IP in the AP or Raspberry Pi.
5. Create a camera account in the app: **Camera Settings > Advanced Settings > Camera Account**
6. Add integration **Generic Camera**:

   - rtsp://<FIXED_IP>/stream2
   - RTSP transport protocol: TCP
   - Authentication: basic
   - Username and Password for camera.
   - Uncheck `Verify SSL certificate`

> **NB: below seems to be broken currently - can't log into main Tapo account, but is not required for what we need** 7. Ensure the [Tapo HA custom component](https://github.com/JurajNyiri/HomeAssistant-Tapo-Control) is installed. 8. In Home Assistant go to: **Settings -> Devices & Services -> +Integration** select **Tapo: Cameras Control** 9. Add the camera with the IP address selected in 4. 10. Add the account details from 4. 11. Add the cloud password for the master Tapo account.

## Setup backups

- Settings -> System -> Backups
- Create automatic backups into the directory `config/backups`
- Install rclone `sudo apt-get install rclone`
- Congigure rclone to sync backups to S3 storage e.g. `~/.config/rclone/rclone.conf`:

  ```[katapault]
  type = s3
  provider = Other
  access_key_id = XXXX
  secret_access_key = YYYYY
  endpoint = uk-lon-1.katapultobjects.com:443
  ```

- Use cron to configure rclone to sync backups to external repository `contab -e`

  ```# m h  dom mon dow   command
  MAILTO="it@farmurban.co.uk"
  0 5 * * * rclone sync --s3-no-check-bucket  /opt/home-assistant/config/backups katapault:fu-backups/farmpi
  ```
---
# IGNORE - Below this line are the old setup notes

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

## Additional Tasmota Configuration

We've encountered issues with Tasmota switches disconnecting and not being triggered correctly. The following settings are attempts to try and fix this.

| Command             | Description                                                                           |
| ------------------- | ------------------------------------------------------------------------------------- |
| `WifiConfig 5`      | Stick to one AP only, no roaming                                                      |
| `SetOption57 0`     | Disable WiFi network rescan every 44 minutes                                          |
| `PowerOnState 3`    | switch power(s) to their last saved state (Tasmota default but changed in LocalBytes) |
| `MqttKeepAlive 100` | Default is 30                                                                         |

To set with a single command:

`Backlog WifiConfig 5; SetOption57 0; PowerOnState 3; MqttKeepAlive 100`

This seems to work, but it's not clear which was the magic setting that fixed things.

To enable deeper debugging: `Backlog WebLog 4; MQTTLog 2`

To disable debugging: `Backlog WebLog 2; MQTTLog 0`
